# En un gimnasio desean tener una aplicación informática para llevar un control de la gestión de este.
# El gimnasio está abierto las 24 horas del día de lunes a viernes). Este servicio es novedoso para los clientes.
# Dispone de una serie de aparatos de entrenamiento, los cuales, son reservados para sesiones de los clientes.
# Cada sesión tiene una duración de media hora.
# la aplicación deberá poder generar un listado, para un determinado día de la semana (de lunes a viernes), de las horas en las que está ocupado y por qué cliente.
# Una vez al mes se generan todos los recibos de ese mes para los clientes. Se desea poder llevar un control de qué clientes han pagado.
# También se desea poder obtener un listado de clientes que son morosos.
from Aparato import *
from Clientes import *


class Gimnasio:
    def __init__(self):
        self.clientes = []
        self.aparatos = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def agregar_aparato(self, aparato):
        self.aparatos.append(aparato)

    def generar_recibos(self):
        recibos = []
        for cliente in self.clientes:
            recibos.append(f"Recibo para {cliente.nombre}: {'Pagado' if cliente.ha_pagado else 'No pagado'}")
        return recibos

    def listar_morosos(self):
        return [cliente for cliente in self.clientes if not cliente.ha_pagado]


# Crear una instancia del gimnasio
gimnasio = Gimnasio()
aparato = Aparato(1, "Cinta de correr")

# Agregar clientes a través de la instancia del gimnasio
gimnasio.agregar_cliente(Cliente(1, "Juan Perez", True))
gimnasio.agregar_cliente(Cliente(2, "Maria Lopez", False))
gimnasio.agregar_cliente(Cliente(3, "Pedro Gutierrez", True))

gimnasio.agregar_aparato(Aparato(1, "Cinta de correr"))
gimnasio.agregar_aparato(Aparato(2, "Bicicleta estatica"))
gimnasio.agregar_aparato(Aparato(3, "Pesas"))

aparato.reservas.append(Reserva(2, "Juan", "lunes", "09:00"))
aparato.reservas.append(Reserva(1, "Ruben", "lunes", "12:00"))
aparato.reservas.append(Reserva(3, "Dani", "lunes", "17:00"))

while True:
    print("""
        -- Bienvenido al Gimnasio --
        ¿Qué acción quieres realizar?

        1. Agregar cliente
        2. Agregar aparato
        3. Generar recibos
        4. Ver morosos
        5. Hacer una reserva
        6. Ver reservas
        0. Salir
        """)
    try:
        accion = int(input("Ingresa una acción: "))
        if accion == 1:
            nombre = input("Ingresa el nombre del cliente: ")
            id_cliente = len(gimnasio.clientes) + 1
            ha_pagado = input("¿El cliente ha pagado? (s/n): ").lower() == 's'
            gimnasio.agregar_cliente(Cliente(id_cliente, nombre, ha_pagado))
        elif accion == 2:
            nombre = input("Ingresa el nombre del aparato: ")
            id_aparato = len(gimnasio.aparatos) + 1
            print("ID del nuevo aparato:", id_aparato)
            gimnasio.agregar_aparato(Aparato(id_aparato, nombre))
        elif accion == 3:
            print("Recibos:")
            for recibo in gimnasio.generar_recibos():
                print(recibo)
        elif accion == 4:
            print("Morosos:")
            morosos = gimnasio.listar_morosos()
            if morosos:
                for moroso in morosos:
                    print(moroso.nombre)
            else:
                print("No hay clientes morosos.")
        elif accion == 5:
                # Mostrar la lista de aparatos con su ID
            for aparato in gimnasio.aparatos:
                print(f"Aparato ID: {aparato.id_aparato}, Nombre: {aparato.nombre}")

            # Obtener el ID del aparato a reservar
            id_aparato = int(input("Ingresa el ID del aparato: "))

            # Encontrar el aparato correcto en la lista
            aparato_seleccionado = next((a for a in gimnasio.aparatos if a.id_aparato == id_aparato), None)

            if aparato_seleccionado:
                dia_semana = input("Ingresa el día de la semana (lunes, martes, miércoles, jueves, viernes): ")
                cliente = input("Ingresa el nombre del cliente: ")
                hora = input("Ingresa la hora (hh:mm): ")

                # Reservar el aparato seleccionado
                aparato.reservar(id_aparato, cliente, dia_semana, hora)
            else:
                print(f"No se encontró un aparato con el ID {id_aparato}.")
        elif accion == 6:
            dia_semana = input("Ingresa el día de la semana (lunes, martes, miércoles, jueves, viernes): ")
            aparato.ver_disponibilidad(dia_semana)
        elif accion == 0:
            print("Gracias por utilizar el gimnasio")
            break
        else:
            print("Opción no válida")
    except Exception as e:
            print(f"Ocurrió un error: {e}")
    finally:
        print("\n")
