import streamlit as st
st.title("🩺 Calculateur d'IMC")

poids = st.number_input("Poids (kg) :", min_value=0.1, value=70.0, step=0.1)
taille_cm = st.number_input("Taille (cm) :", min_value=50.0, value=170.0, step=0.1)
taille = taille_cm / 100  # Conversion en mètres

if st.button("Calculer l'IMC"):
    if taille > 0:
        imc = poids / (taille  2)
        st.success(f"Votre IMC est : {imc:.2f}")

        if imc < 18.5:
            categorie = "🔴 Maigreur"
        elif imc < 25:
            categorie = "🟢 Corpulence normale"
        elif imc < 30:
            categorie = "🟡 Surpoids"
        else:
            categorie = "🔴 Obésité"

        st.info(f"**Catégorie : {categorie}")
    else:
        st.error("La taille doit être supérieure à 0 !")