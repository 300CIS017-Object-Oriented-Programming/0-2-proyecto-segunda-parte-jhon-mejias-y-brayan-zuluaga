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
    def fase_ventas(self):
        """
        This method is used to update the sales phase of an event. It asks the user for the type and name of the event,
        and the new sales phase. If the event is found, it updates the sales phase.
        """

        tipo_evento = input("Ingrese el tipo de evento (bar, teatro, filantropico): ")
        nombre_evento = input("Ingrese el nombre del evento: ")
        nueva_fase = input("Ingrese la nueva fase de ventas: ")

        evento_encontrado = False
        if tipo_evento == "bar":
            for bar in self.bares:
                if bar.nombre == nombre_evento:
                    bar.set_fase_ventas(nueva_fase)
                    print("La fase de ventas del evento Bar se ha actualizado correctamente.")
                    evento_encontrado = True
                    break
        elif tipo_evento == "teatro":
            for teatro in self.teatros:
                if teatro.nombre == nombre_evento:
                    teatro.set_fase_ventas(nueva_fase)
                    print("La fase de ventas del evento Teatro se ha actualizado correctamente.")
                    evento_encontrado = True
                    break
        elif tipo_evento == "filantropico":
            for filantropico in self.filantropicos:
                if filantropico.nombre == nombre_evento:
                    filantropico.set_fase_ventas(nueva_fase)
                    print("La fase de ventas del evento Filantropico se ha actualizado correctamente.")
                    evento_encontrado = True
                    break

        if not evento_encontrado:
            print("Error: El evento no existe.")

    def generar_ventas(self):
        """
        This method generates a sales report for a specific event. It asks the user for the type and name of the event.
        If the event is found, it calculates the income from pre-sale and regular tickets and prints the report.
        """
        tipo_evento = input("Ingrese el tipo de evento (Filantropico, Bar o Teatro): ")
        nombre_evento = input("Ingrese el nombre del evento para generar el reporte de ventas de boletas: ")

        evento_seleccionado = None
        if tipo_evento.lower() == "filantropico":
            evento_seleccionado = next((f for f in self.filantropicos if f.nombre == nombre_evento), None)
        elif tipo_evento.lower() == "bar":
            evento_seleccionado = next((b for b in self.bares if b.nombre == nombre_evento), None)
        elif tipo_evento.lower() == "teatro":
            evento_seleccionado = next((t for t in self.teatros if t.nombre == nombre_evento), None)

        if evento_seleccionado:
            precio_preventa = evento_seleccionado.precio_preventa
            precio_regular = evento_seleccionado.precio_regular
            cantidad_asistentes = evento_seleccionado.cantidad_asistentes()

            ingresos_preventa = cantidad_asistentes * precio_preventa
            ingresos_regular = cantidad_asistentes * precio_regular
            ingresos_totales = ingresos_preventa + ingresos_regular

            print("Reporte de Ventas de Boletas para el evento '{}'\n"
                  "------------------------------------------------------\n"
                  "Total de boletas vendidas: {}\n"
                  "Total de ingresos: ${}\n"
                  "Ingresos por preventa: ${}\n"
                  "Ingresos por venta regular: ${}".format(nombre_evento, cantidad_asistentes, ingresos_totales,
                                                            ingresos_preventa, ingresos_regular))
        else:
            print("No se encontró ningún evento con el nombre ingresado.")

    def generar_financiero(self):
        """
        This method generates a financial report for a specific event. It asks the user for the type and name of the event.
        If the event is found, it calculates the income from pre-sale and regular tickets, separated by payment method,
        and prints the report.
        """

        tipo_evento = input("Ingrese el tipo de evento (Filantropico, Bar o Teatro): ")
        nombre_evento = input("Ingrese el nombre del evento para generar el reporte financiero: ")

        evento_seleccionado = None
        if tipo_evento.lower() == "filantropico":
            evento_seleccionado = next((f for f in self.filantropicos if f.nombre == nombre_evento), None)
        elif tipo_evento.lower() == "bar":
            evento_seleccionado = next((b for b in self.bares if b.nombre == nombre_evento), None)
        elif tipo_evento.lower() == "teatro":
            evento_seleccionado = next((t for t in self.teatros if t.nombre == nombre_evento), None)

        if evento_seleccionado:
            ingresos_preventa_efectivo = 0
            ingresos_preventa_tarjeta = 0
            ingresos_regular_efectivo = 0
            ingresos_regular_tarjeta = 0

            for boleteria in evento_seleccionado.boleterias:
                if boleteria.tipo_boleteria == "preventa":
                    if boleteria.metodo_pago == "efectivo":
                        ingresos_preventa_efectivo += boleteria.precio
                    elif boleteria.metodo_pago == "tarjeta":
                        ingresos_preventa_tarjeta += boleteria.precio
                elif boleteria.tipo_boleteria == "regular":
                    if boleteria.metodo_pago == "efectivo":
                        ingresos_regular_efectivo += boleteria.precio
                    elif boleteria.metodo_pago == "tarjeta":
                        ingresos_regular_tarjeta += boleteria.precio

            print("Reporte Financiero para el evento '{}'\n"
                  "-----------------------------------------------------------\n"
                  "Ingresos por tipo de boleteria:\n"
                  "  - Preventa (Efectivo): ${}\n"
                  "  - Preventa (Tarjeta): ${}\n"
                  "  - Regular (Efectivo): ${}\n"
                  "  - Regular (Tarjeta): ${}".format(nombre_evento, ingresos_preventa_efectivo,
                                                      ingresos_preventa_tarjeta, ingresos_regular_efectivo,
                                                      ingresos_regular_tarjeta))
        else:
            print("No se encontró ningún evento con el nombre ingresado.")

    def generar_compradores(self):
        """
        This method generates a report of the buyers for a specific event. It asks the user for the type and name of the event.
        If the event is found, it prints the details of each buyer.
        """
        tipo_evento = input("Ingrese el tipo de evento (Filantropico, Bar o Teatro): ")
        tipo_evento = input("Ingrese el tipo de evento (Filantropico, Bar o Teatro): ")
        nombre_evento = input("Ingrese el nombre del evento para generar el reporte financiero: ")

        evento_seleccionado = None
        if tipo_evento.lower() == "filantropico":
            evento_seleccionado = next((f for f in self.filantropicos if f.nombre == nombre_evento), None)
        elif tipo_evento.lower() == "bar":
            evento_seleccionado = next((b for b in self.bares if b.nombre == nombre_evento), None)
        elif tipo_evento.lower() == "teatro":
            evento_seleccionado = next((t for t in self.teatros if t.nombre == nombre_evento), None)

        if evento_seleccionado:
            asistentes = evento_seleccionado.asistentes

            print("Reporte de Datos de los Compradores para el evento '{}'\n"
                  "--------------------------------------------------------------------\n".format(nombre_evento))
            for asistente in asistentes:
                print("Nombre: {}\n"
                      "Apellido: {}\n"
                      "Edad: {}\n"
                      "Direccion: {}\n"
                      "Medio por el que se entero: {}\n".format(asistente.nombre, asistente.apellido,
                                                                 asistente.edad, asistente.direccion,
                                                                 asistente.medio_enterado))
        else:
            print("No se encontró ningún evento con el nombre ingresado.")

    def generar_artistas(self):
        # Solicitar al usuario el nombre del artista
        nombre_artista = input("Ingrese el nombre del artista para generar el reporte de datos por artista: ")
        porcentaje_aforo = 0.0
        artista_encontrado = False

        # Iterar sobre los eventos filantrópicos
        for evento in self.filantropicos:
            artistas_evento = evento.get_artistas()
            if nombre_artista in artistas_evento:
                artista_encontrado = True
                porcentaje_aforo = (evento.get_personas() / evento.get_aforo()) * 100.0
                # Mostrar datos relevantes del evento
                print("Evento:", evento.get_nombre())
                print("Fecha:", evento.get_fecha())
                print("Lugar:", evento.get_lugar())
                print("Cantidad de boletas vendidas:", evento.get_personas())
                print("Porcentaje de aforo cubierto:", porcentaje_aforo)
                print()

        # Iterar sobre los eventos de bares
        for evento in self.bares:
            artistas_evento = evento.get_artistas()
            if nombre_artista in artistas_evento:
                artista_encontrado = True
                porcentaje_aforo = (evento.get_personas() / evento.get_aforo()) * 100.0
                # Mostrar datos relevantes del evento
                print("Evento:", evento.get_nombre())
                print("Fecha:", evento.get_fecha())
                print("Lugar:", evento.get_lugar())
                print("Cantidad de boletas vendidas:", evento.get_personas())
                print("Porcentaje de aforo cubierto:", porcentaje_aforo)
                print()

        # Iterar sobre los eventos de teatros
        for evento in self.teatros:
            artistas_evento = evento.get_artistas()
            if nombre_artista in artistas_evento:
                artista_encontrado = True
                porcentaje_aforo = (evento.get_personas() / evento.get_aforo()) * 100.0
                # Mostrar datos relevantes del evento
                print("Evento:", evento.get_nombre())
                print("Fecha:", evento.get_fecha())
                print("Lugar:", evento.get_lugar())
                print("Cantidad de boletas vendidas:", evento.get_personas())
                print("Porcentaje de aforo cubierto:", porcentaje_aforo)
                print()

        # Verificar si se encontró el artista en algún evento
        if not artista_encontrado:
            print("No se encontró ningún evento con el artista ingresado.")


    def crear_bar(self, nombre, fecha, hora_inicio, hora_show, lugar, direccion, ciudad, estado, aforo, pago_artistas):
        bar = Bar(nombre, fecha, hora_inicio, hora_show, lugar, direccion, ciudad, estado, aforo, pago_artistas)
        self.bares.append(bar)

    def crear_teatro(self, nombre, fecha, hora_inicio, hora_show, lugar, direccion, ciudad, estado, aforo, costo):
        teatro = Teatro(nombre, fecha, hora_inicio, hora_show, lugar, direccion, ciudad, estado, aforo)
        teatro.costo = costo
        self.teatros.append(teatro)

    def crear_filantropico(self, nombre, fecha, hora_inicio, hora_show, lugar, direccion, ciudad, estado, aforo,
                           patrocinadores):
        filantropico = Filantropico(nombre, fecha, hora_inicio, hora_show, lugar, direccion, ciudad, estado, aforo)

        # Dividir el string de patrocinadores en una lista de patrocinadores individuales
        lista_patrocinadores = patrocinadores.split(',')

        # Iterar sobre la lista de patrocinadores y agregar cada uno al diccionario de patrocinadores
        for patrocinador in lista_patrocinadores:
            patrocinador = patrocinador.strip()  # Eliminar espacios en blanco al principio y al final
            filantropico.agregar_patrocinador(patrocinador)

        self.filantropicos.append(filantropico)


    def editar_evento(self):
        tipo_evento = input("Ingrese el tipo de evento a editar (bar, teatro, filantropico): ")
        nombre_evento = input("Ingrese el nombre del evento a editar: ")

        evento_encontrado = False
        if tipo_evento == "bar" and not evento_encontrado:
            for bar in self.bares:
                if bar.get_nombre() == nombre_evento:
                    # Solicitar los nuevos datos al usuario
                    nuevo_nombre = input("Ingrese el nuevo nombre del evento: ")
                    nueva_fecha = input("Ingrese la nueva fecha del evento: ")
                    nueva_hora_inicio = input("Ingrese la nueva hora de inicio del evento: ")
                    nueva_hora_show = input("Ingrese la nueva hora del show del evento: ")
                    nuevo_lugar = input("Ingrese el nuevo lugar del evento: ")
                    nueva_direccion = input("Ingrese la nueva dirección del evento: ")
                    nueva_ciudad = input("Ingrese la nueva ciudad del evento: ")
                    nuevo_estado = input("Ingrese el nuevo estado del evento: ")
                    nuevo_aforo = int(input("Ingrese el nuevo aforo del evento: "))

                    # Actualizar los datos del evento
                    bar.set_nombre(nuevo_nombre)
                    bar.set_fecha(nueva_fecha)
                    bar.set_hora_inicio(nueva_hora_inicio)
                    bar.set_hora_show(nueva_hora_show)
                    bar.set_lugar(nuevo_lugar)
                    bar.set_direccion(nueva_direccion)
                    bar.set_ciudad(nueva_ciudad)
                    bar.set_estado(nuevo_estado)
                    bar.set_aforo(nuevo_aforo)

                    evento_encontrado = True
                    break
        elif tipo_evento == "teatro" and not evento_encontrado:
            for teatro in self.teatros:
                if teatro.get_nombre() == nombre_evento:
                    # Solicitar los nuevos datos al usuario
                    nuevo_nombre = input("Ingrese el nuevo nombre del evento: ")
                    nueva_fecha = input("Ingrese la nueva fecha del evento: ")
                    nueva_hora_inicio = input("Ingrese la nueva hora de inicio del evento: ")
                    nueva_hora_show = input("Ingrese la nueva hora del show del evento: ")
                    nuevo_lugar = input("Ingrese el nuevo lugar del evento: ")
                    nueva_direccion = input("Ingrese la nueva dirección del evento: ")
                    nueva_ciudad = input("Ingrese la nueva ciudad del evento: ")
                    nuevo_estado = input("Ingrese el nuevo estado del evento: ")
                    nuevo_aforo = int(input("Ingrese el nuevo aforo del evento: "))

                    # Actualizar los datos del evento
                    teatro.set_nombre(nuevo_nombre)
                    teatro.set_fecha(nueva_fecha)
                    teatro.set_hora_inicio(nueva_hora_inicio)
                    teatro.set_hora_show(nueva_hora_show)
                    teatro.set_lugar(nuevo_lugar)
                    teatro.set_direccion(nueva_direccion)
                    teatro.set_ciudad(nueva_ciudad)
                    teatro.set_estado(nuevo_estado)
                    teatro.set_aforo(nuevo_aforo)

                    evento_encontrado = True
                    break
        elif tipo_evento == "filantropico" and not evento_encontrado:
            for filantropico in self.filantropicos:
                if filantropico.get_nombre() == nombre_evento:
                    # Solicitar los nuevos datos al usuario
                    nuevo_nombre = input("Ingrese el nuevo nombre del evento: ")
                    nueva_fecha = input("Ingrese la nueva fecha del evento: ")
                    nueva_hora_inicio = input("Ingrese la nueva hora de inicio del evento: ")
                    nueva_hora_show = input("Ingrese la nueva hora del show del evento: ")
                    nuevo_lugar = input("Ingrese el nuevo lugar del evento: ")
                    nueva_direccion = input("Ingrese la nueva dirección del evento: ")
                    nueva_ciudad = input("Ingrese la nueva ciudad del evento: ")
                    nuevo_estado = input("Ingrese el nuevo estado del evento: ")
                    nuevo_aforo = int(input("Ingrese el nuevo aforo del evento: "))

                    # Actualizar los datos del evento
                    filantropico.set_nombre(nuevo_nombre)
                    filantropico.set_fecha(nueva_fecha)
                    filantropico.set_hora_inicio(nueva_hora_inicio)
                    filantropico.set_hora_show(nueva_hora_show)
                    filantropico.set_lugar(nuevo_lugar)
                    filantropico.set_direccion(nueva_direccion)
                    filantropico.set_ciudad(nueva_ciudad)
                    filantropico.set_estado(nuevo_estado)
                    filantropico.set_aforo(nuevo_aforo)

                    evento_encontrado = True
                    break

        if not evento_encontrado:
            print("Error: El evento a editar no existe.")

    def eliminar_evento(self, tipo_evento, nombre_evento):

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

    def crear_artista(self, nombre, tipo_artista):
        if nombre in self.artistas:
            return False
        else:
            nuevo_artista = Artista(nombre, tipo_artista)
            self.artistas[nombre] = nuevo_artista
            return True
    def asignar_artista(self, tipo_evento, nombre_evento, nombre_artista):
        evento_encontrado = False
        if tipo_evento == "bar":
            for bar in self.bares:
                if bar.get_nombre() == nombre_evento:
                    if nombre_artista in self.artistas:
                        bar.asignar_artista(nombre_artista, self.artistas[nombre_artista])
                        self.artistas[nombre_artista].agregar_nombre_evento(nombre_evento)
                        return True
                    else:
                        return False
                    evento_encontrado = True
                    break
        elif tipo_evento == "teatro":
            for teatro in self.teatros:
                if teatro.get_nombre() == nombre_evento:
                    if nombre_artista in self.artistas:
                        teatro.asignar_artista(nombre_artista, self.artistas[nombre_artista])
                        self.artistas[nombre_artista].agregar_nombre_evento(nombre_evento)
                        return True
                    else:
                        return False
                    evento_encontrado = True
                    break
        elif tipo_evento == "filantropico":
            for filantropico in self.filantropicos:
                if filantropico.get_nombre() == nombre_evento:
                    if nombre_artista in self.artistas:
                        filantropico.asignar_artista(nombre_artista, self.artistas[nombre_artista])
                        self.artistas[nombre_artista].agregar_nombre_evento(nombre_evento)
                        return True
                    else:
                        return False
                    evento_encontrado = True
                    break

        if not evento_encontrado:
            return False

    def mostrar_detalles_evento(self, tipo_evento, nombre_evento):
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

    def imprimir_eventos(self):
        print("Eventos de tipo Bar:")
        for bar in self.bares:
            print(bar.get_nombre())

        print("Eventos de tipo Teatro:")
        for teatro in self.teatros:
            print(teatro.get_nombre())

        print("Eventos de tipo Filantropico:")
        for filantropico in self.filantropicos:
            print(filantropico.get_nombre())

    def crear_artista(self, nombre, tipo_artista):
        if nombre in self.artistas:
            return False
        else:
            nuevo_artista = Artista(nombre, tipo_artista)
            self.artistas[nombre] = nuevo_artista
            return True

    def asignar_artistas(self, tipo_evento, nombre_evento, nombre_artista):

        if tipo_evento == "bar":
            for bar in self.bares:
                if bar.get_nombre() == nombre_evento:
                    if nombre_artista in self.artistas:
                        bar.asignar_artista(nombre_artista, self.artistas[nombre_artista])
                        self.artistas[nombre_artista].agregar_nombre_evento(nombre_evento)
                        return True
                    else:
                        return False

        elif tipo_evento == "teatro":
            for teatro in self.teatros:
                if teatro.get_nombre() == nombre_evento:
                    if nombre_artista in self.artistas:
                        teatro.asignar_artista(nombre_artista, self.artistas[nombre_artista])
                        self.artistas[nombre_artista].agregar_nombre_evento(nombre_evento)
                        return True
                    else:
                        return False
        elif tipo_evento == "filantropico":
            for filantropico in self.filantropicos:
                if filantropico.get_nombre() == nombre_evento:
                    if nombre_artista in self.artistas:
                        filantropico.asignar_artista(nombre_artista, self.artistas[nombre_artista])
                        self.artistas[nombre_artista].agregar_nombre_evento(nombre_evento)
                        return True
                    else:
                        return False


    def imprimir_eventos(self):
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


    def buscar_evento(self, tipo_evento, nombre_evento):
        if tipo_evento.lower() == "filantropico":
            for evento in self.filantropicos:
                if evento.get_nombre() == nombre_evento:
                    return evento
        elif tipo_evento.lower() == "bar":
            for evento in self.bares:
                if evento.get_nombre() == nombre_evento:
                    return evento
        elif tipo_evento.lower() == "teatro":
            for evento in self.teatros:
                if evento.get_nombre() == nombre_evento:
                    return evento
        return None

    def registrar_ingreso(self, nombre_evento, tipo_evento, nombre_asistente):
        if tipo_evento == "Filantropico":
            for filantropico in self.filantropicos:
                if filantropico.get_nombre() == nombre_evento:
                    for a in filantropico.asistentes:
                        if a.getNombre() == nombre_asistente:
                            a.confirmacion = True
                            return True
        elif tipo_evento == "Bar":
            for bar in self.bares:
                if bar.get_nombre() == nombre_evento:
                    for a in bar.asistentes:
                        if a.getNombre() == nombre_asistente:
                            a.confirmacion = True
                            return True
        elif tipo_evento == "Teatro":
            for teatro in self.teatros:
                if teatro.get_nombre() == nombre_evento:
                    for a in teatro.asistentes:
                        if a.getNombre() == nombre_asistente:
                            a.confirmacion = True
                            return True
        return False

    def boletas_vendidas(self):
        # Retorna el diccionario de boletas vendidas
        return self.boletas_vendidas

    def generar_reporte_ventas(self, nombre_evento, tipo_evento):
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
        # Crear un diccionario para almacenar los datos del reporte
        reporte = {"preventa_efectivo": 0, "preventa_tarjeta": 0, "regular_efectivo": 0, "regular_tarjeta": 0, "ingresos_totales": 0}

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

            reporte["ingresos_totales"] += sum(reporte.values())

        # Convertir el reporte a un DataFrame de pandas
        df_reporte = pd.DataFrame([reporte])

        # Retornar el DataFrame
        return df_reporte

    def generar_reporte_compradores(self, nombre_evento, tipo_evento):
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
                     asistente.get_medio_enterado()])

        # Crear un DataFrame con los datos
        df = pd.DataFrame(datos, columns=["Nombre", "Apellido", "Edad", "Direccion", "Medio Enterado"])

        # Devolver el DataFrame
        return df

    def generar_reporte_artistas(self, nombre_artista):
        # Implementa la lógica para generar el reporte de artistas aquí
        pass