import streamlit as st
import pickle
import numpy as np
import sklearn 
# Load the saved model
with open("model1.pkl", "rb") as file:
    model = pickle.load(file)

# Streamlit UI
st.title("Movie Earnings Prediction")
st.write("Enter movie details to predict earnings.")

# Input fields
running_time = st.number_input("Running time (in minutes)", min_value=0, max_value=300, value=0)
budget = st.number_input("Budget $ in million ", min_value=0, max_value=5000000000000000, value=1)
box_office = st.number_input("Box Office $ in million", min_value=0, max_value=5000000000000000, value=1)
actors_bo_percentage = st.number_input("Actors Box Office %", min_value=0.0, max_value=100.0, value=1.00)
director_bo_percentage = st.number_input("Director Box Office %", min_value=0.0, max_value=100.0, value=1.00)
nominations = st.number_input("Oscar and Golden Globes nominations", min_value=0, max_value=50, value=1)
awards = st.number_input("Oscar and Golden Globes awards", min_value=0, max_value=20, value=1)
release_year = st.number_input("Release year", min_value=1900, max_value=2030, value=1901)
imdb_score = st.number_input("IMDb score", min_value=0.0, max_value=10.0, value=1.00)

# Predict button
if st.button("Predict Earnings"):
    input_data = np.array([[running_time, budget, box_office, actors_bo_percentage, 
                            director_bo_percentage, nominations, awards, release_year, imdb_score]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Earnings: ${prediction[0]:,.2f} ")