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

<img width="1895" height="923" alt="Screenshot 2025-12-07 081420" src="https://github.com/user-attachments/assets/e6a1735b-9600-49cb-a194-20393250e6db" />
<img width="1714" height="915" alt="Screenshot 2025-12-07 080656" src="https://github.com/user-attachments/assets/5f943d0f-e550-496d-a2bd-4a8bc22767a0" />


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

## ⚡ Setup

### 1. Clone the repository
```bash
git clone https://github.com/KUDewmina/DNA-Sequence-Classifier.git
cd DNA-Sequence-Classifier
