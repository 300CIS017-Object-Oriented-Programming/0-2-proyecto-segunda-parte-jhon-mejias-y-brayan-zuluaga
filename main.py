from view import main_view
import streamlit as st

def main():
    # Configuracion de la pestaña
    st.set_page_config(
        page_title="ComediaGonzos.com",  # Título de la pestaña
        page_icon="😁",  # Icono de la pestaña
        layout="wide",
        initial_sidebar_state="auto")

    control = main_view.View()
    control.inicio()
    return 0

main()