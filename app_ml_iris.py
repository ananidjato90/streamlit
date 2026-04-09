import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Configuration de la page
st.set_page_config(page_title="Iris Predictor", page_icon="🌸")

# Titre et introduction
st.title("Classification des Fleurs d'Iris")
st.write("Cette application prédit la variété d'une iris en fonction de ses dimensions.")

# Chargement des données et entraînement du modèle (mis en cache)
@st.cache_resource
def train_model():
    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    y = iris.target
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model, iris.target_names

model, class_names = train_model()

# Barre latérale pour les paramètres de saisie
st.sidebar.header("Paramètres de la fleur")

def user_input_features():
    sepal_length = st.sidebar.slider('Longueur du sépale (cm)', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Largeur du sépale (cm)', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Longueur du pétale (cm)', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Largeur du pétale (cm)', 0.1, 2.5, 0.2)

    data = {
        'sepal length (cm)': sepal_length,
        'sepal width (cm)': sepal_width,
        'petal length (cm)': petal_length,
        'petal width (cm)': petal_width
    }
    return pd.DataFrame(data, index=[0])

df_user = user_input_features()

# Affichage des paramètres choisis
st.subheader("Dimensions saisies")
st.write(df_user)

# Prédiction
prediction = model.predict(df_user)
prediction_proba = model.predict_proba(df_user)

# Affichage du résultat
st.subheader("Résultat de la Prédiction")
st.success(f"L'espèce prédite est : **{class_names[prediction[0]]}**")

st.subheader("Probabilités par espèce")
proba_df = pd.DataFrame(prediction_proba, columns=class_names)
st.bar_chart(proba_df.T)
