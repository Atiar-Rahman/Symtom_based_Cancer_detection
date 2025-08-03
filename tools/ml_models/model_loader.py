import joblib
import os
from django.conf import settings

# Safe model loading function
def safe_load_model(path):
    if os.path.exists(path):
        print(f"Loaded model from: {path}")
        return joblib.load(path)
    else:
        print(f"Model file not found: {path}")
        return None

# Construct paths relative to BASE_DIR
BRDA_model_path = os.path.join(settings.BASE_DIR, 'tools', 'ml_models', 'BRDA_model.pkl')
Liver_cancer_model_path = os.path.join(settings.BASE_DIR, 'tools', 'ml_models', 'Liver_cancer_model.pkl')
lung_cancer_model_path = os.path.join(settings.BASE_DIR, 'tools', 'ml_models', 'lung_cancer_model.pkl')

# Load models safely
breast_model = safe_load_model(BRDA_model_path)
liver_model = safe_load_model(Liver_cancer_model_path)
lung_model = safe_load_model(lung_cancer_model_path)

# Optional: print warnings
if breast_model is None:
    print(" Breast cancer model not loaded. Related predictions may not work.")
if liver_model is None:
    print("Liver cancer model not loaded. Related predictions may not work.")
if lung_model is None:
    print("Lung cancer model not loaded. Related predictions may not work.")
