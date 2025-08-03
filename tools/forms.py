from django import forms

class CancerDetectionForm(forms.Form):
    # Common Fields
    age = forms.FloatField(
        label="Age",
        min_value=0,
        widget=forms.NumberInput(attrs={
            "placeholder": "Enter your age",
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
            "placeholder": "Enter Protein1",
            "class": "w-full border border-gray-300 rounded-md px-6 py-2 focus:outline-none focus:ring-2 focus:ring-rose-500"
        })
    )
    protein2 = forms.FloatField(
        label="Protein2",
        widget=forms.NumberInput(attrs={
            "placeholder": "Enter Protein2",
            "class": "w-full border border-gray-300 rounded-md px-6 py-2 focus:outline-none focus:ring-2 focus:ring-rose-500"
        })
    )
    protein3 = forms.FloatField(
        label="Protein3",
        widget=forms.NumberInput(attrs={
            "placeholder": "Enter Protein3",
            "class": "w-full border border-gray-300 rounded-md px-6 py-2 focus:outline-none focus:ring-2 focus:ring-rose-500"
        })
    )
    protein4 = forms.FloatField(
        label="Protein4",
        widget=forms.NumberInput(attrs={
            "placeholder": "Enter Protein4",
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
            "placeholder": "Total Bilirubin",
            "class": "w-full border border-gray-300 rounded-md px-6 py-2 focus:outline-none focus:ring-2 focus:ring-rose-500"
        })
    )
    direct_bilirubin = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={
            "placeholder": "Direct Bilirubin",
            "class": "w-full border border-gray-300 rounded-md px-6 py-2 focus:outline-none focus:ring-2 focus:ring-rose-500"
        })
    )
    alkaline_phosphotase = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={
            "placeholder": "Alkaline Phosphotase",
            "class": "w-full border border-gray-300 rounded-md px-6 py-2 focus:outline-none focus:ring-2 focus:ring-rose-500"
        })
    )
    alamine_aminotransferase = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={
            "placeholder": "Alamine Aminotransferase",
            "class": "w-full border border-gray-300 rounded-md px-6 py-2 focus:outline-none focus:ring-2 focus:ring-rose-500"
        })
    )
    aspartate_aminotransferase = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={
            "placeholder": "Aspartate Aminotransferase",
            "class": "w-full border border-gray-300 rounded-md px-6 py-2 focus:outline-none focus:ring-2 focus:ring-rose-500"
        })
    )
    total_proteins = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={
            "placeholder": "Total Proteins",
            "class": "w-full border border-gray-300 rounded-md px-6 py-2 focus:outline-none focus:ring-2 focus:ring-rose-500"
        })
    )
    albumin = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={
            "placeholder": "Albumin",
            "class": "w-full border border-gray-300 rounded-md px-6 py-2 focus:outline-none focus:ring-2 focus:ring-rose-500"
        })
    )
    albumin_and_globulin_ratio = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={
            "placeholder": "Albumin and Globulin Ratio",
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
            "placeholder": "BMI",
            "class": "w-full border border-gray-300 rounded-md px-6 py-2 focus:outline-none focus:ring-2 focus:ring-rose-500"
        })
    )
    cholesterol_level = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={
            "placeholder": "Cholesterol Level",
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
