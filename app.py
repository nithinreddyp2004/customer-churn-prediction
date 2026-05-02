import streamlit as st
import joblib
import pandas as pd
import os
os.system("pip install joblib")

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="ChurnGuard | Customer Analytics",
    page_icon="📊",
    layout="wide"
)

# -------------------------------
# Model Loading (Updated Path)
# -------------------------------
@st.cache_resource
def load_model():
    # Based on your folder structure in image_974839.png, 
    # the model is inside 'churn_project1'
    model_path = "churn_project1/churn_model.pkl"
    
    if not os.path.exists(model_path):
        st.error(f"File not found at {model_path}. Please check your folder structure.")
        st.stop()
        
    return joblib.load(model_path)

model = load_model()

# -------------------------------
# Header Section
# -------------------------------
st.title("📊 Customer Churn Prediction Portal")
st.markdown("""
Predict the likelihood of customer churn using demographic and billing data. 
Fill in the details in the sidebar and click **Analyze Customer** to see results.
""")
st.divider()

# -------------------------------
# Sidebar Inputs
# -------------------------------
with st.sidebar:
    st.header("🛠️ Customer Input")
    st.info("Provide the latest customer data.")
    
    with st.expander("Demographics", expanded=True):
        gender = st.radio("Gender", ["Male", "Female"], horizontal=True)
        partner = st.selectbox("Partner?", ["No", "Yes"])
        dependents = st.selectbox("Dependents?", ["No", "Yes"])
    
    with st.expander("Billing & Usage", expanded=True):
        tenure = st.slider("Tenure (Months)", 0, 72, 12)
        monthly = st.number_input("Monthly Charges ($)", min_value=0.0, value=65.0)
        total = st.number_input("Total Charges ($)", min_value=0.0, value=700.0)

# -------------------------------
# Data Processing
# -------------------------------
input_data = {
    'Tenure Months': tenure,
    'Monthly Charges': monthly,
    'Total Charges': total,
    'Gender_Male': 1 if gender == "Male" else 0,
    'Partner_Yes': 1 if partner == "Yes" else 0,
    'Dependents_Yes': 1 if dependents == "Yes" else 0
}

input_df = pd.DataFrame([input_data])

# Ensure columns match model training features
for col in model.feature_names_in_:
    if col not in input_df.columns:
        input_df[col] = 0
input_df = input_df[model.feature_names_in_]

# -------------------------------
# Main Display & Prediction
# -------------------------------
if st.button("🚀 Analyze Customer Risk", type="primary"):
    
    # Run Prediction
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    # Result Layout
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("Prediction Result")
        if prediction == 1:
            st.error("### 🚨 High Risk of Churn")
            st.write("This customer is likely to terminate their service.")
        else:
            st.success("### ✅ Low Risk / Loyal")
            st.write("This customer is likely to remain with the company.")

    with col2:
        st.subheader("Probability Score")
        st.metric(label="Churn Chance", value=f"{probability:.1%}")
        st.progress(probability)

    st.divider()
    
    # Recommendations
    st.subheader("💡 Strategic Recommendations")
    if prediction == 1:
        st.markdown("""
        * **Offer Incentives:** Target with loyalty discounts or contract renewals.
        * **Feedback Loop:** Initiate a proactive customer service call.
        * **Bundling:** Suggest adding a 'Partner' or 'Dependent' plan to increase stickiness.
        """)
    else:
        st.markdown("""
        * **Upsell Opportunity:** Consider promoting higher-tier monthly plans.
        * **Referral Program:** Encourage this loyal customer to refer friends/family.
        """)

# -------------------------------
# Footer
# -------------------------------
st.caption("Developed by Nithin Reddy P | Data Science Intern")