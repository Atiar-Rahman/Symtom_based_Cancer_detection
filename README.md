
# 🩺 Symptom-Based Multi-Cancer Risk Detection Tool  

This project is a **web-based application** that helps users assess their risk of developing **Breast Cancer, Lung Cancer, and Liver Cancer** based on self-reported symptoms. The tool is designed to raise awareness, provide preliminary risk insights, and encourage users to seek professional medical consultation.  

 **Disclaimer**: This tool is **not a medical diagnosis system**. It is only for educational and awareness purposes. Always consult a qualified doctor for medical advice.  

##  Live Demo

You can explore the live web app here: **[Symptom-Based Cancer Detection Tool](https://symtom-based-cancer-detection.onrender.com/)**

---

##  Features  

-  **Symptom-Based Detection**: Users can enter their symptoms to get an estimated cancer risk score.  
-  **Cancers Covered**:  
  - Breast Cancer  
  - Lung Cancer  
  - Liver Cancer  
-  **Risk Prediction**: Provides a simple low/medium/high risk assessment.  
-  **Responsive Web Interface** built with **HTML, Tailwind CSS, and JavaScript**.  
-  **Blog Section**: Awareness content for breast cancer and other cancers.  
-  **FAQs Section**: Educates users about common cancer-related questions.  
-  **Contact & Newsletter**: Allows users to get in touch and subscribe for updates.  

---

## 🛠️ Tech Stack  

- **Frontend**: HTML, Tailwind CSS, JavaScript  
- **Backend (Optional)**: Python (Flask/Django) or Node.js for risk prediction models  
- **ML Models**: Logistic Regression / LightGBM / Random Forest (trained on symptom datasets)  
- **Deployment**: Vercel / Firebase / Netlify  

---
```
##  Project Structure  

symptom-cancer-detection/
│── index.html             # Homepage (UI)
│── blog.html              # Breast cancer awareness blog
│── faq.html               # FAQ section
│── contact.html           # Contact form
│── /static
│    ├── css/              # Tailwind CSS files
│    ├── js/               # Custom JavaScript for prediction logic
│    └── images/           # Project images & icons
│── /models
│    ├── breast_cancer.pkl # Trained ML model (Breast Cancer)
│    ├── lung_cancer.pkl   # Trained ML model (Lung Cancer)
│    └── liver_cancer.pkl  # Trained ML model (Liver Cancer)
│── app.py / server.js     # Backend (Flask/Node.js) to serve ML models
│── README.md              # Project documentation
```

---

##  How It Works

1. User selects symptoms from a checklist or form.
2. The system processes symptoms using trained ML models.
3. A risk score is calculated (Low / Medium / High).
4. Results are shown with **awareness tips** and a **doctor consultation recommendation**.

---

##  Machine Learning Approach

* **Data Preprocessing**: Cleaning and encoding symptom datasets.
* **Model Training**: Logistic Regression, Random Forest, LightGBM were tested.
* **Evaluation Metrics**: Accuracy, Precision, Recall, F1-score, ROC-AUC.
* **Best Model**: LightGBM (highest accuracy & efficiency).

---

## ⚡ Installation & Setup

### 1 Clone Repository

```bash
git clone https://github.com/your-username/symptom-cancer-detection.git
cd symptom-cancer-detection
```

### 2 Install Dependencies

If using **Django (Python)**:

```bash
pip install -r requirements.txt
```

### 3. venv create
```bash
python3 -m venv env_name
```
active this venv 
### 4. Run the project
```bash
python3 manage.py runserver
```
---

## 🧑‍🤝‍🧑 Contributors

* 👨‍💻 \[Md. Atiar Rahman and others] – Developer & Researcher
* 🩺 Medical Advisors (Optional if collaborated)

---

## 📜 License

This project is licensed under the **MIT License** – free to use and modify with attribution.



