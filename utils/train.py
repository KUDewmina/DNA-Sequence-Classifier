import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Conv1D, MaxPooling1D, GlobalMaxPooling1D, Dense, Dropout
from keras.callbacks import EarlyStopping, ReduceLROnPlateau

df = pd.read_csv("utils/dna_dataset.csv")

MAX_LEN = df["Sequence"].str.len().max()
accuracy = 89

def one_hot_encode(seq, max_len=MAX_LEN):
    mapping = {'A':[1,0,0,0],'C':[0,1,0,0],'G':[0,0,1,0],'T':[0,0,0,1]}
    seq = seq.upper()
    seq = seq[:max_len].ljust(max_len, 'A')
    return np.array([mapping[b] for b in seq])

le = LabelEncoder()
y_labels = le.fit_transform(df["Class_Label"])
y = to_categorical(y_labels, num_classes=4)

X = np.array([one_hot_encode(s, MAX_LEN) for s in df.Sequence])

def retrain_model(epochs=20, batch_size=32):

    global accuracy

    X_train, X_temp, y_train, y_temp = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    X_val, X_test, y_val, y_test = train_test_split(
        X_temp, y_temp, test_size=0.5, random_state=42, stratify=y_temp
    )

    model = Sequential([
        Conv1D(128, 9, activation='relu', padding='same'),
        MaxPooling1D(4),
        Dropout(0.3),

        Conv1D(256, 7, activation='relu', padding='same'),
        MaxPooling1D(4),
        Dropout(0.4),

        Conv1D(512, 5, activation='relu', padding='same'),
        GlobalMaxPooling1D(),

        Dense(256, activation='relu'),
        Dropout(0.5),

        Dense(4, activation='softmax')
    ])

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    early_stop = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
    reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=2, min_lr=1e-6, verbose=1)

    history = model.fit(
        X_train, y_train,
        validation_data=(X_val, y_val),
        epochs=epochs,
        batch_size=batch_size,
        shuffle=True,
        callbacks=[early_stop, reduce_lr],
        verbose=1
    )

    loss, acc = model.evaluate(X_test, y_test)
    test_acc = round(acc * 100, 2)
    train_acc = round(history.history['accuracy'][-1] * 100, 2)

    fitting = abs(test_acc - train_acc)
    quality = "No specific assessment for this accuracy range."
    if fitting<=6 and test_acc>=85 and train_acc>=88 :
         quality = "The model generalizes well, learning motifs and patterns instead of memorizing sequences."
    elif fitting<=6 and test_acc<85 and train_acc<88 :
         quality = "Trained model doesn't have enough capacity to detect patterns in sequences.DNA sequences are highly structured: they have motifs, conserved regions, repeats, etc. Network is too shallow to learn these motifs properly."
    elif fitting>6 and test_acc<85 and train_acc>=88 :
         quality = "Model is very deep on limited dataset, it memorizes the exact motif combinations in training sequences instead of learning general patterns.Model may only recognize motifs at fixed positions."

    with open("utils/accuracy.txt", "w") as f:
        f.write(f"{test_acc}\n{train_acc}\n{quality}")
        
    print("\n==================================")
    print("Test Accuracy:", test_acc, "%")
    print("Train Final Accuracy:",train_acc , "%")
    print("==================================")

    model.save("utils/dna_classifier.keras")
    print("Model retrained and saved!")

    return model  

if __name__ == "__main__":
    retrain_model()
