def eliminar_evento():
    st.title("Eliminar Evento")
    container = st.container()
    col1, col2 = container.columns(2)

    with col1:
        tipo_evento = st.selectbox("Tipo de evento", ["Bar", "Teatro", "Filantropico"])
        nombre_evento = st.text_input("Nombre del evento")

    with col2:
        if st.button("Eliminar"):
            admin_eventos.eliminar_evento(tipo_evento.lower(), nombre_evento)


def vender_boletas():
    st.title("Vender Boletas")
    container = st.container()
    col1, col2 = container.columns(2)

    with col1:
        tipo_evento = st.selectbox("Tipo de evento", ["Filantropico", "Bar", "Teatro"])
        nombre_evento = st.text_input("Nombre del evento")

    with col2:
        if st.button("Vender"):
            admin_eventos.vender_boletas(tipo_evento.lower(), nombre_evento)


def crear_artista():
    st.title("Crear Nuevo Artista")
    container = st.container()
    col1, col2 = container.columns(2)

    with col1:
        nombre = st.text_input("Nombre del artista")
    with col2:
        tipo_artista = st.text_input("Tipo de artista")

    if st.button("Crear"):
        admin_eventos.crear_artista(nombre, tipo_artista)


def asignar_artista():
    st.title("Asignar Artista a Evento")
    container = st.container()
    col1, col2 = container.columns(2)

    with col1:
        tipo_evento = st.selectbox("Tipo de evento", ["Bar", "Teatro", "Filantropico"])
        nombre_evento = st.text_input("Nombre del evento")
    with col2:
        nombre_artista = st.text_input("Nombre del artista")

    if st.button("Asignar"):
        admin_eventos.asignar_artista(tipo_evento.lower(), nombre_evento, nombre_artista)


def mostrar_detalles_evento():
    st.title("Mostrar Detalles de Evento")
    container = st.container()
    col1, col2 = container.columns(2)

    with col1:
        tipo_evento = st.selectbox("Tipo de evento", ["Bar", "Teatro", "Filantropico"])
        nombre_evento = st.text_input("Nombre del evento")

    with col2:
        if st.button("Mostrar"):
            admin_eventos.mostrar_detalles_evento(tipo_evento.lower(), nombre_evento)


