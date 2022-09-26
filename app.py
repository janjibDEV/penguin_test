import pickle
import streamlit as st


st.write('''
# Penguin Classification
## Input penguin details
''')

bill_length = st.slider("Enter bill length (mm)",min_value=30,max_value=60,value=43)
bill_depth = st.slider("Enter bill depth (mm)",min_value=13,max_value=21,value=17)
flipper_length = st.slider("Enter flipper length (mm)",min_value=172,max_value=231,value=200)
body_mass = st.slider("Enter body mass (g)",min_value=2700,max_value=6300,value=4207)

sex_option = st.selectbox(
    "Choose penguin's sex",
    ('Male', 'Female'))

st.write('You selected:', sex_option)

island_option = st.selectbox(
    "Choose penguin's origin",
    ('Torgersen', 'Biscoe', 'Dream'))

st.write('You selected:', island_option)
def sex_binary(gender):
    if gender == "Male":
        return 1
    else:
        return 0

def OH_island(i):
    # Torgersen 2
    # Dream 1
    # Biscoe 0
    OH_encoding = {"Torgersen":2,"Dream":1,"Biscoe":0}
    l = [0,0,0]
    l[OH_encoding[i]] = 1.0
    return l

load_clf = pickle.load(open("penguins.pkl","rb"))
pred_species = None

species_mapper = {"Adelie" : 1, "Gentoo":2, "Chinstrap":3}

guess = [bill_length,bill_depth,flipper_length,body_mass, sex_binary(sex_option)] + OH_island(island_option)
preds = load_clf.predict([guess])[0]
preds_proba = load_clf.predict_proba([guess])
for i in species_mapper:
    if species_mapper[i] == preds:
        pred_species = i
st.write('''
### Predicted penguin's species:
''')
st.write(pred_species)


