class Reserva:
    def __init__(self, id_aparato, cliente, dia_semana, hora):
        self.cliente = cliente
        self.dia_semana = dia_semana  # Día de la semana (ejemplo: "Lunes")
        self.hora = hora  # Hora de la reserva (ejemplo: "09:00")
        self.id_aparato = id_aparato

    def __str__(self):
       return f"Reserva de {self.cliente.nombre} en {self.aparato.nombre} el {self.dia_semana} a las {self.hora}"
