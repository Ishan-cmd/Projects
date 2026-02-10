import pickle 
import pandas as pd

# import the ml model
with open('Model/model.pkl', 'rb') as f:
    model = pickle.load(f)

#MLFlow
MODEL_VERSION = '1.0.0'

# Get class labels from model
class_labels = model.classes_.tolist()

def predict_output(user_input: dict):

    df = pd.DataFrame([user_input])

    predicted_class = model.predict(df)[0]

    probabilities = model.predict_proba(df)[0]
    confidence =  max(probabilities)

    return {
        "predicted_category": predicted_class,
        "confidence": round(confidence, 4)
    }
