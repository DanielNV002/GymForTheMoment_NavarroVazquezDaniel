from Aparato import Aparato
from BBDD import BBDD
from Clientes import Cliente

# Crear una instancia de BBDD
bbdd = BBDD()

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
        aparato = Aparato.obtener_todos()
        cliente = [c for c in Cliente.obtener_todos() if c.id_cliente == id_cliente][0]
        aparato_seleccionado = [a for a in aparato if a.id_aparato == id_aparato][0]
        aparato_seleccionado.reservar(cliente, dia_semana, hora)


# Función principal

def menu():
    Ap = Aparato(None, None, bbdd)
    gimnasio = Gimnasio()
    bbdd.crear_tablas()
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
                aparato = Ap(None, nombre)
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
                for aparato in Ap.obtener_todos():
                    print(f"Aparato ID: {aparato.id_aparato}, Nombre: {aparato.nombre}")

                # Obtener el ID del aparato a reservar
                id_aparato = int(input("Ingresa el ID del aparato: "))

                # Mostrar la lista de clientes
                for cliente in Cliente.obtener_todos():
                    print(f"Cliente ID: {cliente.id_cliente}, Nombre: {cliente.nombre}")

                # Obtener el ID del cliente
                id_cliente = int(input("Ingresa el ID del cliente: "))

                # Realizar la reserva
                dia_semana = input("Ingresa el día de la semana (lunes, martes, miércoles, jueves, viernes): ")
                hora = input("Ingresa la hora (hh:mm): ")

                if Ap.comprobar_reserva(dia_semana, hora):
                    print("Ya existe una reserva para ese día y hora.")
                else:
                    print("No hay reservas para ese día y hora. Puedes hacer la reserva.")
                    gimnasio.hacer_reserva(id_aparato, id_cliente, dia_semana, hora)

            elif accion == 6:
                dia_semana = input("Ingresa el día de la semana (lunes, martes, miércoles, jueves, viernes): ")
                reservas = Ap.obtener_reservas(dia_semana)
                if reservas:
                    for reserva in reservas:
                        print(f"Hora: {reserva[0]}, Cliente: {reserva[1]}")
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
