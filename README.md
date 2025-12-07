# 🧬 DNA Sequence Classifier

![Python](https://img.shields.io/badge/python-3.11.0-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/flask-3.1.2-000000?style=flat-square&logo=flask&logoColor=white)
![Keras](https://img.shields.io/badge/keras-3.11.3-D00000?style=flat-square&logo=keras&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-2.3.5-013243?style=flat-square&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-2.3.3-150458?style=flat-square&logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.7.2-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![TensorFlow](https://img.shields.io/badge/tensorflow-2.20.0-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)


A deep learning-based **DNA sequence classifier** that predicts the origin of a DNA sequence (Virus, Bacteria, Human, Plant) and highlights detected motifs. Built with **Keras, TensorFlow, and Flask** for interactive web deployment.

---

<img width="1548" height="1472" alt="Untitled-3" src="https://github.com/user-attachments/assets/8892f770-7ef4-4be6-956b-3f14e89bb6cf" />


## 🌟 Features

- ✅ **Sequence Classification** – Classify DNA sequences into multiple categories.  
- ✅ **Motif Detection** – Detect common motifs in sequences.  
- ✅ **Add New Sequences** – Expand the dataset directly from the web interface.  
- ✅ **Retrain Model** – Retrain the classifier on **new DNA sequences**.  
- ✅ **Reset Dataset** – Restore the original dataset with one click.  
- ✅ **Beautiful Dashboard** – DNA-themed progress circles and interactive UI.  

---

## 💾 Dataset

- Original dataset (generated based on motifs and considering mutations on four classes) : `utils/dna_dataset_original.csv`  
- Active dataset: `utils/dna_dataset.csv`  
- Supports **adding new sequences** through the web app.

---

## Structure of Neural Network model
<img width="2100" height="1500" alt="Untitled-1" src="https://github.com/user-attachments/assets/37773173-7948-4177-aae1-d1c321f39562" />


## Why This Architecture Works So Well for DNA

- **Large receptive field** → detects motifs anywhere in sequence
- **Hierarchical learning** → short → medium → long-range patterns
- **Global pooling** → position-independent motif detection
- **Heavy dropout** → robust to mutations and noise
- **Trained end-to-end** → learns biologically meaningful features automatically

## ⚡ Setup

### 1. Clone the repository
```bash
git clone https://github.com/KUDewmina/DNA-Sequence-Classifier.git
cd DNA-Sequence-Classifier
