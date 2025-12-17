# crop-recommendation-using-ml
This project is an interactive Streamlit-based Crop Recommendation System that suggests the most suitable crop based on soil nutrients and environmental conditions. It uses a trained machine learning model to analyze user inputs and provide accurate crop predictions along with confidence scores.
**Features**
- Interactive Streamlit UI
- Inputs for:
- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- Soil pH
- Rainfall
** How the App Works**
- The app loads:
- pipeline (ML model)
- label_encoder
- feature_columns
- User enters soil and weather values.
-  **The model predicts probabilities using:**
-  pipeline.predict_proba(df)
- The app displays:
- The highest probability crop


**Technologies Used**
- Python
- Streamlit
- NumPy
- Pandas
- Joblib
- Scikit-learn (for the trained model).


Installation & Setup
1. Clone the repository
git clone https://github.com/your-username/crop-recommendation.git
cd crop-recommendation.

2. Install dependencies.
   pip install -r requirements.txt

3. Run the Streamlit app.
   streamlit run app.py
4. Project Structure
├── app.py                         # Streamlit application
├── crop_recommendation_model.pkl  # Trained ML model
├── requirements.txt               # Dependencies
└── README.md                      # Documentation



 **Code Explanation**
1. Load model
bundle = joblib.load("crop_recommendation_model.pkl")
pipeline = bundle["pipeline"]
label_encoder = bundle["label_encoder"]
feature_columns = bundle["feature_columns"]

2.User inputs
Streamlit number inputs are created dynamically based on feature names.
3.Prediction
proba = pipeline.predict_proba(df)[0]
4.Display results
Recommended crop






