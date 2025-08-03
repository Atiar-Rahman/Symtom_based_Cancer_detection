from django import forms

class CancerDetectionForm(forms.Form):
    # Common Fields
    age = forms.FloatField(
        label="Age",
        min_value=0,
        max_value=120,
        widget=forms.NumberInput(attrs={
            "placeholder": "Enter your age: e.g., 45",
            "class": "w-full border border-gray-300 rounded-md px-6 py-2 focus:outline-none focus:ring-2 focus:ring-rose-500"
        })
    )

    gender = forms.ChoiceField(
        choices=[('MALE', 'Male'), ('FEMALE', 'Female')],
        widget=forms.Select(attrs={
            "class": "w-full border border-gray-300 rounded-md px-6 py-2 bg-white focus:outline-none focus:ring-2 focus:ring-rose-500"
        })
    )

    # Breast cancer features
    protein1 = forms.FloatField(
        label="Protein1",
        widget=forms.NumberInput(attrs={
            "placeholder": "Enter Protein1: e.g., 15.4 (ng/mL)",
            "class": "w-full border border-gray-300 rounded-md px-6 py-2 focus:outline-none focus:ring-2 focus:ring-rose-500"
        })
    )
    protein2 = forms.FloatField(
        label="Protein2",
        widget=forms.NumberInput(attrs={
            "placeholder": "Enter Protein2: e.g., 8.2 (ng/mL)",
            "class": "w-full border border-gray-300 rounded-md px-6 py-2 focus:outline-none focus:ring-2 focus:ring-rose-500"
        })
    )
    protein3 = forms.FloatField(
        label="Protein3",
        widget=forms.NumberInput(attrs={
            "placeholder": "Enter Protein3: e.g., 21.0 (ng/mL)",
            "class": "w-full border border-gray-300 rounded-md px-6 py-2 focus:outline-none focus:ring-2 focus:ring-rose-500"
        })
    )
    protein4 = forms.FloatField(
        label="Protein4",
        widget=forms.NumberInput(attrs={
            "placeholder": "Enter Protein4: e.g., 5.6 (ng/mL)",
            "class": "w-full border border-gray-300 rounded-md px-6 py-2 focus:outline-none focus:ring-2 focus:ring-rose-500"
        })
    )

    tumour_stage = forms.ChoiceField(
        choices=[('I', 'Stage I'), ('II', 'Stage II'), ('III', 'Stage III')],
        widget=forms.Select(attrs={
            "class": "w-full border border-gray-300 rounded-md px-6 py-2 bg-white focus:outline-none focus:ring-2 focus:ring-rose-500"
        })
    )

    histology = forms.ChoiceField(
        choices=[
            ('Infiltrating Ductal Carcinoma', 'Infiltrating Ductal Carcinoma'),
            ('Mucinous Carcinoma', 'Mucinous Carcinoma'),
            ('Infiltrating Lobular Carcinoma','Infiltrating Lobular Carcinoma')
        ],
        widget=forms.Select(attrs={
            "class": "w-full border border-gray-300 rounded-md px-6 py-2 bg-white focus:outline-none focus:ring-2 focus:ring-rose-500"
        })
    )

    er_status = forms.ChoiceField(
        label="ER Status",
        choices=[('Positive', 'Positive'), ('Negative', 'Negative')],
        widget=forms.Select(attrs={
            "class": "w-full border border-gray-300 rounded-md px-6 py-2 bg-white focus:outline-none focus:ring-2 focus:ring-rose-500"
        })
    )
    pr_status = forms.ChoiceField(
        label="PR Status",
        choices=[('Positive', 'Positive'), ('Negative', 'Negative')],
        widget=forms.Select(attrs={
            "class": "w-full border border-gray-300 rounded-md px-6 py-2 bg-white focus:outline-none focus:ring-2 focus:ring-rose-500"
        })
    )
    her2_status = forms.ChoiceField(
        label="HER2 Status",
        choices=[('Positive', 'Positive'), ('Negative', 'Negative')],
        widget=forms.Select(attrs={
            "class": "w-full border border-gray-300 rounded-md px-6 py-2 bg-white focus:outline-none focus:ring-2 focus:ring-rose-500"
        })
    )

    # Liver cancer features
    total_bilirubin = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={
            "placeholder": "Total Bilirubin: e.g., 1.2 (mg/dL)",
            "class": "w-full border border-gray-300 rounded-md px-6 py-2 focus:outline-none focus:ring-2 focus:ring-rose-500"
        })
    )
    direct_bilirubin = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={
            "placeholder": "Direct Bilirubin: e.g., 0.3 (mg/dL)",
            "class": "w-full border border-gray-300 rounded-md px-6 py-2 focus:outline-none focus:ring-2 focus:ring-rose-500"
        })
    )
    alkaline_phosphotase = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={
            "placeholder": "Alkaline Phosphotase: e.g., 100-300 (U/L)",
            "class": "w-full border border-gray-300 rounded-md px-6 py-2 focus:outline-none focus:ring-2 focus:ring-rose-500"
        })
    )
    alamine_aminotransferase = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={
            "placeholder": "Alamine Aminotransferase: e.g., 7-56 (U/L)",
            "class": "w-full border border-gray-300 rounded-md px-6 py-2 focus:outline-none focus:ring-2 focus:ring-rose-500"
        })
    )
    aspartate_aminotransferase = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={
            "placeholder": "Aspartate Aminotransferase: e.g., 10-40 (U/L)",
            "class": "w-full border border-gray-300 rounded-md px-6 py-2 focus:outline-none focus:ring-2 focus:ring-rose-500"
        })
    )
    total_proteins = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={
            "placeholder": "Total Proteins: e.g., 6.0-8.3 (g/dL)",
            "class": "w-full border border-gray-300 rounded-md px-6 py-2 focus:outline-none focus:ring-2 focus:ring-rose-500"
        })
    )
    albumin = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={
            "placeholder": "Albumin: e.g., 3.4-5.4 (g/dL)",
            "class": "w-full border border-gray-300 rounded-md px-6 py-2 focus:outline-none focus:ring-2 focus:ring-rose-500"
        })
    )
    albumin_and_globulin_ratio = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={
            "placeholder": "Albumin and Globulin Ratio: e.g., 1.1-2.5",
            "class": "w-full border border-gray-300 rounded-md px-6 py-2 focus:outline-none focus:ring-2 focus:ring-rose-500"
        })
    )

    # Lung cancer features
    smoking = forms.ChoiceField(
        choices=[
            ('Passive Smoker', 'Passive Smoker'),
            ('Former Smoker', 'Former Smoker'),
            ('Never Smoked', 'Never Smoked'),
            ('Current Smoker', 'Current Smoker'),
        ],
        required=False,
        widget=forms.Select(attrs={
            "class": "w-full border border-gray-300 rounded-md px-6 py-2 bg-white focus:outline-none focus:ring-2 focus:ring-rose-500"
        })
    )
    family_history = forms.ChoiceField(
        choices=[('Yes', 'Yes'), ('No', 'No')],
        required=False,
        widget=forms.Select(attrs={
            "class": "w-full border border-gray-300 rounded-md px-6 py-2 bg-white focus:outline-none focus:ring-2 focus:ring-rose-500"
        })
    )
    bmi = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={
            "placeholder": "BMI: e.g., 22.5 (kg/m²)",
            "class": "w-full border border-gray-300 rounded-md px-6 py-2 focus:outline-none focus:ring-2 focus:ring-rose-500"
        })
    )
    cholesterol_level = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={
            "placeholder": "Cholesterol Level:  e.g., 180 (mg/dL)",
            "class": "w-full border border-gray-300 rounded-md px-6 py-2 focus:outline-none focus:ring-2 focus:ring-rose-500"
        })
    )
    hypertension = forms.ChoiceField(
        choices=[('1', 'Yes'), ('0', 'No')],
        required=False,
        label="Hypertension",
        widget=forms.Select(attrs={
            "class": "w-full border border-gray-300 rounded-md px-6 py-2 bg-white focus:outline-none focus:ring-2 focus:ring-rose-500"
        })
    )
    asthma = forms.ChoiceField(
        choices=[('1', 'Yes'), ('0', 'No')],
        required=False,
        label="Asthma",
        widget=forms.Select(attrs={
            "class": "w-full border border-gray-300 rounded-md px-6 py-2 bg-white focus:outline-none focus:ring-2 focus:ring-rose-500"
        })
    )
