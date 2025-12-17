# 🌾 Crop Recommendation Using Machine Learning

An interactive **Streamlit-based Crop Recommendation System** that suggests the most suitable crop based on **soil nutrients** and **environmental conditions**. The system leverages a trained **machine learning pipeline** to analyze user inputs and provide accurate crop predictions along with confidence scores.

---

## 🚀 Features

* User-friendly **Streamlit web interface**
* Input parameters include:

  * Nitrogen (N)
  * Phosphorus (P)
  * Potassium (K)
  * Temperature (°C)
  * Humidity (%)
  * Soil pH
  * Rainfall (mm)
* Predicts the **most suitable crop**
* Displays **prediction confidence (probability score)**
* Fast and lightweight inference using a pre-trained ML pipeline

---

## 🧠 How the Application Works

1. The application loads the following trained artifacts:

   * `pipeline` – Machine learning model pipeline
   * `label_encoder` – Encodes crop labels
   * `feature_columns` – Expected input feature order
2. The user enters soil and weather parameters through the UI.
3. Input values are converted into a Pandas DataFrame.
4. The model predicts class probabilities using:

   ```python
   pipeline.predict_proba(df)
   ```
5. The crop with the **highest probability** is selected and displayed.

---

## 🛠️ Technologies Used

* **Python**
* **Streamlit** – Web application framework
* **NumPy** – Numerical operations
* **Pandas** – Data manipulation
* **Joblib** – Model serialization
* **Scikit-learn** – Machine learning model training and inference

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/crop-recommendation.git
cd crop-recommendation
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
├── app.py                            # Streamlit application
├── crop_recommendation_model.pkl     # Trained ML model bundle
├── requirements.txt                  # Project dependencies
└── README.md                         # Project documentation
```

---

## 🔍 Code Overview

### 1. Load the Trained Model

```python
bundle = joblib.load("crop_recommendation_model.pkl")
pipeline = bundle["pipeline"]
label_encoder = bundle["label_encoder"]
feature_columns = bundle["feature_columns"]
```

### 2. User Input Handling

* Streamlit number input fields are generated dynamically based on `feature_columns`.

### 3. Prediction Logic

```python
proba = pipeline.predict_proba(df)[0]
```

### 4. Display Results

* The crop with the highest probability is decoded using the label encoder.
* Output shown as:

  * **Recommended Crop**
  * **Confidence Score**

---

## ✅ Use Case

This system can assist:

* Farmers in choosing the right crop
* Agricultural researchers
* Smart farming and AgriTech applications

---

## 📌 Future Enhancements

* Support for multiple crop recommendations
* Visualization of probability distribution
* Integration with real-time weather APIs
* Deployment on cloud platforms

---

## 📄 License

This project is intended for **educational and research purposes**.

---

⭐ If you find this project useful, consider giving it a star!
