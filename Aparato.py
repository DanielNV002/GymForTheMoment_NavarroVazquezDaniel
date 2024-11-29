from _pydatetime import *

from Reserva import Reserva

class Aparato:
    def __init__(self, id_aparato, nombre):
        self.id_aparato = id_aparato
        self.nombre = nombre
        self.reservas = []  # Lista de reservas para este aparato

    def reservar(self, id_aparato, cliente, dia_semana, hora):
        reservaGuardada = Reserva(id_aparato, cliente, dia_semana, hora)
        self.reservas.append(reservaGuardada)
        print(f"Se ha reservado el aparato {self.nombre} el {reservaGuardada.dia_semana} a las {reservaGuardada.hora} por {reservaGuardada.cliente}.")

    def ver_disponibilidad(self, dia_semana):
        for r in self.reservas:
            if r.dia_semana == dia_semana:
                # Convertimos la hora de inicio en un objeto datetime
                hora_inicio = datetime.strptime(r.hora, "%H:%M")
                # Sumamos 30 minutos
                hora_fin = hora_inicio + timedelta(minutes=30)
                # Formateamos la hora de inicio y fin para que se vean como HH:MM
                hora_inicio_str = hora_inicio.strftime("%H:%M")
                hora_fin_str = hora_fin.strftime("%H:%M")

                print(f"El aparato {self.nombre} no se encuentra disponible de {hora_inicio_str} a {hora_fin_str} por {r.cliente}.")
        return f"El aparato {self.nombre} se encuentra disponible el {dia_semana}."

    def __str__(self):
        return f"Aparato {self.nombre} (ID: {self.id_aparato})"