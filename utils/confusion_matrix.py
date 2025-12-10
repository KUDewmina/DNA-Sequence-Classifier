def confusion_matrix():
        import numpy as np
        import pandas as pd
        import seaborn as sns
        import matplotlib.pyplot as plt
        from sklearn.metrics import confusion_matrix, classification_report
        from keras.models import load_model
        from sklearn.preprocessing import LabelEncoder

        df = pd.read_csv("utils/dna_dataset.csv")  

        model = load_model("utils/dna_classifier.keras")


        MAX_LEN = max(df["Sequence"].str.len().max(), 500)  

        def one_hot_encode(seq, max_len=MAX_LEN):
            mapping = {'A':[1,0,0,0,0],'C':[0,1,0,0,0],'G':[0,0,1,0,0],'T':[0,0,0,1,0],'N':[0,0,0,0,1]}
            seq = seq.upper()
            seq = seq[:max_len].ljust(max_len, 'N')
            seq = [b if b in mapping else 'N' for b in seq]
            return np.array([mapping[b] for b in seq])


        X = np.array([one_hot_encode(seq) for seq in df["Sequence"]])

        class_col = "Class" if "Class" in df.columns else "Class_Label"
        true_labels = df[class_col].values

        le = LabelEncoder()
        le.fit(["Human", "Bacteria", "Plant", "Virus"])  
        y_true = le.transform(true_labels)

        y_pred_proba = model.predict(X, verbose=0)
        y_pred = np.argmax(y_pred_proba, axis=1)

        cm = confusion_matrix(y_true, y_pred)

        plt.figure(figsize=(10, 8))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                    xticklabels=le.classes_,
                    yticklabels=le.classes_,
                    linewidths=2, linecolor='black')

        plt.title('DNA Sequence Classifier - Confusion Matrix', fontsize=18, pad=20)
        plt.xlabel('Predicted Class', fontsize=14)
        plt.ylabel('True Class', fontsize=14)
        plt.tight_layout()

        # Save and show
        plt.savefig("confusion_matrix.png", dpi=300, bbox_inches='tight')
        plt.show()

        print("\n" + "="*60)
        print("CLASSIFICATION REPORT")
        print("="*60)
        print(classification_report(y_true, y_pred, target_names=le.classes_))
        print("="*60)
        print(f"Total sequences tested: {len(df)}")
        print(f"Overall Accuracy: {np.mean(y_true == y_pred)*100:.2f}%")

if __name__ == "__main__":
    confusion_matrix()