# Imports
import streamlit as st
import pandas as pd
import pickle

# Opening intro text
st.write("# Will It Be Adopted?")

st.write("### Describe Your Animal:")

# Creating columns to make the intake details look nicer
col1, col2, col3 = st.columns(3)

# First column: animal type choice
with col1:
    animal_type = st.radio(
        label='Is the animal a cat or dog?', 
        options=['Cat', 'Dog', 'Other'])

# Second column: some animal details
with col2:
    color_black = st.checkbox(
        label='Is the animal black?')

    female = st.checkbox(
        label='Is the animal female?')

    young = st.checkbox(
        label='Is the animal less than 1 year old?')

# Third column: intake/medical details
with col3:
    fixed = st.checkbox(
        label='Is the animal fixed?')  

    intake_condition = st.checkbox(
        label="Is the animal not in a normal condition?")

# Cleaning up animal type details before putting into the df
if animal_type == 'Cat':
    is_cat = True
    is_dog = False
elif animal_type == 'Dog':
    is_cat = False
    is_dog = True
else:
    is_cat = False
    is_dog = False

# Creating the dataframe to run predictions on
row = [color_black, fixed, is_cat, is_dog, intake_condition, female, young]
columns = [
    'Color_black', 'Fixed', 'Type_Cat', 'Type_Dog', 
    'Intake Condition_Not Normal', 'Female', 'Young']

new_animal = pd.DataFrame(dict(zip(columns, row)), index=[0])

# Now - predicting!
if st.button(label="Click to Predict"):

    # Load the model
    loaded_model = pickle.load(open('rf_model.sav', 'rb'))
    # Make predictions (and get out pred probabilities)
    pred = loaded_model.predict(new_animal)[0]
    proba = loaded_model.predict_proba(new_animal)[:,1][0]
    
    # Sharing the predictions
    if pred == 0:
        st.write("### The animal is not predicted to be adopted")
        st.write(f"Predicted probability of adoption: {proba*100:.2f} %")

    elif pred == 1:
        st.write("### The animal is predicted to be adopted!")
        st.write(f"Predicted probability of adoption: {proba*100:.2f} %")

