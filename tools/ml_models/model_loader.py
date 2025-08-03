import joblib
import os

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# def load_model(path):
#     full_path = os.path.join(BASE_DIR, path)
#     return joblib.load(full_path)

# import joblib

# # Specify the path to your saved model file
# model_filepath = 'path/to/your/saved_model.pkl'

# # Load the model
# loaded_model = joblib.load(model_filepath)

# The loaded_model can now be used for predictions or other operations
# For example, if it's a scikit-learn model:
# predictions = loaded_model.predict(new_data)
   # or encoder
BRDA_model = '/home/atiar/Videos/phitron/django/Symtom_based_cancer_detection_tool/tools/ml_models/BRDA_model.pkl'
Liver_cancer_model = '/home/atiar/Videos/phitron/django/Symtom_based_cancer_detection_tool/tools/ml_models/Liver_cancer_model.pkl'
lung_cancer_model = '/home/atiar/Videos/phitron/django/Symtom_based_cancer_detection_tool/tools/ml_models/lung_cancer_model.pkl'

breast_model = joblib.load(BRDA_model)
# breast_scaler = load_model("breast_scaler.joblib")

liver_model = joblib.load(Liver_cancer_model)
# liver_scaler = load_model("liver_scaler.joblib")

lung_model = joblib.load(lung_cancer_model)
# lung_scaler = load_model("lung_scaler.joblib")
