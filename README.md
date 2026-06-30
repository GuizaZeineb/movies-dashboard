# Movies Dashboard

## Présentation

Movies Dashboard est une application développée avec **Streamlit** permettant d'explorer un catalogue de films à partir du dataset 'movies.csv'.

Le projet a été réalisé dans le cadre d'un challenge Data Science et couvre l'ensemble du processus d'analyse de données :

- chargement des données ;
- préparation et nettoyage ;
- analyse exploratoire (EDA) ;
- visualisations interactives ;
- développement d'une application web.

---

## Fonctionnalités

L'application est organisée en quatre pages :

### Dashboard

Vue d'ensemble du catalogue avec :

- nombre de films ;
- nombre de genres ;
- nombre de langues ;
- période couverte ;
- note moyenne ;
- graphiques de synthèse.

### Exploration interactive

Filtrage des films selon plusieurs critères :

- année de sortie ;
- langue ;
- note minimale.

Les résultats sont affichés dans un tableau interactif.

### Analyse d'un film

Recherche d'un film et affichage de :

- l'affiche ;
- le résumé ;
- les genres ;
- l'année ;
- la langue ;
- la popularité ;
- la note moyenne.

### Analyse avancée

Visualisation interactive de la relation entre :

- popularité ;
- note moyenne ;
- genre principal.

---

## Structure du projet

```text
movies-dashboard/

├── app.py
├── data/
│   └── movies.csv
│
├── notebooks/
│   └── exploratory_data_analysis.ipynb
│
├── pages/
│   ├── 1_Dashboard.py
│   ├── 2_Exploration.py
│   ├── 3_Movie_Search.py
│   └── 4_Advanced_Analysis.py
│
├── src/
│   ├── data_loader.py
│   └── preprocessing.py
│
├── requirements.txt
└── README.md
```

---

## Installation

Créer un environnement virtuel :

```bash
python -m venv .venv
source .venv/bin/activate
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

---

## Lancement de l'application

Depuis la racine du projet :

```bash
python -m streamlit run app.py
```

---

## Dataset

Le projet utilise le fichier `movies.csv` fourni dans le cadre du challenge.

---

## Technologies utilisées

- Python
- Pandas
- Plotly
- Streamlit
- Git / GitHub

---

## Auteur

Projet réalisé dans le cadre d'un challenge Data Science.
