import datetime

from Aparato import Aparato
from BBDD import BBDD
from Clientes import Cliente

# Crear una instancia de BBDD
bbdd = BBDD()
Ap = Aparato(None, None, bbdd)


class Gimnasio:
    def __init__(self):
        pass

    def agregar_cliente(self, cliente):
        cliente.guardar()

    def agregar_aparato(self, aparato):
        aparato.guardar()

    def generar_recibos(self):
        clientes = Cliente.obtener_todos()
        recibos = []
        for cliente in clientes:
            recibos.append(f"Recibo para {cliente.nombre}: {'Pagado' if cliente.ha_pagado else 'No pagado'}")
        return recibos

    def listar_morosos(self):
        return Cliente.obtener_morosos()

    def hacer_reserva(self, id_aparato, id_cliente, dia_semana, hora):
        aparato = Ap.obtener_todos(bbdd)
        cliente = next((c for c in Cliente.obtener_todos() if c.id_cliente == id_cliente), None)
        aparato_seleccionado = next((a for a in aparato if a.id_aparato == id_aparato), None)

        if cliente is None:
            print("Cliente no encontrado.")
            return
        if aparato_seleccionado is None:
            print("Aparato no encontrado.")
            return

        # Verificar que no haya conflictos en la reserva
        if Ap.comprobar_reserva(id_aparato, dia_semana, hora):
            print("El aparato ya está reservado para ese día y hora (reserva 30 minutos mas tarde).")
            return

        # Realizar la reserva
        aparato_seleccionado.reservar(cliente, dia_semana, hora)
        print("Reserva completada.")


def validar_dia_hora(dia_semana, hora):
    dias_validos = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    try:
        datetime.datetime.strptime(hora, '%H:%M')
    except ValueError:
        return False
    return dia_semana in dias_validos


# Función principal

def menu():
    Ap = Aparato(None, None, bbdd)
    gimnasio = Gimnasio()
    bbdd.drop_tablas()
    bbdd.crear_tablas()
    bbdd.insertarDatos()
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
                ha_pagado = input("¿El cliente ha pagado? (s/n): ").lower() == 's'
                cliente = Cliente(None, nombre, 1 if ha_pagado else 0)
                gimnasio.agregar_cliente(cliente)
            elif accion == 2:
                nombre = input("Ingresa el nombre del aparato: ")
                aparato = Aparato(None, nombre, bbdd)
                gimnasio.agregar_aparato(aparato)
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
                for aparato in Ap.obtener_todos(bbdd):
                    print(f"Aparato ID: {aparato.id_aparato}, Nombre: {aparato.nombre}")

                # Obtener el ID del aparato a reservar
                id_aparato = int(input("Ingresa el ID del aparato: "))

                # Mostrar la lista de clientes
                for cliente in Cliente.obtener_todos():
                    print(f"Cliente ID: {cliente.id_cliente}, Nombre: {cliente.nombre}")

                # Obtener el ID del cliente
                id_cliente = int(input("Ingresa el ID del cliente: "))

                # Realizar la reserva
                dia_semana = input("Ingresa el día de la semana (Lunes, Martes, Miercoles, Jueves, Viernes): ")
                hora = input("Ingresa la hora (hh:mm): ")

                if not validar_dia_hora(dia_semana.capitalize(), hora):
                    print("El formato del día o la hora es inválido.")
                else:
                    gimnasio.hacer_reserva(id_aparato, id_cliente, dia_semana.capitalize(), hora)

            elif accion == 6:
                dia_semana = input("Ingresa el día de la semana (Lunes, Martes, Miercoles, Jueves, Viernes): ")
                reservas = Ap.obtener_reservas(dia_semana.capitalize())
                if reservas:
                    for reserva in reservas:
                        hora_inicio, hora_final, cliente = reserva
                        print(f"Hora: {hora_inicio} - {hora_final}, Cliente: {cliente}")
                else:
                    print("No hay reservas para ese día.")

            elif accion == 0:
                print("Gracias por utilizar el gimnasio")
                bbdd.close()
                break
            else:
                print("Opción no válida")
        except Exception as e:
            print(f"Ocurrió un error: {e}")
        finally:
            print("\n")


if __name__ == "__main__":
    menu()

# Cerrar la conexión a la base de datos al finalizar
bbdd.conn.close()
