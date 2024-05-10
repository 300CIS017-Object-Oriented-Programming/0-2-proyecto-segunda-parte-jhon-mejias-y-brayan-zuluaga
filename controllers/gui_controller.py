import streamlit as st
from game_controller import AdministrarEventos

# Initialize the event manager
event_manager = AdministrarEventos()

# Define Streamlit app
def main():
    st.title("Event Management System")

    # Sidebar menu
    menu = ["Crear Evento", "Editar Evento", "Eliminar Evento", "Fase de Ventas", "Generar Reportes", "Vender Boletas", "Crear Artista", "Asignar Artista", "Mostrar Detalles de Evento", "Imprimir Eventos"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Crear Evento":
        st.subheader("Crear Nuevo Evento")
        event_manager.crear_evento()

    elif choice == "Editar Evento":
        st.subheader("Editar Evento Existente")
        event_manager.editar_evento()

    elif choice == "Eliminar Evento":
        st.subheader("Eliminar Evento Existente")
        event_manager.eliminar_evento()

    elif choice == "Fase de Ventas":
        st.subheader("Actualizar Fase de Ventas")
        event_manager.fase_ventas()

    elif choice == "Generar Reportes":
        report_options = ["Reporte de Ventas", "Reporte Financiero", "Reporte de Compradores", "Reporte de Artistas"]
        report_choice = st.selectbox("Seleccione el tipo de reporte", report_options)

        if report_choice == "Reporte de Ventas":
            event_manager.generar_ventas()
        elif report_choice == "Reporte Financiero":
            event_manager.generar_financiero()
        elif report_choice == "Reporte de Compradores":
            event_manager.generar_compradores()
        elif report_choice == "Reporte de Artistas":
            event_manager.generar_artistas()

    elif choice == "Vender Boletas":
        st.subheader("Venta de Boletas")
        event_manager.vender_boletas()

    elif choice == "Crear Artista":
        st.subheader("Crear Nuevo Artista")
        event_manager.crear_artista()

    elif choice == "Asignar Artista":
        st.subheader("Asignar Artista a Evento")
        event_manager.asignar_artista()

    elif choice == "Mostrar Detalles de Evento":
        st.subheader("Mostrar Detalles de Evento")
        event_manager.mostrar_detalles_evento()

    elif choice == "Imprimir Eventos":
        st.subheader("Eventos Registrados")
        event_manager.imprimir_eventos()

if __name__ == "__main__":
    main()
