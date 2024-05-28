import streamlit as st
from controllers.game_controller import AdministrarEventos
from controllers.gui_controller import GuiController
import plotly.express as px
import os
class View():

    def __init__(self):
        self.widget_counter = 0
        if 'controler' not in st.session_state:
            st.session_state['controler'] = AdministrarEventos()

        if 'gui_view' not in st.session_state:
            st.session_state['gui_view'] = GuiController()

    def generate_key(self, base_key):
        # Generar una clave única para un widget
        unique_key = f"{base_key}_{self.widget_counter}"
        self.widget_counter += 1
        return unique_key
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
        if st.session_state['gui_view'].get_menu() and not st.session_state['gui_view'].get_creando_evento():
            self.menu_principal()
        if st.session_state['gui_view'].get_creando_evento():
            self.crear_evento()
        if st.session_state['gui_view'].get_editando_evento():
            self.modificar_evento() #aun no implementado
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
        if st.session_state['gui_view'].get_mostrando_detalles_evento():
            self.mostrar_detalles_evento()
        if st.session_state['gui_view'].get_registrar_ingreso():
            self.registrar_ingreso()
        if st.session_state['gui_view'].get_mostrar_reportes():
            self.mostrar_reportes()
        if st.session_state['gui_view'].get_asignar_patrocinador():
            self.asignar_patrocinadores()

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

        opcion = st.radio(
            "¿Qué tipo de evento quieres crear?",
            ('Crear Evento Bar', 'Crear Evento Teatro', 'Crear Evento Filantropico'),key=self.generate_key('unique_keys'))

        if opcion == 'Crear Evento Bar':
            self.crear_evento_bar()
        elif opcion == 'Crear Evento Teatro':
            self.crear_evento_teatro()
        elif opcion == 'Crear Evento Filantropico':
            self.crear_evento_filantropico()

        if st.button("Atrás",key=self.generate_key('unique_keys')):
            st.session_state['gui_view'].desactivate_creando_evento()
            st.session_state['gui_view'].activate_menu()
    def crear_evento_bar(self):

        st.title("Crear Evento Bar")
        col1, col2 = st.columns(2)  # Crear dos columnas

        with st.form(key=self.generate_key('unique_keys')):
            with col1:
                nombre = st.text_input("Ingrese el nombre del evento: ",key=self.generate_key('unique_keys'))
                fecha = st.date_input("Ingrese la fecha del evento: ",key=self.generate_key('unique_keys'))
                hora_inicio = st.time_input("Ingrese la hora de inicio del evento: ",key=self.generate_key('unique_keys'))
                lugar = st.text_input("Ingrese el lugar del evento: ",key=self.generate_key('unique_keys'))
                direccion = st.text_input("Ingrese la dirección del evento: ",key=self.generate_key('unique_keys'))



            with col2:
                hora_show = st.time_input("Ingrese la hora del show: ", key=self.generate_key('unique_keys'))
                ciudad = st.text_input("Ingrese la ciudad del evento: ",key=self.generate_key('unique_keys'))
                estado = st.selectbox("Estado del evento:",options=["Por realizar","Realizado" , "Cancelado", "Aplazado", "Cerrado"],key=self.generate_key('unique_keys'))
                aforo = st.number_input("Ingrese el aforo del evento", min_value=0, value=1, key=self.generate_key('unique_keys'))
                pago_artistas = st.number_input("Valor a pagar al Artista:", min_value=0, value=5000,
                                                key=self.generate_key('unique_keys'))
            submit_button = st.form_submit_button(label='Finalizar')
            if submit_button:
                # Verificar que todas las casillas estén llenas
                if nombre and fecha and hora_inicio and lugar and direccion and hora_show and ciudad and estado and aforo:
                    aforo = int(aforo)  # Convertir el aforo a un entero
                    st.session_state['controler'].crear_bar(nombre, fecha, hora_inicio, hora_show, lugar, direccion,
                                                            ciudad,
                                                            estado, aforo, pago_artistas)
                    st.success("Evento Bar creado exitosamente.")
                else:
                    st.error("Por favor, llena todas las casillas antes de enviar.")

    def modificar_evento(self):
        st.title("Modificar Evento")
        tipo_evento = st.selectbox("Seleccione el tipo de evento", ["Bar", "Teatro", "Filantropico"])
        nombre_evento = st.text_input("Ingrese el nombre del evento a modificar")

        with st.form(key='modificar_evento_form'):
            nueva_fecha = st.date_input("Nueva fecha del evento")
            nueva_hora_inicio = st.time_input("Nueva hora de inicio del evento")
            nuevo_estado = st.selectbox("Nuevo estado del evento",
                                        options=["Por realizar", "Realizado", "Cancelado", "Aplazado",
                                                 "Cerrado"])
            nuevo_aforo = st.number_input("Nuevo aforo del evento", min_value=0, value=1)
            if st.form_submit_button(label='Modificar Evento'):
                result = st.session_state['controler'].modificar_evento(tipo_evento, nombre_evento, nueva_fecha,
                                                                        nueva_hora_inicio, nuevo_estado, nuevo_aforo)
                if result:
                    st.success("Evento modificado exitosamente.")
                else:
                    st.error(f"No se encontró ningún evento con el nombre {nombre_evento} o no se pudo modificar.")
        if st.button("Atrás"):
            st.session_state['gui_view'].desactivate_editando_evento()
            st.session_state['gui_view'].activate_menu()

    def crear_evento_filantropico(self):
        st.title("Crear Evento Filantropico")
        col1, col2 = st.columns(2)  # Crear dos columnas

        with st.form(key='filantropico_form'):
            with col1:
                nombre = st.text_input("Ingrese el nombre del evento: ",key=self.generate_key('unique_keys'))
                fecha = st.date_input("Ingrese la fecha del evento: ",key=self.generate_key('unique_keys'))
                hora_inicio = st.time_input("Ingrese la hora de inicio del evento: ", key=self.generate_key('unique_keys'))
                lugar = st.text_input("Ingrese el lugar del evento: ",key=self.generate_key('unique_keys'))
                direccion = st.text_input("Ingrese la dirección del evento: ",key=self.generate_key('unique_keys'))

            with col2:
                hora_show = st.time_input("Ingrese la hora del show: ", key=self.generate_key('unique_keys'))
                ciudad = st.text_input("Ingrese la ciudad del evento: ",key=self.generate_key('unique_keys'))
                estado = st.selectbox("Estado del evento:",
                                      options=["Por realizar", "Realizado", "Cancelado", "Aplazado", "Cerrado"],key=self.generate_key('unique_keys'))
                aforo = st.number_input("Ingrese el aforo del evento", min_value=0, value=1, key=self.generate_key('unique_keys'))
                pago_artistas = st.number_input("Valor a pagar al Artista:", min_value=0, value=5000,
                                                key=self.generate_key('unique_keys'))

            submit_button = st.form_submit_button(label='Finalizar')
            if submit_button:
                if nombre and fecha and hora_inicio and lugar and direccion and hora_show and ciudad and estado and aforo:
                    aforo = int(aforo)  # Convertir el aforo a un entero
                    st.session_state['controler'].crear_filantropico(nombre, fecha, hora_inicio, hora_show, lugar,
                                                                     direccion, ciudad, estado, aforo, pago_artistas)
                    st.success("Evento Filantropico creado exitosamente.")
                else:
                    st.error("Por favor, llena todas las casillas antes de enviar.")

    def crear_evento_teatro(self):
        st.title("Crear Evento Teatro")
        col1, col2 = st.columns(2)  # Crear dos columnas

        with st.form(key='teatro_form'):
            with col1:
                nombre = st.text_input("Ingrese el nombre del evento: ",key=self.generate_key('unique_keys'))
                fecha = st.date_input("Ingrese la fecha del evento: ",key=self.generate_key('unique_keys'))
                hora_inicio = st.time_input("Ingrese la hora de inicio del evento: ", key=self.generate_key('unique_keys'))
                lugar = st.text_input("Ingrese el lugar del evento: ",key=self.generate_key('unique_keys'))
                direccion = st.text_input("Ingrese la dirección del evento: ",key=self.generate_key('unique_keys'))

            with col2:
                hora_show = st.time_input("Ingrese la hora del show: ", key="hora_show_teatro")
                ciudad = st.text_input("Ingrese la ciudad del evento: ")
                estado = st.selectbox("Estado del evento:",
                                      options=["Por realizar", "Realizado", "Cancelado", "Aplazado", "Cerrado"])
                aforo = st.number_input("Ingrese el aforo del evento", min_value=0, value=1, key=self.generate_key('unique_keys'))
                costo = st.number_input("Valor a pagar de alquiler:", min_value=0, value=100000,
                                                key=self.generate_key('unique_keys'))
                pago_artistas = st.number_input("Valor a pagar al Artista:", min_value=0, value=500000,
                                                key=self.generate_key('unique_keys'))
            submit_button = st.form_submit_button(label='Finalizar')
            if submit_button:
                if nombre and fecha and hora_inicio and lugar and direccion and hora_show and ciudad and estado and aforo:
                    aforo = int(aforo)  # Convertir el aforo a un entero
                    st.session_state['controler'].crear_teatro(nombre, fecha, hora_inicio, hora_show, lugar, direccion,
                                                               ciudad, estado, aforo, costo, pago_artistas)
                    st.success("Evento Teatro creado exitosamente.")
                else:
                    st.error("Por favor, llena todas las casillas antes de enviar.")
    def menu_principal(self):
        st.write("<h1 style='text-align: center;'>ComediaGonzos te da la bienvenida! </h1>", unsafe_allow_html=True)

        st.title("MENU PRINCIPAL")

        if st.button("Crear Evento"):
            st.session_state['gui_view'].activate_creando_evento()
            st.session_state['gui_view'].desactivate_menu()
            self.crear_evento()

        if st.button("Modificar Evento"):
            st.session_state['gui_view'].activate_editando_evento()
            st.session_state['gui_view'].desactivate_menu()

        if st.button("Mostrar Detalles de Evento"):
            st.session_state['gui_view'].activate_mostrando_detalles_evento()
            st.session_state['gui_view'].desactivate_menu()

        if st.button("Asignar Patrocinadores "):
            st.session_state['gui_view'].activate_asignar_patrocinador()
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

        if st.button("Registrar Ingreso"):
            st.session_state['gui_view'].activate_registrar_ingreso()
            st.session_state['gui_view'].desactivate_menu()

        if st.button("Reportes"):
            st.session_state['gui_view'].activate_mostrar_reportes()
            st.session_state['gui_view'].desactivate_menu()

    def eliminar_evento(self):
        st.title("Eliminar vento")
        tipo_evento = st.selectbox("Seleccione el tipo de evento", ["bar", "teatro", "filantropico"])
        nombre_evento = st.text_input("Ingrese el nombre del evento a eliminar")

        if st.button("Eliminar Evento"):
            resultado = st.session_state['controler'].eliminar_evento(tipo_evento, nombre_evento)
            if resultado:
                st.success(f"El evento {nombre_evento} ha sido eliminado exitosamente.")
            else:
                st.error(f"No se encontró ningún evento con el nombre {nombre_evento}.")
        if st.button("Atrás"):
            st.session_state['gui_view'].desactivate_eliminando_evento()
            st.session_state['gui_view'].activate_menu()

    def vender_boletas(self):
        st.title("Vender Boletas")
        container = st.container()
        col1, col2 = container.columns(2)

        with col1:
            tipo_evento = st.selectbox("Tipo de evento", ["Filantropico", "Bar", "Teatro"], key='unique_keys_0')
            nombre_evento = st.text_input("Nombre del evento")
            cantidad_boletas = st.number_input("Cantidad de boletas a vender", min_value=1, step=1)
            codigo_descuento = st.text_input("Código de descuento (opcional)")
        with col2:
            nombre_asistente = st.text_input("Nombre del asistente")
            apellido_asistente = st.text_input("Apellido del asistente")
            edad = st.number_input("Edad del asistente", min_value=1, step=1)
            direccion = st.text_input("Dirección del asistente")
            medio_enterado = st.selectbox("¿Cómo se enteró del evento?", ["Internet", "Radio", "Televisión", "Amigos/Familia", "Otros"])
            tipo_boleteria = st.selectbox("Tipo de boleteria", ["preventa", "regular","cortesia"])
            # Mostrar el precio de la boleta tan pronto como el usuario seleccione el tipo de boletería
            if tipo_evento == "Filantropico" and tipo_boleteria in ["preventa", "regular"]:
                precio = 0
            else:
                precio = st.session_state['controler'].precio_boleta(tipo_boleteria)
            st.write(f"Precio de la boleta: {precio}")
            metodo_pago = st.selectbox("Método de pago", ["efectivo", "tarjeta"])

            total = precio * cantidad_boletas
            if codigo_descuento == "Mayo2024":
                total = total * 0.8  # Aplicar un descuento del 20%
            st.write(f"El precio Total es: {total}")


        if st.button("Vender"):
            resultado = st.session_state['controler'].vender_boletas(tipo_evento, nombre_evento,
                                                                     nombre_asistente, apellido_asistente, edad,
                                                                     direccion, medio_enterado, tipo_boleteria,
                                                                     metodo_pago, cantidad_boletas)
            if resultado:
                st.success(f"Se vendió una boleta para el evento {nombre_evento}.")
                evento = st.session_state['controler'].buscar_evento(tipo_evento, nombre_evento)
                if evento is not None:
                    st.session_state['controler'].generar_boleta(nombre_asistente, apellido_asistente, edad, direccion,
                                                                 medio_enterado, tipo_boleteria, cantidad_boletas,
                                                                 total, nombre_evento, evento.get_fecha(),
                                                                 evento.get_hora_inicio(), evento.get_lugar(),
                                                                 evento.get_direccion(), evento.get_hora_show(),
                                                                 evento.get_ciudad(), evento.get_estado(),
                                                                 evento.get_aforo(), tipo_evento)
                else:
                    st.error("No se pudo encontrar el evento.")
            else:
                st.error(
                    "No se pudo vender la boleta.La cantidad de aforo llego a su limite, estas colocando mal el nombre o tipo del evento")
        # Agregar botón de "Atrás"
        if st.button("Atrás"):
            st.session_state['gui_view'].desactivate_vendiendo_boletas()
            st.session_state['gui_view'].activate_menu()

    def crear_artista(self):
        st.title("Crear Nuevo Artista")
        container = st.container()
        col1, col2 = container.columns(2)

        with col1:
            nombre = st.text_input("Nombre del artista")
        with col2:
            tipo_artista = st.text_input("Tipo de artista")

        if st.button("Crear"):
            resultado = st.session_state['controler'].crear_artista(nombre, tipo_artista)
            if resultado:
                st.success("Artista creado exitosamente.")
            else:
                st.error("No se pudo crear el artista.")
        if st.button("Atrás"):
            st.session_state['gui_view'].desactivate_creando_artista()
            st.session_state['gui_view'].activate_menu()

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
            resultado = st.session_state['controler'].asignar_artista(tipo_evento, nombre_evento,nombre_artista)
            if resultado:
                st.success("Artista asignado exitosamente.")
            else:
                st.error("No se pudo asignar el artista.")

        if st.button("Atrás"):
            st.session_state['gui_view'].desactivate_asignando_artista()
            st.session_state['gui_view'].activate_menu()

    def mostrar_detalles_evento(self):
        st.title("Mostrar Detalles de Evento")
        tipo_evento = st.selectbox("Seleccione el tipo de evento", ["bar", "teatro", "filantropico"])
        nombre_evento = st.text_input("Ingrese el nombre del evento a mostrar")

        if st.button("Mostrar Detalles"):
            detalles = st.session_state['controler'].mostrar_detalles_evento(tipo_evento, nombre_evento)
            if detalles:
                for linea in detalles.split('\n'):
                    st.markdown(linea)
            else:
                st.error(f"No se encontró ningún evento con el nombre {nombre_evento}.")
        if st.button("Atrás"):
            st.session_state['gui_view'].desactivate_mostrando_detalles_evento()
            st.session_state['gui_view'].activate_menu()

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

    def registrar_ingreso(self):
        st.title("Registrar Ingreso")
        tipo_evento = st.selectbox("Tipo de evento", ["Filantropico", "Bar", "Teatro"], key=self.generate_key('unique_keys'))
        nombre_evento = st.text_input("Nombre del evento", key=self.generate_key('unique_keys'))
        nombre_asistente = st.text_input("Nombre del asistente", key=self.generate_key('unique_keys'))
        cantidad_personas = st.number_input("Cantidad de personas a ingresar", min_value=1, step=1, key=self.generate_key('unique_keys'))

        if st.button("Registrar",key=self.generate_key('unique_keys')):
            for personas in range(cantidad_personas):
                resultado = st.session_state['controler'].registrar_ingreso(nombre_evento, tipo_evento, nombre_asistente)
                if resultado:
                    st.success("se registró la asistencia exitosamente.")
                else:
                    st.error("No se pudo registrar la asistencia. Verifica que el evento y el asistente existan.")

        if st.button("Atrás",key=self.generate_key('unique_keys')):
            st.session_state['gui_view'].desactivate_registrar_ingreso()
            st.session_state['gui_view'].activate_menu()

    def mostrar_reportes(self):
        st.title("Reportes")

        reporte_option = st.selectbox("Seleccione el tipo de reporte",
                                      ["Generar Reporte de Ventas", "Generar Reporte Financiero",
                                       "Generar Reporte de Compradores", "Generar Reporte de Datos por Artista"])

        # Pide al usuario el nombre y tipo del evento



        if reporte_option == "Generar Reporte de Ventas":
            nombre_evento = st.text_input("Nombre del evento")
            tipo_evento = st.selectbox("Tipo de evento", ["Bar", "Teatro", "Filantropico"])
            # Llama al método para generar el reporte de ventas y muestra los resultados
            if st.button("Generar"):
                reporte = st.session_state['controler'].generar_reporte_ventas(nombre_evento, tipo_evento)
                st.write(reporte)

        elif reporte_option == "Generar Reporte Financiero":
            nombre_evento = st.text_input("Nombre del evento")
            tipo_evento = st.selectbox("Tipo de evento", ["Bar", "Teatro", "Filantropico"])
            # Llama al método para generar el reporte financiero y muestra los resultados
            if st.button("Generar"):
                df_reporte = st.session_state['controler'].generar_reporte_financiero(nombre_evento, tipo_evento)
                st.write(df_reporte)

        elif reporte_option == "Generar Reporte de Compradores":
            nombre_evento = st.text_input("Nombre del evento")
            tipo_evento = st.selectbox("Tipo de evento", ["Bar", "Teatro", "Filantropico"])
            # Llama al método para generar el reporte de compradores
            if st.button("Generar"):
                df = st.session_state['controler'].generar_reporte_compradores(nombre_evento, tipo_evento)

                # Crear un histograma de las edades de los compradores
                fig1 = px.histogram(df, x="Edad", nbins=10, title="Distribución de Edades de los Compradores")
                st.plotly_chart(fig1)

                # Crear un gráfico de barras de los medios por los cuales los compradores se enteraron del evento
                fig2 = px.bar(df["Medio Enterado"].value_counts(),
                              title="Medios por los que los Compradores se Enteraron del Evento")
                st.plotly_chart(fig2)

                # Exportar los datos a un archivo Excel
                df.to_excel("outputs/reporte_compradores.xlsx", index=False)
                # Después de crear el archivo Excel
                os.startfile(os.path.realpath("outputs/reporte_compradores.xlsx"))

        elif reporte_option == "Generar Reporte de Datos por Artista":
            # Pide al usuario el nombre del artista
            nombre_artista = st.text_input("Nombre del artista")
            if st.button("Generar"):
                # Llama al método para generar el reporte de artistas y muestra los resultados
                reporte = st.session_state['controler'].generar_reporte_artistas(nombre_artista)
                st.write(reporte)

        if st.button("Atrás"):
            # Vuelve al menú principal
            st.session_state['gui_view'].desactivate_mostrar_reportes()
            st.session_state['gui_view'].activate_menu()
    def asignar_patrocinadores(self):
        st.title("Asignar Patrocinadores")
        container = st.container()
        col1, col2 = container.columns(2)

        with col1:
            nombre_evento = st.text_input("Nombre del evento")
        with col2:
            nombre_patrocinador = st.text_input("Nombre del patrocinador")
            donacion_pratrocinador = st.text_input("Donacion del patrocinador")

        if st.button("Asignar"):
            resultado = st.session_state['controler'].asignar_patrocinadores(nombre_evento, nombre_patrocinador,donacion_pratrocinador)
            if resultado:
                st.success("Patrocinador asignado exitosamente.")
            else:
                st.error("No se pudo asignar el patrocinador.")
        if st.button("Mostrar Patrocinadores"):
            st.write("Patrocinadores:")
            patrocinadores = st.session_state['controler'].patrocinadores_evento(nombre_evento)
            if patrocinadores is not None:
                for patrocinador, valor in patrocinadores.items():
                    st.write(f"Patrocinador: {patrocinador}, Valor: {valor}")
            else:
                st.write("No se encuentra el patrocinador.")

        if st.button("Atrás"):
            st.session_state['gui_view'].desactivate_asignar_patrocinador()
            st.session_state['gui_view'].activate_menu()