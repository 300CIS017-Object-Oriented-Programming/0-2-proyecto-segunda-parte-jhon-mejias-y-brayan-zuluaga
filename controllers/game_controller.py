from typing import List, Dict
from models.Filantropico import Filantropico
from models.Bar import Bar
from models.Teatro import Teatro
from models.Artista import Artista
from models.Asistente import Asistente
from models.Boleteria import Boleteria
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
import pandas as pd
import webbrowser
import os


class AdministrarEventos:
    def __init__(self):
        """
        Initializes the AdministrarEventos class with empty lists for different types of events and artists,
        and an empty dictionary for sold tickets.
        """
        self.filantropicos: List[Filantropico] = []
        self.bares: List[Bar] = []
        self.teatros: List[Teatro] = []
        self.artistas: Dict[str, Artista] = {}
        self.boletas_vendidas = {}



    def crear_bar(self, nombre, fecha, hora_inicio, hora_show, lugar, direccion, ciudad, estado, aforo, pago_artistas):

        """
        Creates a new bar event and adds it to the list of bar events.

        This function creates a new bar event with the given details, including the name, date, start time, show time, venue, address, city, state, capacity, and artist payment. The new event is then added to the list of bar events.

        Parameters:
        nombre (str): The name of the event.
        fecha (str): The date of the event.
        hora_inicio (str): The start time of the event.
        hora_show (str): The show time of the event.
        lugar (str): The venue of the event.
        direccion (str): The address of the event venue.
        ciudad (str): The city where the event is taking place.
        estado (str): The state where the event is taking place.
        aforo (int): The capacity of the event.
        pago_artistas (float): The payment for the artists for the event.

        Returns:
        None
        """

        bar = Bar(nombre, fecha, hora_inicio, hora_show, lugar, direccion, ciudad, estado, aforo, pago_artistas)
        self.bares.append(bar)

    def crear_teatro(self, nombre, fecha, hora_inicio, hora_show, lugar, direccion, ciudad, estado, aforo, costo, pago_artistas):

        """
        Creates a new theater event and adds it to the list of theater events.

        This function creates a new theater event with the given details, including the name, date, start time, show time, venue, address, city, state, capacity, cost, and artist payment. The new event is then added to the list of theater events.

        Parameters:
        nombre (str): The name of the event.
        fecha (str): The date of the event.
        hora_inicio (str): The start time of the event.
        hora_show (str): The show time of the event.
        lugar (str): The venue of the event.
        direccion (str): The address of the event venue.
        ciudad (str): The city where the event is taking place.
        estado (str): The state where the event is taking place.
        aforo (int): The capacity of the event.
        costo (float): The cost of the event.
        pago_artistas (float): The payment for the artists for the event.

        Returns:
        None
        """

        teatro = Teatro(nombre, fecha, hora_inicio, hora_show, lugar, direccion, ciudad, estado, aforo,pago_artistas)
        teatro.costo = costo
        self.teatros.append(teatro)

    def crear_filantropico(self, nombre, fecha, hora_inicio, hora_show, lugar, direccion, ciudad, estado, aforo, pago_artistas):
        """
        Creates a new philanthropic event and adds it to the list of philanthropic events.

        This function creates a new philanthropic event with the given details, including the name, date, start time, show time, venue, address, city, state, capacity, sponsors, and artist payment. The sponsors are given as a string and are split into individual sponsors, which are added to the event's list of sponsors. The new event is then added to the list of philanthropic events.

        Parameters:
        nombre (str): The name of the event.
        fecha (str): The date of the event.
        hora_inicio (str): The start time of the event.
        hora_show (str): The show time of the event.
        lugar (str): The venue of the event.
        direccion (str): The address of the event venue.
        ciudad (str): The city where the event is taking place.
        estado (str): The state where the event is taking place.
        aforo (int): The capacity of the event.
        patrocinadores (str): The sponsors of the event, given as a string with individual sponsors separated by commas.
        pago_artistas (float): The payment for the artists for the event.

        Returns:
        None
        """
        filantropico = Filantropico(nombre, fecha, hora_inicio, hora_show, lugar, direccion, ciudad, estado, aforo, pago_artistas)


        self.filantropicos.append(filantropico)



    def eliminar_evento(self, tipo_evento, nombre_evento):

        """
        Deletes an event from the list of events.

        This function iterates over the list of events of the given type. If it finds an event with the given name, it removes the event from the list and returns True. If no matching event is found, it does nothing and returns False.

        Parameters:
        tipo_evento (str): The type of the event (Bar, Theater, Philanthropic).
        nombre_evento (str): The name of the event.

        Returns:
        bool: True if the event was successfully deleted, False otherwise.
        """

        if tipo_evento.lower() == "bar":
            for i, bar in enumerate(self.bares):
                if bar.get_nombre() == nombre_evento:
                    del self.bares[i]
                    return True
        elif tipo_evento.lower() == "teatro":
            for i, teatro in enumerate(self.teatros):
                if teatro.get_nombre() == nombre_evento:
                    del self.teatros[i]
                    return True
        elif tipo_evento.lower() == "filantropico":
            for i, filantropico in enumerate(self.filantropicos):
                if filantropico.get_nombre() == nombre_evento:
                    del self.filantropicos[i]
                    return True

    def vender_boletas(self, tipo_evento, nombre_evento, nombre_asistente, apellido_asistente, edad, direccion, medio_enterado, tipo_boleteria, metodo_pago, cantidad_boletas):

        """
        Sells tickets for a specific event to an attendee.

        This function first identifies the event by its type and name. If the event is found and there is enough capacity for the number of tickets being bought, it creates an attendee with the given details, adds the attendee to the event, and sells the specified number of tickets to the attendee. The function returns True if the tickets were successfully sold, and False otherwise.

        Parameters:
        tipo_evento (str): The type of the event (Filantropico, Bar, Teatro).
        nombre_evento (str): The name of the event.
        nombre_asistente (str): The name of the attendee.
        apellido_asistente (str): The surname of the attendee.
        edad (int): The age of the attendee.
        direccion (str): The address of the attendee.
        medio_enterado (str): How the attendee heard about the event.
        tipo_boleteria (str): The type of ticket being bought by the attendee.
        metodo_pago (str): The payment method used by the attendee.
        cantidad_boletas (int): The number of tickets being bought by the attendee.

        Returns:
        bool: True if the tickets were successfully sold, False otherwise.
        """

        evento_seleccionado = None
        if tipo_evento == "Filantropico":
            for evento in self.filantropicos:
                if evento.get_nombre() == nombre_evento:
                    evento_seleccionado = evento
                    break
        elif tipo_evento == "Bar":
            for evento in self.bares:
                if evento.get_nombre() == nombre_evento:
                    evento_seleccionado = evento
                    break
        elif tipo_evento == "Teatro":
            for evento in self.teatros:
                if evento.get_nombre() == nombre_evento:
                    evento_seleccionado = evento
                    break

        precio = self.precio_boleta(tipo_boleteria)
        total_a_pagar = precio * cantidad_boletas
        if evento_seleccionado is None:
            return False
        if evento_seleccionado.get_cantidad_asistentes() + cantidad_boletas <= evento_seleccionado.get_aforo():
            asistente = Asistente(nombre_asistente, apellido_asistente, edad, direccion, medio_enterado)
            evento_seleccionado.agregar_asistente(asistente)

            for boletass in range(cantidad_boletas):# Vender la cantidad especificada de boletas
                asistente.comprarBoleta()
                evento_seleccionado.sumar_personas()
                nueva_boleteria = Boleteria(tipo_boleteria, self.precio_boleta("preventa"), self.precio_boleta("regular"), metodo_pago)
                evento_seleccionado.agregar_boleteria(nueva_boleteria)

            return True
        else:
            return False


    def mostrar_detalles_evento(self, tipo_evento, nombre_evento):

        """
        Searches for an event by its type and name and returns its details.

        This function iterates over the list of events of the given type. If it finds an event with the given name, it returns the details of the event. If no matching event is found, it returns None.

        Parameters:
        tipo_evento (str): The type of the event (bar, teatro, filantropico).
        nombre_evento (str): The name of the event.

        Returns:
        str: The details of the event if found, None otherwise.
        """

        evento_encontrado = None

        if tipo_evento.lower() == "bar":
            for bar in self.bares:
                if bar.get_nombre() == nombre_evento:
                    evento_encontrado = bar
                    break
        elif tipo_evento.lower() == "teatro":
            for teatro in self.teatros:
                if teatro.get_nombre() == nombre_evento:
                    evento_encontrado = teatro
                    break
        elif tipo_evento.lower() == "filantropico":
            for filantropico in self.filantropicos:
                if filantropico.get_nombre() == nombre_evento:
                    evento_encontrado = filantropico
                    break

        if evento_encontrado:
            return evento_encontrado.mostrar_detalles()
        else:
            return None



    def crear_artista(self, nombre, tipo_artista):

        """
        Creates a new artist and adds them to the list of artists.

        This function checks if an artist with the given name already exists. If the artist exists, it returns False. If the artist does not exist, it creates a new artist with the given name and type, adds the artist to the list of artists, and returns True.

        Parameters:
        nombre (str): The name of the artist.
        tipo_artista (str): The type of the artist.

        Returns:
        bool: True if the artist was successfully created and added, False otherwise.
        """

        if nombre in self.artistas:
            return False
        else:
            nuevo_artista = Artista(nombre, tipo_artista)
            self.artistas[nombre] = nuevo_artista
            return True

    def asignar_artista(self, tipo_evento, nombre_evento, nombre_artista):
        """
        Assigns an artist to an event.

        This function iterates over the list of events of the given type. If it finds an event with the given name, it checks if the artist exists. If the artist exists, it assigns the artist to the event and adds the event to the artist's list of events. The function returns True if the artist was successfully assigned, and False otherwise.

        Parameters:
        tipo_evento (str): The type of the event (Bar, Theater, Philanthropic).
        nombre_evento (str): The name of the event.
        nombre_artista (str): The name of the artist.

        Returns:
        bool: True if the artist was successfully assigned, False otherwise.
        """

        if tipo_evento == "Bar":
            for bar in self.bares:
                if bar.get_nombre() == nombre_evento:
                    if nombre_artista in self.artistas:
                        bar.asignar_artista(nombre_artista, self.artistas[nombre_artista])
                        self.artistas[nombre_artista].agregar_evento(tipo_evento, nombre_evento)
                        return True
                    else:
                        return False

        elif tipo_evento == "Teatro":
            for teatro in self.teatros:
                if teatro.get_nombre() == nombre_evento:
                    if nombre_artista in self.artistas:
                        teatro.asignar_artista(nombre_artista, self.artistas[nombre_artista])
                        self.artistas[nombre_artista].agregar_evento(tipo_evento, nombre_evento)
                        return True
                    else:
                        return False
        elif tipo_evento == "Filantropico":
            for filantropico in self.filantropicos:
                if filantropico.get_nombre() == nombre_evento:
                    if nombre_artista in self.artistas:
                        filantropico.asignar_artista(nombre_artista, self.artistas[nombre_artista])
                        self.artistas[nombre_artista].agregar_evento(tipo_evento, nombre_evento)
                        return True
                    else:
                        return False


    def imprimir_eventos(self):

        """
        Prints the names of all events categorized by their type.

        This function iterates over the lists of events of each type (Bar, Theater, Philanthropic) and prints the name of each event. The names are printed to the console.

        Parameters:
        None

        Returns:
        None
        """

        print("Eventos de tipo Bar:")
        for bar in self.bares:
            print(bar.get_nombre())

        print("Eventos de tipo Teatro:")
        for teatro in self.teatros:
            print(teatro.get_nombre())

        print("Eventos de tipo Filantropico:")
        for filantropico in self.filantropicos:
            print(filantropico.get_nombre())
    def precio_boleta(self, tipo_boleteria):

        """
        Determines the price of a ticket based on its type.

        This function returns the price of a ticket based on its type. The types of tickets can be "preventa", "regular", or "cortesia". If the type of ticket is not recognized, the function returns None.

        Parameters:
        tipo_boleteria (str): The type of the ticket.

        Returns:
        int: The price of the ticket if the type is recognized, None otherwise.
        """

        if tipo_boleteria == "preventa":
            return 5000
        elif tipo_boleteria == "regular":
            return 10000
        elif tipo_boleteria == "cortesia":
            return 0
        else:
            return None

    def generar_boleta(self, nombre_asistente, apellido_asistente, edad, direccion_asistente, medio_enterado,
                       tipo_boleteria, cantidad_boletas, total, nombre_evento, fecha, hora_inicio, lugar,
                       direccion_evento, hora_show, ciudad, estado, aforo, tipo_evento):
            """
           Generates a ticket for an event.

           This function creates a PDF ticket for an event with the details of the attendee, the event, and the purchase. The ticket includes the attendee's name, age, address, how they heard about the event, the type of ticket they bought, and the total amount paid. The event details include the name, date, start time, show time, venue, address, city, state, capacity, and type of the event. The ticket is saved as a PDF file and opened in a new browser tab.

           Parameters:
           nombre_asistente (str): The name of the attendee.
           apellido_asistente (str): The surname of the attendee.
           edad (int): The age of the attendee.
           direccion_asistente (str): The address of the attendee.
           medio_enterado (str): How the attendee heard about the event.
           tipo_boleteria (str): The type of ticket bought by the attendee.
           cantidad_boletas (int): The number of tickets bought by the attendee.
           total (float): The total amount paid by the attendee.
           nombre_evento (str): The name of the event.
           fecha (str): The date of the event.
           hora_inicio (str): The start time of the event.
           lugar (str): The venue of the event.
           direccion_evento (str): The address of the event venue.
           hora_show (str): The show time of the event.
           ciudad (str): The city where the event is taking place.
           estado (str): The state where the event is taking place.
           aforo (int): The capacity of the event.
           tipo_evento (str): The type of the event (Bar, Theater, Philanthropic).

           Returns:
           None
           """

            c = canvas.Canvas("outputs/boleta.pdf", pagesize=letter)

            width, height = letter

            # Define las posiciones x para las columnas
            x1 = 30
            x2 = width / 2
            # Agrega el logo
            logo_path = "img/logo.png"  # Reemplaza con la ruta a tu logo
            c.drawImage(logo_path, x1, height - 120, width=100, height=100)  # Ajusta las coordenadas y el ta

            # Agrega texto al PDF
            c.setFont("Times-Bold", 24)
            c.setFillColor(HexColor(0x000000))  # Set color to black  # Set color to blue
            c.drawString(x1, height - 160, "Boleta de Evento")



            c.setFont("Helvetica", 16)
            c.drawString(x1, height - 200, f"Nombre del asistente: {nombre_asistente} {apellido_asistente}")
            c.drawString(x1, height - 230, f"Edad del asistente: {edad}")
            c.drawString(x1, height - 260, f"Dirección del asistente: {direccion_asistente}")
            c.drawString(x1, height - 290, f"¿Cómo se enteró del evento?: {medio_enterado}")
            c.drawString(x1, height - 320, f"Tipo de boleteria: {tipo_boleteria}")
            c.drawString(x1, height - 350, f"Cantidad de boletas: {cantidad_boletas}")
            c.drawString(x1, height - 380, f"Total a pagar: {total}")

            c.drawString(x2, height - 200, f"Nombre del evento: {nombre_evento}")
            c.drawString(x2, height - 230, f"Fecha del evento: {fecha}")
            c.drawString(x2, height - 260, f"Hora de inicio del evento: {hora_inicio}")
            c.drawString(x2, height - 290, f"Lugar del evento: {lugar}")
            c.drawString(x2, height - 320, f"Dirección del evento: {direccion_evento}")
            c.drawString(x2, height - 350, f"Hora del show: {hora_show}")
            c.drawString(x2, height - 380, f"Ciudad del evento: {ciudad}")
            c.drawString(x2, height - 410, f"Estado del evento: {estado}")
            c.drawString(x2, height - 440, f"Aforo del evento: {aforo}")
            c.drawString(x2, height - 470, f"Tipo de evento: {tipo_evento}")

            # Finaliza y guarda el PDF
            c.save()
            # Después de crear el archivo PDF
            webbrowser.open_new(os.path.realpath("outputs/boleta.pdf"))

    def modificar_evento(self, tipo_evento, nombre_evento, nueva_fecha, nueva_hora_inicio, nuevo_estado, nuevo_aforo):
        """
        Modifies an existing event with the new details provided.

        This function searches for the event of the given type and name. If found, it updates the event's date, start time, state, and capacity with the new details provided.

        Parameters:
        tipo_evento (str): The type of the event (Bar, Theater, Philanthropic).
        nombre_evento (str): The name of the event.
        nueva_fecha (str): The new date of the event.
        nueva_hora_inicio (str): The new start time of the event.
        nuevo_estado (str): The new state of the event.
        nuevo_aforo (int): The new capacity of the event.

        Returns:
        bool: True if the event was successfully modified, False otherwise.
        """
        if tipo_evento == "Bar":
            for bar in self.bares:
                if bar.get_nombre() == nombre_evento:
                    bar.set_fecha(nueva_fecha)
                    bar.set_hora_inicio(nueva_hora_inicio)
                    bar.set_estado(nuevo_estado)
                    bar.set_aforo(nuevo_aforo)
                    return True
        elif tipo_evento == "Teatro":
            for teatro in self.teatros:
                if teatro.get_nombre() == nombre_evento:
                    teatro.set_fecha(nueva_fecha)
                    teatro.set_hora_inicio(nueva_hora_inicio)
                    teatro.set_estado(nuevo_estado)
                    teatro.set_aforo(nuevo_aforo)
                    return True
        elif tipo_evento == "Filantropico":
            for filantropico in self.filantropicos:
                if filantropico.get_nombre() == nombre_evento:
                    filantropico.set_fecha(nueva_fecha)
                    filantropico.set_hora_inicio(nueva_hora_inicio)
                    filantropico.set_estado(nuevo_estado)
                    filantropico.set_aforo(nuevo_aforo)
                    return True
        return False
    def buscar_evento(self, tipo_evento, nombre_evento):

        """
        Searches for an event by its type and name.

        This function iterates over the list of events of the given type. If it finds an event with the given name, it returns the event. If no matching event is found, it returns None.

        Parameters:
        tipo_evento (str): The type of the event (Bar, Theater, Philanthropic).
        nombre_evento (str): The name of the event.

        Returns:
        Evento: The event object if found, None otherwise.
        """

        if tipo_evento == "Filantropico":
            for evento in self.filantropicos:
                if evento.get_nombre() == nombre_evento:
                    return evento
        elif tipo_evento == "Bar":
            for evento in self.bares:
                if evento.get_nombre() == nombre_evento:
                    return evento
        elif tipo_evento == "Teatro":
            for evento in self.teatros:
                if evento.get_nombre() == nombre_evento:
                    return evento
        return None

    def registrar_ingreso(self, nombre_evento, tipo_evento, nombre_asistente):
        """
        Registers the attendance of an attendee to an event.

        This function checks the type of the event and iterates over the list of events of that type. If it finds an event with the given name, it iterates over the attendees of the event. If it finds an attendee with the given name, it confirms their attendance and returns True. If no matching event or attendee is found, it returns False.

        Parameters:
        nombre_evento (str): The name of the event.
        tipo_evento (str): The type of the event (Bar, Theater, Philanthropic).
        nombre_asistente (str): The name of the attendee.

        Returns:
        bool: True if the attendance was successfully registered, False otherwise.
        """

        if tipo_evento == "Filantropico":
            for filantropico in self.filantropicos:
                if filantropico.get_nombre() == nombre_evento:
                    for a in filantropico.asistentes:
                        if a.get_nombre() == nombre_asistente:
                            a.confirmacion = True
                            return True
        elif tipo_evento == "Bar":
            for bar in self.bares:
                if bar.get_nombre() == nombre_evento:
                    for a in bar.asistentes:
                        if a.get_nombre() == nombre_asistente:
                            a.confirmacion = True
                            return True
        elif tipo_evento == "Teatro":
            for teatro in self.teatros:
                if teatro.get_nombre() == nombre_evento:
                    for a in teatro.asistentes:
                        if a.get_nombre() == nombre_asistente:
                            a.confirmacion = True
                            return True
        return False

    def boletas_vendidas(self):
        # Retorna el diccionario de boletas vendidas
        return self.boletas_vendidas

    def generar_reporte_ventas(self, nombre_evento, tipo_evento):

        """
        Generates a sales report for a specific event.

        This function creates a report containing the number of tickets sold (categorized by ticket type) and the total income from ticket sales for a specific event. The report is returned as a pandas DataFrame.

        Parameters:
        nombre_evento (str): The name of the event for which the report is to be generated.
        tipo_evento (str): The type of the event (Bar, Theater, Philanthropic).

        Returns:
        df_reporte (DataFrame): A pandas DataFrame containing the report data.
        """

        # Crear una lista vacía para almacenar los datos del reporte
        reporte = []

        # Seleccionar la lista de eventos según el tipo de evento
        eventos = []
        if tipo_evento == "Bar":
            eventos = self.bares
        elif tipo_evento == "Teatro":
            eventos = self.teatros
        elif tipo_evento == "Filantropico":
            eventos = self.filantropicos
        # Iterar sobre los eventos del tipo seleccionado
        for evento in eventos:
            # Si el nombre del evento coincide con el nombre del evento dado
            if evento.get_nombre() == nombre_evento:
                # Obtener las boletas del evento
                boletas = evento.get_boleteria()
                # Contar las boletas por tipo
                boletas_por_tipo = {"preventa": 0, "regular": 0, "cortesia": 0}
                for boleta in boletas:
                    boletas_por_tipo[boleta.tipo_boleteria] += 1

                # Calcular los ingresos por preventa y venta regular
                ingresos_preventa = boletas_por_tipo["preventa"] * self.precio_boleta("preventa")
                ingresos_regular = boletas_por_tipo["regular"] * self.precio_boleta("regular")

                # Agregar los datos del evento al reporte
                reporte.append({
                    "nombre_evento": evento.get_nombre(),
                    "boletas_preventa": boletas_por_tipo["preventa"],
                    "boletas_regular": boletas_por_tipo["regular"],
                    "boletas_cortesia": boletas_por_tipo["cortesia"],
                    "ingresos_preventa": ingresos_preventa,
                    "ingresos_regular": ingresos_regular,
                    "ingresos_totales": ingresos_preventa + ingresos_regular
                })

        # Convertir la lista de datos del reporte en un DataFrame de pandas
        df_reporte = pd.DataFrame(reporte)

        # Retornar el DataFrame
        return df_reporte

    def generar_reporte_financiero(self, nombre_evento, tipo_evento):

        """
        Generates a financial report for a specific event.

        This function creates a report containing various financial details for a specific event. The report includes the total income from ticket sales (categorized by ticket type and payment method), total payments to artists, rental payments, gross profit, retained earnings, and net profit. The report is returned as a pandas DataFrame.

        Parameters:
        nombre_evento (str): The name of the event for which the report is to be generated.
        tipo_evento (str): The type of the event (Bar, Theater, Philanthropic).

        Returns:
        df_reporte (DataFrame): A pandas DataFrame containing the report data.
        """

        # Crear un diccionario para almacenar los datos del reporte
        reporte = {
            "preventa_efectivo": 0,
            "preventa_tarjeta": 0,
            "regular_efectivo": 0,
            "regular_tarjeta": 0,
            "ingresos_totales": 0,
            "pago_artistas": 0,
            "pago_alquiler": 0,
            "utilidad_bruta": 0,
            "utilidad_retenida": 0,
            "utilidad_neta": 0
        }

        # Seleccionar la lista de eventos según el tipo de evento
        eventos = []

        if tipo_evento == "Bar":
            eventos = self.bares
        elif tipo_evento == "Teatro":
            eventos = self.teatros
        elif tipo_evento == "Filantropico":
            eventos = self.filantropicos

        # Buscar el evento con el nombre dado
        evento_seleccionado = None
        for evento in eventos:
            if evento.get_nombre() == nombre_evento:
                evento_seleccionado = evento
                break

        # Si se encontró el evento, generar el reporte
        if evento_seleccionado is not None:
            # Obtener las boletas del evento
            boletas = evento_seleccionado.get_boleteria()
            # Iterar sobre las boletas
            for boleta in boletas:
                # Clasificar las boletas por tipo de boleteria y metodo de pago
                tipo_boleteria = boleta.get_tipo_boleteria()
                metodo_pago = boleta.get_metodo_pago()
                # Sumar los ingresos correspondientes
                if tipo_boleteria == "preventa" and metodo_pago == "efectivo":
                    reporte["preventa_efectivo"] += self.precio_boleta("preventa")
                elif tipo_boleteria == "preventa" and metodo_pago == "tarjeta":
                    reporte["preventa_tarjeta"] += self.precio_boleta("preventa")
                elif tipo_boleteria == "regular" and metodo_pago == "efectivo":
                    reporte["regular_efectivo"] += self.precio_boleta("regular")
                elif tipo_boleteria == "regular" and metodo_pago == "tarjeta":
                    reporte["regular_tarjeta"] += self.precio_boleta("regular")

            # Sumar los pagos a los artistas y el alquiler del lugar


            # Calcular los ingresos totales

            reporte["ingresos_totales"] = sum(reporte.values())

            reporte["pago_artistas"] = evento_seleccionado.get_pago_artistas()
            reporte["pago_alquiler"] = evento_seleccionado.get_pago_alquiler()
            # Calcular la utilidad bruta
            reporte["utilidad_bruta"] = reporte["ingresos_totales"] - reporte["pago_artistas"] - reporte[
                "pago_alquiler"]

            # Calcular la utilidad retenida y la utilidad neta
            if tipo_evento == "Bar":
                reporte["utilidad_retenida"] = reporte["utilidad_bruta"] * 0.20
            elif tipo_evento == "Teatro":
                reporte["utilidad_retenida"] = reporte["utilidad_bruta"] * 0.07
            reporte["utilidad_neta"] = reporte["utilidad_bruta"] - reporte["utilidad_retenida"]

        # Convertir el reporte a un DataFrame de pandas
        df_reporte = pd.DataFrame([reporte])

        # Retornar el DataFrame
        return df_reporte

    def generar_reporte_compradores(self, nombre_evento, tipo_evento):

        """
        Generates a report of buyers for a specific event.

        This function creates a report containing the details of each buyer for a specific event. The report includes the buyer's name, age, address, how they heard about the event, the type of ticket they bought, and whether their attendance has been confirmed. The report is returned as a pandas DataFrame.

        Parameters:
        nombre_evento (str): The name of the event for which the report is to be generated.
        tipo_evento (str): The type of the event (Bar, Theater, Philanthropic).

        Returns:
        df (DataFrame): A pandas DataFrame containing the report data.
        """

        # Crear una lista para almacenar los datos de cada comprador
        datos = []

        # Seleccionar la lista de eventos basado en el tipo de evento
        eventos = []
        if tipo_evento == "Bar":
            eventos = self.bares
        elif tipo_evento == "Teatro":
            eventos = self.teatros
        elif tipo_evento == "Filantropico":
            eventos = self.filantropicos

        # Encontrar el evento con el nombre dado
        evento_seleccionado = None
        for evento in eventos:
            if evento.get_nombre() == nombre_evento:
                evento_seleccionado = evento
                break

        # Si se encontró el evento, generar el informe
        if evento_seleccionado is not None:
            # Obtener los asistentes del evento
            asistentes = evento_seleccionado.get_asistentes()
            # Iterar sobre los asistentes
            for asistente in asistentes:
                # Agregar los detalles del asistente a los datos
                datos.append(
                    [asistente.get_nombre(), asistente.get_apellido(), asistente.get_edad(), asistente.get_direccion(),
                     asistente.get_medio_enterado(), asistente.get_boletas_compradas(), asistente.get_confirmacion()])

        # Crear un DataFrame con los datos
        df = pd.DataFrame(datos, columns=["Nombre", "Apellido", "Edad", "Direccion", "Medio Enterado", "Boletas compradas", "Asistencia confirmada"])

        # Devolver el DataFrame
        return df

    def generar_reporte_artistas(self, nombre_artista):
        # Initialize the report data
        """
        Generates a report for a given artist.

        This function creates a report containing the total payment received by the artist and the number of events
        the artist has participated in, categorized by event type (Bar, Theater, Philanthropic). The report is returned
        as a pandas DataFrame.

        Parameters:
        nombre_artista (str): The name of the artist for whom the report is to be generated.

        Returns:
        df_reporte (DataFrame): A pandas DataFrame containing the report data.
        """

        reporte = {
            "nombre_artista": nombre_artista,
            "total_por_pago": 0,
            "eventos_bar": 0,
            "eventos_teatro": 0,
            "eventos_filantropico": 0
        }

        # Check if the artist exists
        if nombre_artista not in self.artistas:
            return None

        # Get the artist
        artista = self.artistas[nombre_artista]

        # Iterate over the artist's events
        for tipo_evento, nombres_eventos in artista.eventos.items():
            for nombre_evento in nombres_eventos:
                # Find the event object corresponding to the event name
                evento = None
                if tipo_evento == "Bar":
                    for bar in self.bares:
                        if bar.get_nombre() == nombre_evento:
                            evento = bar
                            break
                elif tipo_evento == "Teatro":
                    for teatro in self.teatros:
                        if teatro.get_nombre() == nombre_evento:
                            evento = teatro
                            break
                elif tipo_evento == "Filantropico":
                    for filantropico in self.filantropicos:
                        if filantropico.get_nombre() == nombre_evento:
                            evento = filantropico
                            break

                # If the event object is found, add its payment to the total
                if evento is not None:
                    reporte["total_por_pago"] += evento.get_pago_artistas()
                    if tipo_evento == "Bar":
                        reporte["eventos_bar"] += 1
                    elif tipo_evento == "Teatro":
                        reporte["eventos_teatro"] += 1
                    elif tipo_evento == "Filantropico":
                        reporte["eventos_filantropico"] += 1

        # Convert the report data to a DataFrame
        df_reporte = pd.DataFrame([reporte])

        return df_reporte
    def asignar_patrocinadores(self, nombre_evento, nombre_patrocinador, donacion_patrocinador):
        """
        Assigns a sponsor to a philanthropic event.

        This function iterates over the list of philanthropic events. If it finds an event with the given name, it assigns the sponsor with the given name and donation amount to the event. The function returns True if the sponsor was successfully assigned, and False otherwise.

        Parameters:
        nombre_evento (str): The name of the philanthropic event.
        nombre_patrocinador (str): The name of the sponsor.
        donacion_patrocinador (float): The donation amount from the sponsor.

        Returns:
        bool: True if the sponsor was successfully assigned, False otherwise.
        """
        for evento in self.filantropicos:
            if evento.get_nombre() == nombre_evento:
                evento.asignar_patrocinador(nombre_patrocinador, donacion_patrocinador)
                return True
        return False
    def patrocinadores_evento(self, nombre_evento):
        """
        Returns the sponsors of a philanthropic event.

        This function iterates over the list of philanthropic events. If it finds an event with the given name, it returns the sponsors of the event. If no matching event is found, it returns None.

        Parameters:
        nombre_evento (str): The name of the philanthropic event.

        Returns:
        list: The sponsors of the event if found, None otherwise.
        """
        for evento in self.filantropicos:
            if evento.get_nombre() == nombre_evento:
                return evento.get_patrocinadores()
        return None