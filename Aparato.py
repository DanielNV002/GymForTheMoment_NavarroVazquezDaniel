from BBDD import BBDD

# Crear una instancia de BBDD
bbdd = BBDD()

class Aparato:
    def __init__(self, id_aparato, nombre, bbdd):
        self.id_aparato = id_aparato
        self.nombre = nombre
        self.bbdd = bbdd  # Ahora la instancia de BBDD se pasa como un argumento.

    @classmethod
    def from_db(cls, row):
        return cls(row[0], row[1])

    def guardar(self):
        bbdd.cursor.execute('''
            INSERT INTO aparatos (nombre)
            VALUES (?)
        ''', (self.nombre,))
        bbdd.conn.commit()

    @staticmethod
    def obtener_todos():
        bbdd.cursor.execute('SELECT * FROM aparatos')
        return [Aparato.from_db(row) for row in bbdd.cursor.fetchall()]

    def reservar(self, cliente, dia_semana, hora):
        bbdd.cursor.execute('''
            INSERT INTO reservas (id_aparato, id_cliente, dia_semana, hora)
            VALUES (?, ?, ?, ?)
        ''', (self.id_aparato, cliente.id_cliente, dia_semana, hora))
        bbdd.conn.commit()

    @staticmethod
    def obtener_reservas(dia_semana):
        bbdd.cursor.execute('''
            SELECT reservas.hora, clientes.nombre
            FROM reservas
            JOIN clientes ON reservas.id_cliente = clientes.id_cliente
            WHERE reservas.dia_semana = ?
            ORDER BY reservas.hora
        ''', (dia_semana,))
        return bbdd.cursor.fetchall()

    def comprobar_reserva(self, dia_semana, hora):
        # Realizar la consulta para verificar si ya existe una reserva en ese día y hora
        bbdd.cursor.execute('''
            SELECT 1
            FROM reservas
            WHERE dia_semana = ? AND hora = ?
        ''', (dia_semana, hora))

        # Si la consulta devuelve algún resultado, significa que ya hay una reserva
        if bbdd.cursor.fetchone():
            return True  # Ya existe una reserva en ese día y hora
        else:
            return False  # No hay ninguna reserva en ese día y hora
