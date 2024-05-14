import streamlit as st
from controllers.game_controller import AdministrarEventos
from controllers.gui_controller import GuiController


class View():

    def __init__(self):
        if 'controler' not in st.session_state:
            st.session_state['controler'] = AdministrarEventos()

        if 'gui_view' not in st.session_state:
            st.session_state['gui_view'] = GuiController()

    def inicio(self):
        # Nuevo estilo CSS para los botones
        st.markdown("""
                   <style>
                       .stButton>button {
                           width: 90%;
                           font-weight: 600;
                           font-size: 18px;
                           padding: 15px;
                           margin: 5px;
                           border-radius: 5px;
                           background-color: #008080;
                           color: #FFF;
                           border: 2px solid transparent;
                           transition: all 0.3s ease;
                       }
                       .stButton>button:hover {
                           color: #008080;
                           background-color: #ffffff;
                           border: 2px solid #008080;
                           transform: scale(1.05);
                       }
                   </style>
               """, unsafe_allow_html=True)
        if st.session_state['gui_view'].get_menu():
            self.menu_principal()
        if st.session_state['gui_view'].get_creando_evento():
            self.crear_evento()
        if st.session_state['gui_view'].get_editando_evento():
            self.modificar_evento()
        if st.session_state['gui_view'].get_vendiendo_boletas():
            self.vender_boletas()
        if st.session_state['gui_view'].get_creando_artista():
            self.crear_artista()
        if st.session_state['gui_view'].get_asignando_artista():
            self.asignar_artista()
        if st.session_state['gui_view'].get_eliminando_evento():
            self.eliminar_evento()
        if st.session_state['gui_view'].get_imprimiendo_eventos():
            self.imprimir_eventos()


        footer_html = """
              <style>
                  .footer {
                      position: fixed;
                      left: 0;
                      bottom: 0;
                      width: 100%;
                      background-color: #008080;
                      color: white;
                      text-align: center;
                      padding: 15px 0;
                      font-size: 16px;
                      border-top: 4px solid #FFF;
                  }
              </style>
              <div class="footer">
                  <p>Desarrollado por: BZJM.</p>
              </div>
              """
        # Mostrar el nuevo footer
        st.markdown(footer_html, unsafe_allow_html=True)

    def crear_evento(self):
        st.title("Crear Evento")
        col1, col2, col3 = st.columns(3)

        with col1:
            if st.checkbox("Crear Evento Bar", key='crear_evento_bar'):
                self.crear_evento_bar()

        with col2:
            if st.checkbox("Crear Evento Teatro", key='crear_evento_teatro'):
                self.crear_evento_teatro()

        with col3:
            if st.checkbox("Crear Evento Filantropico", key='crear_evento_filantropico'):
                self.crear_evento_filantropico()

        if st.button("Atrás"):
            st.session_state['gui_view'].desactivate_creando_evento()
            st.session_state['gui_view'].activate_menu()
    def crear_evento_bar(self):

        st.title("Crear Evento Bar")
        col1, col2 = st.columns(2)  # Crear dos columnas

        with st.form(key='bar_form'):
            with col1:
                nombre = st.text_input("Ingrese el nombre del evento: ")
                fecha = st.date_input("Ingrese la fecha del evento: ")
                hora_inicio = st.time_input("Ingrese la hora de inicio del evento: ", key="hora_inicio_bar")
                lugar = st.text_input("Ingrese el lugar del evento: ")
                direccion = st.text_input("Ingrese la dirección del evento: ")



            with col2:
                hora_show = st.time_input("Ingrese la hora del show: ", key="hora_show_bar")
                ciudad = st.text_input("Ingrese la ciudad del evento: ")
                estado = st.selectbox("Estado del evento:",options=["Por realizar","Realizado" , "Cancelado", "Aplazado", "Cerrado"])
                aforo = st.text_input("Ingrese el aforo del evento: ")
                pago_artistas = st.slider("Valor a pagar al Artista:", min_value=0, max_value=10000,value=5000)
            submit_button = st.form_submit_button(label='Finalizar')
            if submit_button:
                aforo = int(aforo)  # Convertir el aforo a un entero
                st.session_state['controler'].crear_bar(nombre, fecha, hora_inicio, hora_show, lugar, direccion, ciudad,
                                                        estado, aforo, pago_artistas)
                st.success("Evento Bar creado exitosamente.")


    def crear_evento_teatro(self):
        st.title("Crear Evento Teatro")
        col1, col2 = st.columns(2)  # Crear dos columnas

        with st.form(key='teatro_form'):
            with col1:
                nombre = st.text_input("Ingrese el nombre del evento: ")
                fecha = st.date_input("Ingrese la fecha del evento: ")
                hora_inicio = st.time_input("Ingrese la hora de inicio del evento: ", key="hora_inicio_teatro")
                lugar = st.text_input("Ingrese el lugar del evento: ")
                direccion = st.text_input("Ingrese la dirección del evento: ")

            with col2:
                hora_show = st.time_input("Ingrese la hora del show: ", key="hora_show_teatro")
                ciudad = st.text_input("Ingrese la ciudad del evento: ")
                estado = st.selectbox("Estado del evento:",options=["Por realizar","Realizado" , "Cancelado", "Aplazado", "Cerrado"])
                aforo = st.text_input("Ingrese el aforo del evento: ")
                costo = st.slider("Valor del alquiler:", min_value=0, max_value=10000, value=5000)
            submit_button = st.form_submit_button(label='Finalizar')
            if submit_button:
                aforo = int(aforo)  # Convertir el aforo a un entero
                st.session_state['controler'].crear_teatro(nombre, fecha, hora_inicio, hora_show, lugar, direccion,
                                                           ciudad, estado, aforo, costo)
                st.success("Evento Teatro creado exitosamente.")

    def crear_evento_filantropico(self):
        st.title("Crear Evento Filantropico")
        col1, col2 = st.columns(2)  # Crear dos columnas

        with st.form(key='filantropico_form'):
            with col1:
                nombre = st.text_input("Ingrese el nombre del evento: ")
                fecha = st.date_input("Ingrese la fecha del evento: ")
                hora_inicio = st.time_input("Ingrese la hora de inicio del evento: ", key="hora_inicio_filantropico")
                lugar = st.text_input("Ingrese el lugar del evento: ")
                direccion = st.text_input("Ingrese la dirección del evento: ")

            with col2:
                hora_show = st.time_input("Ingrese la hora del show: ", key="hora_show_filantropico")
                ciudad = st.text_input("Ingrese la ciudad del evento: ")
                estado = st.selectbox("Estado del evento:",options=["Por realizar","Realizado" , "Cancelado", "Aplazado", "Cerrado"])
                aforo = st.text_input("Ingrese el aforo del evento: ")
                patrocinadores = st.text_input("Ingrese los patrocinadores del evento: ")  # Nuevo campo para patrocinadores
            submit_button = st.form_submit_button(label='Finalizar')
            if submit_button:
                aforo = int(aforo)  # Convertir el aforo a un entero
                st.session_state['controler'].crear_filantropico(nombre, fecha, hora_inicio, hora_show, lugar,
                                                                 direccion, ciudad, estado, aforo, patrocinadores)
                st.success("Evento Filantropico creado exitosamente.")
    def menu_principal(self):
        st.write("<h1 style='text-align: center;'>ComediaGonzos te da la bienvenida! </h1>", unsafe_allow_html=True)

        st.title("MENU PRINCIPAL")

        if st.button("Crear Evento"):
            st.session_state['gui_view'].activate_creando_evento()
            st.session_state['gui_view'].desactivate_menu()

        if st.button("Modificar Evento"):
            st.session_state['gui_view'].activate_editando_evento()
            st.session_state['gui_view'].desactivate_menu()

        if st.button("Imprimir eventos"):
            st.session_state['gui_view'].activate_imprimiendo_eventos()
            st.session_state['gui_view'].desactivate_menu()

        if st.button("Eliminar Evento"):
            st.session_state['gui_view'].activate_eliminando_evento()
            st.session_state['gui_view'].desactivate_menu()

        if st.button("Crear Artista"):
            st.session_state['gui_view'].activate_creando_artista()
            st.session_state['gui_view'].desactivate_menu()

        if st.button("Asignar Artista"):
            st.session_state['gui_view'].activate_asignando_artista()
            st.session_state['gui_view'].desactivate_menu()

        if st.button("Vender Boleta"):
            st.session_state['gui_view'].activate_vendiendo_boletas()
            st.session_state['gui_view'].desactivate_menu()

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


    def imprimir_eventos(self):
        st.title("Imprimir Eventos")

        if st.button("Imprimir Eventos de tipo Bar"):
            st.write("Eventos de tipo Bar:")
            for bar in st.session_state['controler'].bares:
                st.write(bar.get_nombre())

        if st.button("Imprimir Eventos de tipo Teatro"):
            st.write("Eventos de tipo Teatro:")
            for teatro in st.session_state['controler'].teatros:
                st.write(teatro.get_nombre())

        if st.button("Imprimir Eventos de tipo Filantropico"):
            st.write("Eventos de tipo Filantropico:")
            for filantropico in st.session_state['controler'].filantropicos:
                st.write(filantropico.get_nombre())

        if st.button("Atrás"):
            st.session_state['gui_view'].desactivate_imprimiendo_eventos()
            st.session_state['gui_view'].activate_menu()