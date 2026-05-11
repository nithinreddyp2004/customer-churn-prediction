# 📉 Customer Churn Prediction App

A machine learning web application that predicts whether a customer is likely to churn (leave) based on their account and usage data. Built with Python, Scikit-learn, and deployed using Streamlit.

---

## 🚀 Live Demo

> Run locally using the steps below or deploy on [Streamlit Cloud](https://customer-churn-prediction28.streamlit.app/)

---

## 📌 Problem Statement

Customer churn is one of the biggest challenges for businesses. Losing a customer costs 5x more than retaining one. This app helps businesses identify at-risk customers early so they can take action to retain them.

---

## 🔧 Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| Pandas & NumPy | Data manipulation and analysis |
| Matplotlib & Seaborn | Data visualization and EDA |
| Scikit-learn | Machine learning model building |
| Streamlit | Web app deployment |
| Pickle | Model saving and loading |

---

## 📊 Dataset

- **Source:** Telco Customer Churn Dataset
- **Records:** 7,043 customers
- **Features:** 20 (tenure, contract type, monthly charges, etc.)
- **Target:** Churn (Yes/No)

---

## 🧪 ML Pipeline

1. **Exploratory Data Analysis (EDA)** — Visualized churn patterns across features
2. **Data Preprocessing** — Handled missing values, encoded categorical variables
3. **Feature Engineering** — Selected most impactful features
4. **Model Building** — Trained and compared multiple models:
   - Logistic Regression
   - Random Forest Classifier
   - Decision Tree
5. **Model Evaluation** — Accuracy, Precision, Recall, F1-Score, Confusion Matrix
6. **Deployment** — Saved best model as `.pkl` and deployed via Streamlit

---

## 📈 Model Performance

| Model | Accuracy |
|-------|----------|
| Logistic Regression | ~80% |
| Decision Tree | ~79% |
| Random Forest | ~85% |

> ✅ **Best Model: Random Forest** with ~85% accuracy

---

## 🖥️ How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/nithinreddyp2004/customer-churn-prediction.git

# 2. Navigate to the project folder
cd customer-churn-prediction

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Streamlit app
streamlit run app.py
```

---

## 📁 Project Structure

```
customer-churn-prediction/
│
├── churn_project1/          # Jupyter notebook with full EDA and model training
├── app.py                   # Streamlit web application
├── churn_model.pkl          # Saved trained model
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## 🔍 Key Insights from EDA

- Customers with **month-to-month contracts** churn the most
- Higher **monthly charges** correlate with higher churn rates
- Customers with **longer tenure** are less likely to churn
- **Senior citizens** have a higher churn rate

---

## 👨‍💻 Author

**Nithin Reddy**
- GitHub: [@nithinreddyp2004](https://github.com/nithinreddyp2004)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
