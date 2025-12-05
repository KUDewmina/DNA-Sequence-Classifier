from train import one_hot_encode,MAX_LEN,le
import numpy as np
from keras.models import load_model

model = load_model("utils/dna_classifier.keras")
test_seq = "CGAGTCGTCGCAGACTAGCGACAAACAATCGTCTCTATGGCTAATTGGCATCGGCCAGACAGCTAAGTATCGATGTTATTCGAGTTTGTCGGTACATATAATCACACCCATTAGTTTCCGTCTAATGTTCTTACTTACCATCACATCCACCAGAGTCCATTGGATCGGGAATCATGGCAAAACGCCGCCGGTATTGGACAATATTGCGGTGGCTGTCCGAATGACTCGGTATCAAAAACGTTACCAGTGTCAAGGTACCTGTGAAGCCCGCTCCAAATCACAAGGAGAGGCCCTGTTTCCTGCCGAGTACTGGTTGCAGGGACAAACGTATAAATGCTAACGCAGCGCACGGGTACCCCAATACAAGGGTTCCAATGTATTAGAAAGGACAGTGCCGCGG"
X_new = np.array([one_hot_encode(test_seq, MAX_LEN)])
pred = model.predict(X_new)
print(pred)
pred_percent = pred[0] * 100
pred_percent = (np.round(pred_percent, 2)).tolist()
#probs = list(map(int, pred_percent))
probs = [round(x) for x in pred_percent]
print(probs)
print(type(probs[0]))
print("Predicted class:", le.inverse_transform([np.argmax(pred)])[0])