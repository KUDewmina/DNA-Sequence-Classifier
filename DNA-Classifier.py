from flask import Flask, render_template, request, jsonify
import tensorflow as tf
from utils.train import MAX_LEN, one_hot_encode, le
from utils.dataset import motifs_dict
from keras.models import load_model
import numpy as np
import pandas as pd
import os

app = Flask(__name__)

model = load_model("utils/dna_classifier.keras")

@app.route('/')
def home():
    return render_template('DNA.html')

@app.route("/classify", methods=["POST"])
def predict():
    dna_sequence = request.form["sequence"]
    X_new = np.array([one_hot_encode(dna_sequence, MAX_LEN)])
    pred = model.predict(X_new)
    pred_percent = pred[0] * 100
    pred_percent = (np.round(pred_percent, 2)).tolist()
    probs = [round(x) for x in pred_percent]
    class_label = le.inverse_transform([np.argmax(pred)])[0]

    with open("utils/accuracy.txt", "r") as f:
            lines = f.readlines()
            test_acc = float(lines[0].strip()) 

    return jsonify({
        "sequence": dna_sequence,
        "probabilities": probs,
        "predicted_class": class_label,
        "confidence": max(pred_percent),
        "detected_motifs": motifs_dict[class_label],
        "model_accuracy": str(test_acc) + "%",
        "interpretation": "This sequence is most likely from the " + class_label + " class"
    })

@app.route("/add_to_dataset", methods=["POST"])
def data_input():
    new_sequence = request.form["new_sequence"].strip().upper()
    new_sequence = new_sequence.replace(",", "")
    new_label = request.form["class_label"].strip()

    valid_nucs = ['A','T','C','G']

    for nuc in new_sequence:
        if nuc not in valid_nucs:
            return jsonify({"message":"Sequence is not valid"}), 400

    if not new_sequence or not new_label:
        return jsonify({"message":"Missing sequence or class"}), 400

    min_len = 50
    if len(new_sequence) < min_len:
        new_sequence = new_sequence.ljust(min_len, 'A')

    df = pd.read_csv("utils/dna_dataset.csv", usecols=["Sequence", "Class_Label"])  # ignore extra columns

    new_row = pd.DataFrame([{"Sequence": new_sequence, "Class_Label": new_label}])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv("utils/dna_dataset.csv", index=False)

    return jsonify({"message":"New data added successfully !"})

@app.route("/retrain_model", methods=["POST"])
def retrain_model():
    global model
    import utils.train as train_module
    train_module.retrain_model()
    model = load_model("utils/dna_classifier.keras")
    with open("utils/accuracy.txt", "r") as f:
            lines = f.readlines()
            test_acc = float(lines[0].strip())  
            train_acc = float(lines[1].strip())
            try:
                quality = str(lines[2].strip())
            except:
                 quality = ""
    
    return jsonify({"message":"Model retrained successfully with " + str(test_acc) + "% of test accuracy and " + str(train_acc) + "% of train accuracy ! " + quality})

@app.route("/reset_dataset", methods=["POST"])
def restore_dataset():
    import shutil

    shutil.copy("utils/dna_dataset_original.csv", "utils/dna_dataset.csv")
    return jsonify({"message": "Dataset restored to original!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))


