# Iris Predictor - Streamlit App

## Description

Cette application **Streamlit** permet de prédire la classe d'une fleur
d'iris parmi les trois espèces suivantes :

-   Setosa
-   Versicolor
-   Virginica

Le modèle utilisé est un **Random Forest Classifier** entraîné sur le
dataset classique **Iris** de `scikit-learn`.

## Fonctionnalités

-   Interface interactive avec **Streamlit**
-   Saisie utilisateur via sliders :
    -   Longueur du sépale
    -   Largeur du sépale
    -   Longueur du pétale
    -   Largeur du pétale
-   Prédiction en temps réel
-   Affichage des probabilités par classe
-   Modèle entraîné automatiquement (cache optimisé)

## Modèle Machine Learning

-   Algorithme : `RandomForestClassifier`
-   Nombre d'arbres : 100
-   Dataset : Iris (`sklearn.datasets`)
-   Features :
    -   sepal length (cm)
    -   sepal width (cm)
    -   petal length (cm)
    -   petal width (cm)

## Structure du projet

    .
    ├── app.py              # Application Streamlit
    ├── README.md           # Documentation
    └── requirements.txt    # Dépendances

## Installation

### 1. Cloner le repository

``` bash
git clone https://github.com/ananidjato90/streamlit.git
cd streamlit
```

### 2. Créer un environnement virtuel

``` bash
conda create -n streamlit python=3.13
conda activate streamlit
```

### 3. Installer les dépendances

``` bash
pip install -r requirements.txt
```


## Lancer l'application

``` bash
streamlit run app_ml_iris.py
```

Puis ouvrir dans le navigateur :

    http://localhost:8501


## Utilisation

1.  Ajuster les paramètres dans la barre latérale
2.  Visualiser les dimensions sélectionnées
3.  Consulter :
    -   L'espèce prédite
    -   Les probabilités associées
