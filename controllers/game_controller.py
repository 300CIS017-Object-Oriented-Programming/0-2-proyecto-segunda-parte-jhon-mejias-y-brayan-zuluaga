from typing import List, Dict
from models.Filantropico import Filantropico
from models.Bar import Bar
from models.Teatro import Teatro
from models.Artista import Artista
from models.Asistente import Asistente
from models.Boleteria import Boleteria




class AdministrarEventos:
    def __init__(self):
        self.filantropicos: List[Filantropico] = []
        self.bares: List[Bar] = []
        self.teatros: List[Teatro] = []
        self.artistas: Dict[str, Artista] = {}

    def fase_ventas(self):
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

    def crear_teatro(self, nombre, fecha, hora_inicio, hora_show, lugar, direccion, ciudad, estado, aforo):
        teatro = Teatro(nombre, fecha, hora_inicio, hora_show, lugar, direccion, ciudad, estado, aforo)
        teatro.costo_alquiler()
        self.teatros.append(teatro)
    def crear_filantropico(self, nombre, fecha, hora_inicio, hora_show, lugar, direccion, ciudad, estado, aforo):
        filantropico = Filantropico(nombre, fecha, hora_inicio, hora_show, lugar, direccion, ciudad, estado, aforo)
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

    def eliminar_evento(self):
        tipo_evento = input("Ingress el tipo de evento (bar, teatro, filantropico): ")
        nombre_evento = input("Ingrese el nombre del evento: ")

        evento_encontrado = False
        if tipo_evento == "bar" and not evento_encontrado:
            for evento in self.bares:
                if evento.get_nombre() == nombre_evento:
                    if evento.get_cantidad_asistentes() == evento.get_aforo():
                        print("No se puede eliminar el evento, el número de asistentes es igual al aforo.")
                    else:
                        self.bares.remove(evento)
                        del evento
                        print("Evento Bar eliminado correctamente.")
                    evento_encontrado = True
                    break
        elif tipo_evento == "teatro" and not evento_encontrado:
            for evento in self.teatros:
                if evento.get_nombre() == nombre_evento:
                    if evento.get_cantidad_asistentes() == evento.get_aforo():
                        print("No se puede eliminar el evento, el número de asistentes es igual al aforo.")
                    else:
                        self.teatros.remove(evento)
                        del evento
                        print("Evento Teatro eliminado correctamente.")
                    evento_encontrado = True
                    break
        elif tipo_evento == "filantropico" and not evento_encontrado:
            for evento in self.filantropicos:
                if evento.get_nombre() == nombre_evento:
                    if evento.get_cantidad_asistentes() == evento.get_aforo():
                        print("No se puede eliminar el evento Filantropico porque ya ha alcanzado su aforo máximo.")
                    else:
                        self.filantropicos.remove(evento)
                        del evento
                        print("Evento Filantropico eliminado correctamente.")
                    evento_encontrado = True
                    break

        if not evento_encontrado:
            print("Error: El evento no existe.")

    def vender_boletas(self):
        evento_encontrado = False
        tipo_evento = input("Ingrese el tipo de evento (Filantropico, Bar o Teatro): ")
        nombre_evento = input("Ingrese el nombre del evento para comprar boleta: ")

        evento_seleccionado = None

        if tipo_evento == "Filantropico" and not evento_encontrado:
            for evento in self.filantropicos:
                if evento.get_nombre() == nombre_evento:
                    evento_seleccionado = evento
                    evento_encontrado = True
                    break
        elif tipo_evento == "Bar" and not evento_encontrado:
            for evento in self.bares:
                if evento.get_nombre() == nombre_evento:
                    evento_seleccionado = evento
                    evento_encontrado = True
                    break
        elif tipo_evento == "Teatro" and not evento_encontrado:
            for evento in self.teatros:
                if evento.get_nombre() == nombre_evento:
                    evento_seleccionado = evento
                    evento_encontrado = True
                    break
        else:
            print("Tipo de evento no válido.")
            return

        if evento_seleccionado is None:
            print("No se encontró ningún evento con el nombre ingresado.")
            return

        if evento_seleccionado.get_cantidad_asistentes() < evento_seleccionado.get_aforo():
            nombre_asistente = input("Ingrese el nombre del asistente: ")
            apellido_asistente = input("Ingrese el apellido del asistente: ")
            edad = int(input("Ingrese la edad del asistente: "))
            direccion = input("Ingrese la dirección del asistente: ")
            medio_enterado = input("Cómo se enteró del evento? ")
            tipo_boleteria = input("Ingrese el tipo de boleteria si es preventa o regular: ")
            metodo_pago = input("Ingrese el método de pago: ")

            nuevo_asistente = Asistente(nombre_asistente, apellido_asistente, edad, direccion, medio_enterado)
            evento_seleccionado.agregar_asistente(nuevo_asistente)
            evento_seleccionado.sumar_personas()

            nueva_boleteria = Boleteria(tipo_boleteria, evento_seleccionado.get_precio_preventa(), evento_seleccionado.get_precio_regular(), metodo_pago)
            evento_seleccionado.agregar_boleteria(nueva_boleteria)

            print("Boleta vendida correctamente para el evento '{}'.".format(nombre_evento))
        else:
            print("El evento '{}' ha alcanzado su aforo máximo.".format(nombre_evento))

    def crear_artista(self):
        nombre = input("Ingrese el nombre del artista: ")
        tipo_artista = input("Ingrese el tipo de artista: ")

        if nombre in self.artistas:
            print("Error: El artista ya existe.")
        else:
            nuevo_artista = Artista(nombre, tipo_artista)
            self.artistas[nombre] = nuevo_artista
            print("Artista creado exitosamente.")

    def asignar_artista(self):
        tipo_evento = input("Ingrese el tipo de evento (bar, teatro, filantropico): ")
        nombre_evento = input("Ingrese el nombre del evento: ")
        nombre_artista = input("Ingrese el nombre del artista: ")

        evento_encontrado = False
        if tipo_evento == "bar":
            for bar in self.bares:
                if bar.get_nombre() == nombre_evento:
                    if nombre_artista in self.artistas:
                        bar.asignar_artista(nombre_artista, self.artistas[nombre_artista])
                        self.artistas[nombre_artista].agregar_nombre_evento(nombre_evento)
                        print("Artista asignado correctamente al evento Bar.")
                    else:
                        print("Error: El artista no existe.")
                    evento_encontrado = True
                    break
        elif tipo_evento == "teatro":
            for teatro in self.teatros:
                if teatro.get_nombre() == nombre_evento:
                    if nombre_artista in self.artistas:
                        teatro.asignar_artista(nombre_artista, self.artistas[nombre_artista])
                        self.artistas[nombre_artista].agregar_nombre_evento(nombre_evento)
                        print("Artista asignado correctamente al evento Teatro.")
                    else:
                        print("Error: El artista no existe.")
                    evento_encontrado = True
                    break
        elif tipo_evento == "filantropico":
            for filantropico in self.filantropicos:
                if filantropico.get_nombre() == nombre_evento:
                    if nombre_artista in self.artistas:
                        filantropico.asignar_artista(nombre_artista, self.artistas[nombre_artista])
                        self.artistas[nombre_artista].agregar_nombre_evento(nombre_evento)
                        print("Artista asignado correctamente al evento Filantropico.")
                    else:
                        print("Error: El artista no existe.")
                    evento_encontrado = True
                    break

        if not evento_encontrado:
            print("Error: El evento no existe.")

    def mostrar_detalles_evento(self):
        tipo_evento = input("Ingrese el tipo de evento (bar, teatro, filantropico): ")

        evento_encontrado = False
        if tipo_evento == "bar":
            nombre_evento = input("Ingrese el nombre del evento Bar: ")
            for bar in self.bares:
                if bar.get_nombre() == nombre_evento:
                    bar.mostrar_detalles()
                    evento_encontrado = True
                    break
        elif tipo_evento == "teatro":
            nombre_evento = input("Ingrese el nombre del evento Teatro: ")
            for teatro in self.teatros:
                if teatro.get_nombre() == nombre_evento:
                    teatro.mostrar_detalles()
                    evento_encontrado = True
                    break
        elif tipo_evento == "filantropico":
            nombre_evento = input("Ingrese el nombre del evento Filantropico: ")
            for filantropico in self.filantropicos:
                if filantropico.get_nombre() == nombre_evento:
                    filantropico.mostrar_detalles()
                    evento_encontrado = True
                    break
        else:
            print("Tipo de evento no válido.")
            evento_encontrado = True

        if not evento_encontrado:
            print("Error: El evento no existe.")

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

    def crear_artista(self):
        nombre = input("Ingrese el nombre del artista: ")
        tipo_artista = input("Ingrese el tipo de artista: ")

        if nombre in self.artistas:
            print("Error: El artista ya existe.")
        else:
            nuevo_artista = Artista(nombre, tipo_artista)
            self.artistas[nombre] = nuevo_artista
            print("Artista creado exitosamente.")

    def asignar_artista(self):
        tipo_evento = input("Ingrese el tipo de evento (bar, teatro, filantropico): ")
        nombre_evento = input("Ingrese el nombre del evento: ")
        nombre_artista = input("Ingrese el nombre del artista: ")

        evento_encontrado = False
        if tipo_evento == "bar":
            for bar in self.bares:
                if bar.get_nombre() == nombre_evento:
                    if nombre_artista in self.artistas:
                        bar.asignar_artista(nombre_artista, self.artistas[nombre_artista])
                        self.artistas[nombre_artista].agregar_nombre_evento(nombre_evento)
                        print("Artista asignado correctamente al evento Bar.")
                    else:
                        print("Error: El artista no existe.")
                    evento_encontrado = True
                    break
        elif tipo_evento == "teatro":
            for teatro in self.teatros:
                if teatro.get_nombre() == nombre_evento:
                    if nombre_artista in self.artistas:
                        teatro.asignar_artista(nombre_artista, self.artistas[nombre_artista])
                        self.artistas[nombre_artista].agregar_nombre_evento(nombre_evento)
                        print("Artista asignado correctamente al evento Teatro.")
                    else:
                        print("Error: El artista no existe.")
                    evento_encontrado = True
                    break
        elif tipo_evento == "filantropico":
            for filantropico in self.filantropicos:
                if filantropico.get_nombre() == nombre_evento:
                    if nombre_artista in self.artistas:
                        filantropico.asignar_artista(nombre_artista, self.artistas[nombre_artista])
                        self.artistas[nombre_artista].agregar_nombre_evento(nombre_evento)
                        print("Artista asignado correctamente al evento Filantropico.")
                    else:
                        print("Error: El artista no existe.")
                    evento_encontrado = True
                    break

        if not evento_encontrado:
            print("Error: El evento no existe.")

    def mostrar_detalles_evento(self):
        tipo_evento = input("Ingrese el tipo de evento (bar, teatro, filantropico): ")

        evento_encontrado = False
        if tipo_evento == "bar":
            nombre_evento = input("Ingrese el nombre del evento Bar: ")
            for bar in self.bares:
                if bar.get_nombre() == nombre_evento:
                    bar.mostrar_detalles()
                    evento_encontrado = True
                    break
        elif tipo_evento == "teatro":
            nombre_evento = input("Ingrese el nombre del evento Teatro: ")
            for teatro in self.teatros:
                if teatro.get_nombre() == nombre_evento:
                    teatro.mostrar_detalles()
                    evento_encontrado = True
                    break
        elif tipo_evento == "filantropico":
            nombre_evento = input("Ingrese el nombre del evento Filantropico: ")
            for filantropico in self.filantropicos:
                if filantropico.get_nombre() == nombre_evento:
                    filantropico.mostrar_detalles()
                    evento_encontrado = True
                    break
        else:
            print("Tipo de evento no válido.")
            evento_encontrado = True

        if not evento_encontrado:
            print("Error: El evento no existe.")

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
