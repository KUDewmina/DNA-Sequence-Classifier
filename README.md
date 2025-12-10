# 🧬 DNA Sequence Classifier

![Python](https://img.shields.io/badge/python-3.11.0-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/flask-3.1.2-000000?style=flat-square&logo=flask&logoColor=white)
![Keras](https://img.shields.io/badge/keras-3.11.3-D00000?style=flat-square&logo=keras&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-2.3.5-013243?style=flat-square&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-2.3.3-150458?style=flat-square&logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.7.2-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![TensorFlow](https://img.shields.io/badge/tensorflow-2.20.0-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)


 ## A Deep learning–based application designed to determine the biological origin of a DNA sequence.Built with **Keras, Tensorflow, and Flask** for interactive web deployment.

 ### 🔍 Classification Targets

> - 🦠 **Virus**
> - 🧫 **Bacteria**
> - 🌱 **Plant**
> - 🏃‍♂️ **Human**

---

<img width="1548" height="1472" alt="Untitled-3" src="https://github.com/user-attachments/assets/490086dd-8df2-4385-9e67-a5c1c1509be7" />



## 🌟 Features

- ✅ **Sequence Classification** – Classify DNA sequences into multiple categories.  
- ✅ **Motif Detection** – Detect common motifs in sequences.  
- ✅ **Add New Sequences** – Expand the dataset directly from the web interface⭐️.  
- ✅ **Retrain Model** – Retrain the classifier on **new DNA sequences**. (Retraining time will depend on your system settings). 
- ✅ **Reset Dataset** – Restore the original dataset with one click.  
- ✅ **Beautiful Dashboard** – DNA-themed progress circles and interactive UI.  

---

## 📑 Dataset

- Original dataset (generated based on motifs and considering mutations on four classes) : `utils/dna_dataset_original.csv`  
- Active dataset: `utils/dna_dataset.csv`  
- Supports **adding new sequences** through the web app.

---

## 🧮 Structure of Neural Network model
<img width="2100" height="1500" alt="Untitled-1" src="https://github.com/user-attachments/assets/37773173-7948-4177-aae1-d1c321f39562" />


### Why This Architecture Works So Well for DNA

- **Large receptive field** → detects motifs anywhere in sequence
- **Hierarchical learning** → short → medium → long-range patterns
- **Global pooling** → position-independent motif detection
- **Heavy dropout** → robust to mutations and noise
- **Trained end-to-end** → learns biologically meaningful features automatically

<img width="2789" height="2368" alt="confusion_matrix" src="https://github.com/user-attachments/assets/82791f48-e72f-472e-a0c0-c82afcf29a74" />


## ⚡ Automated Setup (Simple and Fast)

### Clone the repository
```bash
git clone https://github.com/KUDewmina/DNA-Sequence-Classifier.git
cd DNA-Sequence-Classifier
```
### Or download the ZIP file, extract it, and run the `setup.bat` file.

If your browser doesn't open and run application , Open browser and paste this command
```bash
http://127.0.0.1:5000
```
The user interface will load correctly.

## ⚡ Manual Setup 

Follow this guide if you prefer to configure the app manually.

### 1. Install Python 3.11.0

Download from :
https://www.python.org/downloads/release/python-3110/

#### During installation:

✔ Enable “Add Python to PATH”

✔ Choose Install for all users

#### Check version:
```bash
python --version
```

### 2. Create a Virtual Environment

#### Inside the project folder:
```bash
py -3.11 -m venv venv
```

### 3. Activate Virtual Environment
**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the App
```bash
python dna_classifier.py
```
#### Then open:
```bash
http://127.0.0.1:5000
```

---

## 🤝 Contributing

### Pull requests and feature suggestions are welcome!
### If you’d like to improve accuracy, UI, dataset quality, or add new tools — feel free to contribute.
