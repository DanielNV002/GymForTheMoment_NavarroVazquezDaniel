from datetime import datetime, timedelta

from BBDD import BBDD

# Crear una instancia de BBDD
bbdd = BBDD()

class Aparato:
    def __init__(self, id_aparato, nombre, Bd):
        self.id_aparato = id_aparato
        self.nombre = nombre
        self.bbdd = Bd  # Ahora la instancia de BBDD se pasa como un argumento.

    @classmethod
    def from_db(cls, row):
        return cls(row[0], row[1], bbdd)

    def guardar(self):
        bbdd.cursor.execute('''
            INSERT INTO aparatos (nombre)
            VALUES (?)
        ''', (self.nombre,))
        bbdd.conn.commit()

    @staticmethod
    def obtener_todos(Bd):
        Bd.cursor.execute('SELECT * FROM aparatos')
        return [Aparato.from_db(row) for row in Bd.cursor.fetchall()]


    def reservar(self, cliente, dia_semana, hora):

        # Convertir las horas a objetos datetime
        hora_reserva = datetime.strptime(hora, "%H:%M")

        # Calcular la hora de finalización (30 minutos después)
        hora_fin = hora_reserva + timedelta(minutes=30)

        # Convertir la hora y la hora de finalización a cadenas para la comparación
        hora_inicio = hora_reserva.strftime("%H:%M")
        hora_final =hora_fin.strftime("%H:%M")

        bbdd.cursor.execute('''
            INSERT INTO reservas (id_aparato, id_cliente, dia_semana, hora_inicio, hora_final)
            VALUES (?, ?, ?, ?, ?)
        ''', (self.id_aparato, cliente.id_cliente, dia_semana, hora_inicio, hora_final))
        bbdd.conn.commit()

    @staticmethod
    def obtener_reservas(dia_semana):
        bbdd.cursor.execute('''
            SELECT hora_inicio, hora_final, cliente.nombre
            FROM reservas
            JOIN clientes AS cliente ON reservas.id_cliente = cliente.id_cliente
            WHERE reservas.dia_semana = ?
            ORDER BY hora_inicio
        ''', (dia_semana,))  # Nota el uso de tupla con un solo elemento
        return bbdd.cursor.fetchall()

    @staticmethod
    def comprobar_reserva(id_aparato, dia_semana, hora):
        # Convertir las horas a objetos datetime
        hora_reserva = datetime.strptime(hora, "%H:%M")

        # Calcular la hora de finalización (30 minutos después)
        hora_fin = hora_reserva + timedelta(minutes=30)

        # Convertir la hora y la hora de finalización a cadenas para la comparación
        hora_reserva.strftime("%H:%M")
        hora_fin.strftime("%H:%M")

        # Verificar si ya hay una reserva en el mismo aparato y en el mismo intervalo de tiempo
        bbdd.cursor.execute('''
            SELECT hora_inicio, hora_final
            FROM reservas
            WHERE id_aparato = ? AND dia_semana = ?

        ''', (id_aparato, dia_semana))

        for reserva in bbdd.cursor.fetchall():
            hora_inicio = datetime.strptime(reserva[0], "%H:%M")
            hora_final = datetime.strptime(reserva[1], "%H:%M")
            if (hora_inicio <= hora_reserva < hora_final) or (hora_reserva < hora_final and hora_final >= hora_reserva):
                return True

        # Si se encuentra una coincidencia, se devuelve True, lo que significa que ya existe una reserva
        return bbdd.cursor.fetchone() is not None

