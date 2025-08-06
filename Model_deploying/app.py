import streamlit as st
import joblib
import pandas as pd

model = joblib.load("Model_deploying/model.pkl")

st.title("Machine Failure Prediction App")

age = st.slider("Customer Age", 0, 100, 30)
days = st.number_input("Days_Since_Purchase")
Gender = st.selectbox("Customer Gender", ['Male', 'Female', 'Other'])

products = [
    "Canon EOS", "iPhone", "Canon DSLR Camera", "GoPro Hero", "Microsoft Office",
    "Sony Xperia", "Apple AirPods", "Sony 4K HDR TV", "LG OLED", "Nest Thermostat",
    "Amazon Echo", "Garmin Forerunner", "Roomba Robot Vacuum", "Google Pixel", "Nikon D",
    "Philips Hue Lights", "LG Washing Machine", "LG Smart TV", "Bose QuietComfort", "Amazon Kindle",
    "PlayStation", "Sony PlayStation", "Bose SoundLink Speaker", "Autodesk AutoCAD", "Fitbit Versa Smartwatch",
    "Google Nest", "Adobe Photoshop", "Fitbit Charge", "Samsung Soundbar", "HP Pavilion",
    "Asus ROG", "Microsoft Surface", "Xbox", "Dyson Vacuum Cleaner", "GoPro Action Camera",
    "Microsoft Xbox Controller", "Samsung Galaxy", "Nintendo Switch", "MacBook Pro",
    "Nintendo Switch Pro Controller", "Dell XPS", "Lenovo ThinkPad"
]

selected_product = st.selectbox("Product Purchased", sorted(products))


ticket_subjects = [
    "Network problem", "Software bug", "Product compatibility", "Product recommendation", "Product setup",
    "Hardware issue", "Delivery problem", "Refund request", "Battery life", "Account access",
    "Installation support", "Peripheral compatibility", "Payment issue", "Display issue", "Cancellation request", "Data loss"
]

selected_subject = st.selectbox("Ticket Subject:", sorted(ticket_subjects))


satisfaction_levels = ["Low", "Medium", "High"]

selected_satisfaction = st.selectbox("Satisfaction_Level", satisfaction_levels)

input_dict = {
    'Customer Age': [age],
    'Days_Since_Purchase': [days],
    'Customer Gender': [Gender],
    'Product Purchased': [selected_product],
    'Ticket Subject': [selected_subject],
    'Satisfaction_Level': [selected_satisfaction]
}

input_df = pd.DataFrame(input_dict)

if st.button("Predict Satisfaction Rating"):
    prediction = model.predict(input_df)[0]
    rounded = round(prediction, 2)

    # Display Result
    if rounded >= 4:
        st.success(f"Predicted Satisfaction Rating: {rounded} Customer is Happy")
    elif rounded >= 2.5:
        st.info(f"Predicted Satisfaction Rating: {rounded} Customer is Neutral")
    else:
        st.error(f"Predicted Satisfaction Rating: {rounded} Customer is Not Satisfied")


# how to run
# frist activate the enviroment venv\Scripts\activate
# then run
# Streamlit run 'Model_deploying/app.py'