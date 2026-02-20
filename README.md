# ML-Based-Microplastic-Detection-and-Voice-Aware-System






## 📌 Overview

This project is an **ML-based microplastic detection system** that uses a trained **Convolutional Neural Network (CNN)** to classify drinking water images as either **Safe** or **Contaminated**.

The system includes a **Streamlit-based web interface** that supports image upload and webcam capture, along with **voice alerts (English)** to provide real-time safety feedback.

This project demonstrates the complete machine learning pipeline:

* Data preprocessing
* Model training
* Model evaluation
* Web deployment

---

## 🚀 Features

* CNN-based image classification
* 91% model accuracy
* Image upload functionality
* Live webcam capture
* Voice alert (English)
* Confusion matrix performance evaluation
* Streamlit web deployment
* Clean and modular project structure

---

## 🧠 Model Details

| Parameter     | Value                              |
| ------------- | ---------------------------------- |
| Model Type    | Convolutional Neural Network (CNN) |
| Input Size    | 128 × 128 RGB                      |
| Optimizer     | Adam (Adaptive Moment Estimation)                             |
| Loss Function | Binary Crossentropy                |
| Epochs        | 20                                 |
| Accuracy      | 91%                                |
| F1-Score      | 0.91                               |

---

## 📊 Model Performance

### Confusion Matrix

```
[[91  9]
 [ 9 91]]
```

### Evaluation Metrics

* **Accuracy:** 91%
* **Precision:** 91%
* **Recall:** 91%
* **F1-Score:** 0.91

The model demonstrates balanced classification performance with equal false positives and false negatives.

---

## 🏗 Project Structure

```
MP1/
│
├── data/
│   ├── 1_Training/
│   ├── 3_Testing/
│
├── src/
│   ├── train.py
│   ├── model.py
│   ├── utils.py
│   ├── config.py
│
├── stream.py
├── microplastic_model.h5
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```
git clone <your-repository-link>
cd <repository-folder>
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Train the Model

```
python src/train.py
```

The trained model will be saved as:

```
microplastic_model.h5
```

---

## 🌐 Run the Web Application

```
streamlit run stream.py
```

Open the local URL displayed in the terminal (usually:
[http://localhost:8501](http://localhost:8501))

---

## 🔮 Future Improvements

* Increase dataset size for better generalization
* Improve recall for safety-critical detection
* Deploy the application to cloud platforms (Streamlit Cloud / AWS)
* Add mobile-responsive UI
* Integrate real-time water quality sensor data

---

## 🎯 Impact

This project demonstrates the practical application of **machine learning and computer vision** in environmental safety monitoring. It highlights the implementation of a complete ML pipeline along with real-world deployment through an interactive web interface.

---

