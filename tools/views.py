from django.shortcuts import render
from .forms import CancerDetectionForm
import pandas as pd
import numpy as np
from tools.ml_models.model_loader import breast_model,  lung_model,liver_model



def Home(request):
    return render(request,'Home.html')
def Knowledge(request):
    return render(request,'knowledge.html')
def Contact(request):
    return render(request,'contact.html')


def Predict_Lung_Cancer(model,user_data):
    user_df = pd.DataFrame([user_data])
    # print(user_df)
    prediction = model.predict(user_df)
    proba = model.predict_proba(user_df)

    # print("\nPrediction Result:")
    # print("Prediction:", "Cirrhosis (1 - Cancer)" if prediction[0] == 1 else "No Cirrhosis (0 - No Cancer)")
    # print(f"Probability: {proba[0][1]*100:.2f}% chance of cirrhosis")

    return {
        'cancer_probability': round(proba[0][1] * 100, 2),
        'final_diagnosis': 'Cirrhosis (Cancer)' if prediction[0] == 1 else 'No Cirrhosis (No Cancer)',
        'prediction_class': int(prediction[0])
    }
def Predict_liver_cancer(model, features):
    # print("Input Features Dictionary:")
    # print(features)

    user_df = pd.DataFrame([features])
    # print("\nConverted DataFrame:")
    # print(user_df)

    # Prediction
    prediction = model.predict(user_df)
    probability = model.predict_proba(user_df)

    # print("\nPrediction Result:")
    # print(f"Cancer Probability: {probability[0][1] * 100:.2f}%")
    # print(f"Final Diagnosis: {'Alive' if prediction[0] == 1 else 'Dead'}")

    return{
        'cancer_probability': round(probability[0][1] * 100, 2),
        'final_diagnosis': 'Cancer Detected (High Risk)' if prediction[0] == 1 else 'No Cancer Detected (Low Risk)',
        'prediction_class': int(prediction[0])
    }


def predict_breast_cancer(model, features):
    # print("Input Features Dictionary:")
    # print(features)

    user_df = pd.DataFrame([features])
    # print("\nConverted DataFrame:")
    # print(user_df)

    # Prediction
    prediction = model.predict(user_df)
    probability = model.predict_proba(user_df)

    # print("\nPrediction Result:")
    # print(f"Cancer Probability: {probability[0][1] * 100:.2f}%")
    # print(f"Final Diagnosis: {'Alive' if prediction[0] == 1 else 'Dead'}")

    return{
        'cancer_probability': round(probability[0][1] * 100, 2),
        'final_diagnosis': 'Cancer Detected (High Risk)' if prediction[0] == 1 else 'No Cancer Detected (Low Risk)',
        'prediction_class': int(prediction[0])
    }
def Detection(request):
    prediction = {}

    if request.method == 'POST':
        form = CancerDetectionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            
            # Extract features per cancer type
            breast_features = {
                'Age': data['age'],
                'Gender': data['gender'].upper(),
                'Protein1': float(data['protein1']),
                'Protein2': float(data['protein2']),
                'Protein3': float(data['protein3']),
                'Protein4': float(data['protein4']),
                'Tumour_Stage': data['tumour_stage'].strip().upper(),
                'Histology': data['histology'].strip(),
                'ER status': data['er_status'],
                'PR status': data['pr_status'],
                'HER2 status': data['her2_status'],
            }

            breast_cancer_result= predict_breast_cancer(breast_model,breast_features)

            liver_features = {
                'Age': data.get('age', 0),
                'Gender': 1 if data.get('gender', '').upper() == 'MALE' else 0,
                'Total_Bilirubin': data.get('total_bilirubin', 0),
                'Direct_Bilirubin': data.get('direct_bilirubin', 0),
                'Alkaline_Phosphotase': data.get('alkaline_phosphotase', 0),
                'Alamine_Aminotransferase': data.get('alamine_aminotransferase', 0),
                'Aspartate_Aminotransferase': data.get('aspartate_aminotransferase', 0),
                'Total_Protiens': data.get('total_protiens', 0),
                'Albumin': data.get('albumin', 0),
                'Albumin_and_Globulin_Ratio': data.get('albumin_and_globulin_ratio', 0),
            }

            liver_cancer_result = Predict_liver_cancer(liver_model,liver_features)

            # lung complete
            lung_features = {
                'age': data.get('age', 0),
                'gender':data.get('gender', '').title(),
                'family_history': data.get('family_history', 'No'),
                'smoking_status': data.get('smoking_status', 'Never Smoked'),
                'bmi': float(data.get('bmi', 0)),
                'cholesterol_level': int(data.get('cholesterol_level', 0)),
                'hypertension': int(data.get('hypertension', 0)),
                'asthma': int(data.get('asthma', 0)),
            }
            # print("value:", lung_features['smoking_status'])
            # print("gender type:", type(lung_features['smoking_status']))
            # Example use:
            lung_cancer_result = Predict_Lung_Cancer(lung_model,lung_features)
            

            # print("breast")
            # print(breast_cancer_result)
            # print("liver")
            # print(liver_cancer_result)
            # print("breast")
            # print(lung_cancer_result)

            prediction['breast_cancer_result']=breast_cancer_result
            prediction['liver_cancer_result']=liver_cancer_result
            prediction['lung_cancer_result']=lung_cancer_result
            
    else:
        form = CancerDetectionForm()

    print(prediction)
    return render(request, 'detection.html', {'form': form, 'prediction': prediction})
