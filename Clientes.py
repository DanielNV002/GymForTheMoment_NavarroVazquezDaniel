from BBDD import BBDD

# Crear una instancia de BBDD
bbdd = BBDD()

class Cliente:
    def __init__(self, id_cliente, nombre, ha_pagado):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.ha_pagado = ha_pagado

    @classmethod
    def from_db(cls, row):
        return cls(row[0], row[1], row[2])

    def guardar(self):
        bbdd.cursor.execute('''
            INSERT INTO clientes (nombre, ha_pagado)
            VALUES (?, ?)
        ''', (self.nombre, self.ha_pagado))
        bbdd.conn.commit()

    @staticmethod
    def obtener_todos():
        bbdd.cursor.execute('SELECT * FROM clientes')
        return [Cliente.from_db(row) for row in bbdd.cursor.fetchall()]

    @staticmethod
    def obtener_morosos():
        bbdd.cursor.execute('SELECT * FROM clientes WHERE ha_pagado = 0')
        return [Cliente.from_db(row) for row in bbdd.cursor.fetchall()]