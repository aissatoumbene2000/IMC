import streamlit as st

st.title("🩺 Calculateur d'IMC")
poids = st.number_input("Poids (kg) :", min_value=0.1, value=70.0, step=0.1)
taille_cm = st.number_input("Taille (cm) :", min_value=50.0, value=170.0, step=0.1)
taille = taille_cm / 100

if st.button("Calculer l'IMC"):
    if taille > 0:
        imc = poids / (taille ** 2)  # Correction : ** pour puissance 2
        st.metric("Votre IMC", f"{imc:.2f}", delta=None)

        if imc < 18.5:
            categorie = "🔴 Maigreur"
            couleur = "inverse"
        elif imc < 25:
            categorie = "🟢 Corpulence normale"
            couleur = "normal"
        elif imc < 30:
            categorie = "🟡 Surpoids"
            couleur = "warning"
        else:
            categorie = "🔴 Obésité"
            couleur = "inverse"

        st.info(f"**Catégorie : {categorie}**", icon="📊")
    else:
        st.error("La taille doit être > 0 !")​

