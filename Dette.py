# app.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# INTERFACE UTILISATEUR
# =============================================================================
st.title("Simulation de la dette publique")

# Paramètres ajustables
r = st.sidebar.number_input("Taux d'intérêt (r)", value=0.025, step=0.001)
g = st.sidebar.number_input("Taux de croissance (g)", value=0.018, step=0.001)
x0 = st.sidebar.number_input("Dette initiale (% PIB)", value=1.15, step=0.01)
s0 = st.sidebar.number_input("Solde primaire initial (% PIB)", value=-0.032, step=0.01)
x_Obj = st.sidebar.number_input("Objectif de dette (% PIB)", value=1.0, step=0.01)
t = st.sidebar.number_input("Durée courte (années)", value=5, step=1)
n = st.sidebar.number_input("Durée pour objectif de dette (années)", value=10, step=1)
effort = st.sidebar.number_input("Effort annuel max pour lissage", value=0.005, step=0.001)
a0 = st.sidebar.number_input("Année de départ", value=2025, step=1)

# =============================================================================
# FONCTIONS
# =============================================================================
def d(x, s):
    return ((1 + r) / (1 + g)) * x - s

def s_stable(x):
    return ((r - g) / (1 + g)) * x

def x_stable(s):
    return s / ((1 + r) / (1 + g) - 1)

# =============================================================================
# SECTION : SOLDE CONSTANT
# =============================================================================
alpha = (1 + r) / (1 + g)
s_const = (alpha**n * x0 - x_Obj) * (1 - alpha) / (1 - alpha**n)

# Simulation trajectoire dette
x = x0
dette_const = [x * 100]
solde_const = [s_const * 100]

for _ in range(n):
    x = d(x, s_const)
    dette_const.append(x * 100)
    solde_const.append(s_const * 100)

annee_const = [a0 + i for i in range(len(dette_const))]

# =============================================================================
# AFFICHAGE
# =============================================================================
st.subheader("Solde primaire constant et trajectoire de la dette")
st.write(f"Solde primaire constant nécessaire : {s_const*100:.2f}% du PIB")

# Trajectoire du solde
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(annee_const, solde_const, color='blue', marker='o', linestyle='-')
ax.set_xlabel("Années")
ax.set_ylabel("Solde en % du PIB")
ax.set_title("Trajectoire du solde primaire constant")
ax.grid(True, linestyle=':')
st.pyplot(fig)

# Trajectoire de la dette
fig2, ax2 = plt.subplots(figsize=(10, 5))
ax2.plot(annee_const, dette_const, color='red', marker='o', linestyle='-')
ax2.set_xlabel("Années")
ax2.set_ylabel("Dette en % du PIB")
ax2.set_title("Trajectoire de la dette avec solde constant")
ax2.grid(True, linestyle=':')
st.pyplot(fig2)

# Résumé final
st.write(f"Dette initiale : {dette_const[0]:.2f}% du PIB")
st.write(f"Dette finale après {n} ans : {dette_const[-1]:.2f}% du PIB")

