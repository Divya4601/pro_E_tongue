import streamlit as st
import pandas as pd
import pickle
import random

# --- Load the pre-trained AI model ---
# The 'rb' means read binary
with open('svm_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

# --- Streamlit App Interface ---

st.title("🌱 AI-Powered Plant Fingerprinting")
st.write("---")

# Section 1: Adulteration Detection
st.header("1. Adulteration Detection")

if st.button("Scan Plant", key='scan_plant_button'):
    # --- Generate simulated sensor data ---
    # This simulates what your hardware would send
    if random.choice([True, False]):
        # Simulate an authentic sample
        new_sample_ph = random.uniform(6.8, 7.2)
        new_sample_gas = random.uniform(180, 200)
        new_sample_conductivity = random.uniform(1180, 1260)
    else:
        # Simulate an adulterated sample
        new_sample_ph = random.uniform(8.4, 8.9)
        new_sample_gas = random.uniform(340, 370)
        new_sample_conductivity = random.uniform(2450, 2700)
    
    # --- Make a prediction using the AI model ---
    # Put the data into a format the model understands
    new_sample = pd.DataFrame({
        'pH': [new_sample_ph],
        'gas_reading': [new_sample_gas],
        'conductivity': [new_sample_conductivity]
    })
    
    prediction = loaded_model.predict(new_sample)

    # --- Display the results ---
    st.subheader("Sensor Readings:")
    st.write(f"**pH:** {new_sample_ph:.2f}")
    st.write(f"**Gas:** {new_sample_gas:.2f} ppm")
    st.write(f"**Conductivity:** {new_sample_conductivity:.2f} µS/cm")

    st.subheader("AI Verdict:")
    if prediction[0] == "authentic":
        st.success("✅ Prediction: Authentic Sample")
    else:
        st.error("⚠️ Prediction: Adulterated Sample Detected")

st.write("---")

# Section 2: Intelligent Plant Information Assistant
st.header("2. Intelligent Plant Information Assistant")
plant_name = st.text_input("Enter a plant name to learn more:")

if plant_name: # Check if the user has entered something
    # This is a hard-coded example for your presentation
    if plant_name.lower() == "neem":
        st.subheader("Neem (Azadirachta indica)")
        st.write("Neem is widely known for its purifying and medicinal properties in Ayurveda. It has been used for centuries to treat various skin conditions, fever, and dental problems.")
        st.write("**Related Diseases:** Skin infections, fever, dental plaque.")
    elif plant_name.lower() == "ashwagandha":
        st.subheader("Ashwagandha (Withania somnifera)")
        st.write("Ashwagandha is an adaptogenic herb used to help the body manage stress. It is often used to boost energy levels, reduce anxiety, and improve overall vitality.")
        st.write("**Related Diseases:** Stress, anxiety, fatigue.")
    elif plant_name.lower() == "tulsi":
        st.subheader("Tulsi (Ocimum tenuiflorum)")
        st.write("Tulsi, or Holy Basil, is a revered herb with strong spiritual and medicinal significance. It is a powerful antioxidant and is used to support respiratory health and a healthy immune system.")
        st.write("**Related Diseases:** Coughs, colds, respiratory issues.")
    else:
        st.warning("Sorry, information for this plant is not available in our database.")