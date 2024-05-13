import streamlit as st
from controllers.game_controller import AdministrarEventos
from controllers.gui_controller import GuiController


class View():

    def __init__(self):
        if 'controler' not in st.session_state:
            st.session_state['controler'] = AdministrarEventos()

        if 'gui_view' not in st.session_state:
            st.session_state['gui_view'] = GuiController()


    def eliminar_evento(self):
        st.title("Eliminar Evento")
        container = st.container()
        col1, col2 = container.columns(2)

        with col1:
            tipo_evento = st.selectbox("Tipo de evento", ["Bar", "Teatro", "Filantropico"])
            nombre_evento = st.text_input("Nombre del evento")

        with col2:
            if st.button("Eliminar"):
                st.session_state['controler'].eliminar_evento(tipo_evento.lower(), nombre_evento)


    def vender_boletas(self):
        st.title("Vender Boletas")
        container = st.container()
        col1, col2 = container.columns(2)

        with col1:
            tipo_evento = st.selectbox("Tipo de evento", ["Filantropico", "Bar", "Teatro"])
            nombre_evento = st.text_input("Nombre del evento")

        with col2:
            if st.button("Vender"):
                st.session_state['controler'].vender_boletas(tipo_evento.lower(), nombre_evento)


    def crear_artista(self):
        st.title("Crear Nuevo Artista")
        container = st.container()
        col1, col2 = container.columns(2)

        with col1:
            nombre = st.text_input("Nombre del artista")
        with col2:
            tipo_artista = st.text_input("Tipo de artista")

        if st.button("Crear"):
            st.session_state['controler'].crear_artista(nombre, tipo_artista)


    def asignar_artista(self):
        st.title("Asignar Artista a Evento")
        container = st.container()
        col1, col2 = container.columns(2)

        with col1:
            tipo_evento = st.selectbox("Tipo de evento", ["Bar", "Teatro", "Filantropico"])
            nombre_evento = st.text_input("Nombre del evento")
        with col2:
            nombre_artista = st.text_input("Nombre del artista")

        if st.button("Asignar"):
            st.session_state['controler'].asignar_artista(tipo_evento.lower(), nombre_evento, nombre_artista)


    def mostrar_detalles_evento(self):
        st.title("Mostrar Detalles de Evento")
        container = st.container()
        col1, col2 = container.columns(2)

        with col1:
            tipo_evento = st.selectbox("Tipo de evento", ["Bar", "Teatro", "Filantropico"])
            nombre_evento = st.text_input("Nombre del evento")

        with col2:
            if st.button("Mostrar"):
                st.session_state['controler'].mostrar_detalles_evento(tipo_evento.lower(), nombre_evento)


