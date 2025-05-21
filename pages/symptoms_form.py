import streamlit as st
import joblib
import numpy as np
import pandas as pd
import os

# Load the trained model
model = joblib.load("leukemia_risk_model")

st.set_page_config(page_title="LeukoVision - Input", layout="centered")

# Hide sidebar, hamburger menu, and footer
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
        [data-testid="collapsedControl"] {
            display: none;
        }
        #MainMenu, footer {
            visibility: hidden;
        }
    </style>
""", unsafe_allow_html=True)

def save_user_data(input_data, prediction):
    filename = "user_leukemia_data.csv"
    columns = [
        "age", "gender", "fatigue", "weight_loss", "frequent_infections", "easy_bruising",
        "pale_skin", "shortness_of_breath", "bone_joint_pain", "enlarged_lymph_nodes",
        "fever", "night_sweats", "infection_history", "family_history_leukemia",
        "wbc_count", "rbc_count", "platelets_count", "hemoglobin", "predicted_risk"
    ]
    new_row = input_data + [prediction]
    
    if os.path.exists(filename):
        df = pd.read_csv(filename)
        df.loc[len(df)] = new_row
    else:
        df = pd.DataFrame([new_row], columns=columns)

    df.to_csv(filename, index=False)

st.title("📝 Patient Symptom Input Form")

st.markdown("Please fill out the form below to check Leukemia risk.")

with st.form("patient_form"):
    age = st.number_input("Age", min_value=1, max_value=120, step=1)
    gender = st.selectbox("Gender", ["Male", "Female"])
    gender_encoded = 1 if gender == "Male" else 0

    # fatigue = st.selectbox("Fatigue")
    # fatigue = st.selectbox("Fatigue", ["Yes", "No"]) == "Yes"
    fatigue = st.selectbox("Fatigue", ["Yes", "No"],
                           help="Fatigue refers to a constant feeling of tiredness or weakness that doesn’t improve with rest.") == "Yes"
    weight_loss = st.selectbox("Weight Loss", ["Yes", "No"],
                               help="Unintentional weight loss can be a symptom of underlying conditions like leukemia.") == "Yes"
    frequent_infections = st.selectbox("Frequent Infections", ["Yes", "No"],
                                       help="Recurring infections may indicate a weakened immune system, often seen in leukemia.") == "Yes"
    easy_bruising = st.selectbox("Easy Bruising", ["Yes", "No"],
                                 help="Unusual or frequent bruising may happen when platelets are low, which affects blood clotting in leukemia.") == "Yes"
    pale_skin = st.selectbox("Pale Skin", ["Yes", "No"],
                             help="Pale skin means lighter than normal skin tone, often caused by anemia or low red blood cells due to leukemia.") == "Yes"
    shortness_of_breath = st.selectbox("Shortness of Breath", ["Yes", "No"],
                                       help="Low hemoglobin levels can cause fatigue and difficulty breathing.") == "Yes"
    bone_joint_pain = st.selectbox("Bone or Joint Pain", ["Yes", "No"],
                                   help="Leukemia can cause pain in the bones or joints due to overcrowded marrow.") == "Yes"
    enlarged_lymph_nodes = st.selectbox("Enlarged Lymph Nodes", ["Yes", "No"],
                                        help="Lymph nodes may swell due to abnormal white blood cell activity, which is common in leukemia.") == "Yes"
    fever = st.selectbox("Fever", ["Yes", "No"],
                         help="Frequent fevers may indicate infections or abnormal immune responses.") == "Yes"
    night_sweats = st.selectbox("Night Sweats", ["Yes", "No"],
                                help="Excessive sweating during sleep can be associated with cancers like leukemia or infections.") == "Yes"
    infection_history = st.selectbox("Past Infection History", ["Yes", "No"],
                                     help="A history of recurring infections may suggest a suppressed immune system.") == "Yes"
    family_history_leukemia = st.selectbox("Family History of Leukemia", ["Yes", "No"],
                                           help="Genetic predisposition can increase leukemia risk if a family member has had it.") == "Yes"

    wbc_count = st.number_input("White Blood Cell (WBC) Count", min_value=0.0)
    rbc_count = st.number_input("Red Blood Cell (RBC) Count", min_value=0.0)
    platelets_count = st.number_input("Platelets Count", min_value=0.0,
                                      help="Platelets help your blood clot. Low levels can lead to bleeding and bruising.")
    hemoglobin = st.number_input("Hemoglobin", min_value=0.0,
                                 help="Hemoglobin is a protein in red blood cells that carries oxygen. Low levels may indicate anemia or bone marrow issues.")

    submitted = st.form_submit_button("Predict")

if submitted:
    input_data = [[
        age, gender_encoded, int(fatigue), int(weight_loss), int(frequent_infections),
        int(easy_bruising), int(pale_skin), int(shortness_of_breath), int(bone_joint_pain),
        int(enlarged_lymph_nodes), int(fever), int(night_sweats), int(infection_history),
        int(family_history_leukemia), wbc_count, rbc_count, platelets_count, hemoglobin
    ]]

    prediction = int(model.predict(input_data)[0])

    # Map prediction to label
    label_map = {
        0: "Low",
        1: "Moderate",
        2: "High",
        3: "Confirmed"
    }

    st.success(f"Predicted Leukemia Risk: {label_map.get(prediction)}")

    # Get risk label
    risk_label = label_map.get(prediction, "Unknown")
    st.subheader(f"🧪 Predicted Leukemia Risk: {risk_label}")

    # Provide suggestions based on risk
    if prediction == 0:
        st.success("Your risk level is **Low**. Maintain a healthy lifestyle and routine checkups.")
    elif prediction == 1:
        st.info("Your risk level is **Moderate**. We recommend scheduling a visit with a general physician and keeping an eye on symptoms.")
    elif prediction == 2:
        st.warning("Your risk level is **High**. Please consult a hematologist or oncologist as soon as possible for further medical evaluation.")
    elif prediction == 3:
        st.error("Leukemia risk is **Confirmed**. This is a critical situation — we strongly advise seeing a specialist urgently for immediate medical tests and care.")
    else:
        st.error("An unexpected issue occurred. Please try again or consult a medical expert.")

    # Save user data
    save_user_data(input_data[0], risk_label)

    

