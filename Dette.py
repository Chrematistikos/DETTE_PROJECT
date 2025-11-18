# Dette_Streamlit.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# INTERFACE UTILISATEUR
# =============================================================================
st.title("Simulation de la dette publique")

# Paramètres ajustables
r = st.sidebar.number_input("Taux d'intérêt actuel (r)", value=0.025, step=0.001)
g = st.sidebar.number_input("Taux de croissance actuel (g)", value=0.018, step=0.001)
s0 = st.sidebar.number_input("Solde primaire actuel (% PIB)", value=-0.032, step=0.01)
x0 = st.sidebar.number_input("Dette actuelle (% PIB)", value=1.15, step=0.01)
a0 = st.sidebar.number_input("Année actuelle", value=2025, step=1)
x_Obj = st.sidebar.number_input("Objectif de dette (% PIB)", value=1.0, step=0.01)
t = st.sidebar.number_input("Durée de projection pour la trajectoire  (années)", value=5, step=1)
n = st.sidebar.number_input("Durée pour atteindre l'objectif de dette (années)", value=10, step=1)
effort = st.sidebar.number_input("Effort annuel pour l'ajustement progressif", value=0.005, step=0.001)


# Menu
menu = st.sidebar.radio(
    "Choisissez une section",
    [
        "Situation actuelle",
        "Ajustement instantané",
        "Ajustement progressif",
        "Réduction de dette",
        "Réduction de dette (solde constant)"
    ]
)

