# 🧬 DNA Sequence Classifier

![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![TensorFlow](https://img.shields.io/badge/tensorflow-2.15-orange)
![Flask](https://img.shields.io/badge/flask-2.3-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)

A deep learning-based **DNA sequence classifier** that predicts the origin of a DNA sequence (Virus, Bacteria, Human, Plant) and highlights detected motifs. Built with **Keras, TensorFlow, and Flask** for interactive web deployment.

---

<img width="1892" height="927" alt="Screenshot 2025-12-07 075714" src="https://github.com/user-attachments/assets/a27bf03a-bd9f-44b5-90ce-6c3347140032" />
<img width="1714" height="915" alt="Screenshot 2025-12-07 080656" src="https://github.com/user-attachments/assets/5b1e5cc8-e246-483e-9e8f-befc78d4ecd8" />

## 🌟 Features

- ✅ **Sequence Classification** – Classify DNA sequences into multiple categories.  
- ✅ **Motif Detection** – Detect common motifs in sequences.  
- ✅ **Add New Sequences** – Expand the dataset directly from the web interface.  
- ✅ **Retrain Model** – Retrain the classifier on new data with **live progress visualization**.  
- ✅ **Reset Dataset** – Restore the original dataset with one click.  
- ✅ **Beautiful Dashboard** – DNA-themed progress circles and interactive UI.  

---

## 💾 Dataset

- Original dataset: `utils/dna_dataset_original.csv`  
- Active dataset: `utils/dna_dataset.csv`  
- Supports **adding new sequences** through the web app.

---

## ⚡ Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/DNA-Sequence-Classifier.git
cd DNA-Sequence-Classifier
