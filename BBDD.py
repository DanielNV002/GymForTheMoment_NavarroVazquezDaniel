import sqlite3

class BBDD:
    def __init__(self):
        # Conectar a la base de datos (si no existe, se crea)
        self.conn = sqlite3.connect('gimnasio.db')
        self.cursor = self.conn.cursor()

    def crear_tablas(self):
        # Crear tablas necesarias solo si no existen
        self.cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS clientes (
                id_cliente INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                ha_pagado INTEGER NOT NULL
            )
        ''')

        self.cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS aparatos (
                id_aparato INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL
            )
        ''')

        self.cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS reservas (
                id_reserva INTEGER PRIMARY KEY,
                id_aparato INTEGER,
                id_cliente INTEGER,
                dia_semana TEXT NOT NULL,
                hora_inicio TEXT NOT NULL,
                hora_final TEXT NOT NULL,
                FOREIGN KEY (id_aparato) REFERENCES aparatos(id_aparato),
                FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
            )
        ''')

        # Commit para asegurarse de que las tablas se creen
        self.conn.commit()

    def insertarDatos(self):
        # Insertar clientes
        self.cursor.execute('''
            INSERT INTO clientes (nombre, ha_pagado)
            VALUES ("Pedro", 0)
        ''')
        self.cursor.execute('''
            INSERT INTO clientes (nombre, ha_pagado)
            VALUES ("Juan", 1)
        ''')
        self.cursor.execute('''
            INSERT INTO clientes (nombre, ha_pagado)
            VALUES ("Maria", 1)
        ''')
        self.cursor.execute('''
            INSERT INTO clientes (nombre, ha_pagado)
            VALUES ("Luis", 0)
        ''')
        self.cursor.execute('''
            INSERT INTO clientes (nombre, ha_pagado)
            VALUES ("Ana", 1)
        ''')
        self.cursor.execute('''
            INSERT INTO clientes (nombre, ha_pagado)
            VALUES ("Carlos", 0)
        ''')

        # Insertar aparatos
        self.cursor.execute('''
            INSERT INTO aparatos (id_aparato, nombre)
            VALUES (1, "Mancuernas")
        ''')
        self.cursor.execute('''
            INSERT INTO aparatos (id_aparato, nombre)
            VALUES (2, "Cinta de Correr")
        ''')
        self.cursor.execute('''
            INSERT INTO aparatos (id_aparato, nombre)
            VALUES (3, "Bicicleta Estática")
        ''')
        self.cursor.execute('''
            INSERT INTO aparatos (id_aparato, nombre)
            VALUES (4, "Elíptica")
        ''')
        self.cursor.execute('''
            INSERT INTO aparatos (id_aparato, nombre)
            VALUES (5, "Banco de Pesas")
        ''')
        self.cursor.execute('''
            INSERT INTO aparatos (id_aparato, nombre)
            VALUES (6, "Máquina de Remo")
        ''')

        # Insertar reservas
        self.cursor.execute('''
            INSERT INTO reservas (id_reserva, id_aparato, id_cliente, dia_semana, hora_inicio, hora_final)
            VALUES (1, 1, 1, "Lunes", "10:00", "10:30")
        ''')
        self.cursor.execute('''
            INSERT INTO reservas (id_reserva, id_aparato, id_cliente, dia_semana, hora_inicio, hora_final)
            VALUES (2, 2, 2, "Martes", "14:00", "14:30")
        ''')
        self.cursor.execute('''
            INSERT INTO reservas (id_reserva, id_aparato, id_cliente, dia_semana, hora_inicio, hora_final)
            VALUES (3, 3, 3, "Miercoles", "09:00", "09:30")
        ''')
        self.cursor.execute('''
            INSERT INTO reservas (id_reserva, id_aparato, id_cliente, dia_semana, hora_inicio, hora_final)
            VALUES (4, 4, 4, "Jueves", "12:00", "12:30")
        ''')
        self.cursor.execute('''
            INSERT INTO reservas (id_reserva, id_aparato, id_cliente, dia_semana, hora_inicio, hora_final)
            VALUES (5, 5, 5, "Viernes", "08:00", "08:30")
        ''')
        self.cursor.execute('''
            INSERT INTO reservas (id_reserva, id_aparato, id_cliente, dia_semana, hora_inicio, hora_final)
            VALUES (8, 3, 5, "Lunes", "17:00", "17:30")
        ''')
        self.cursor.execute('''
            INSERT INTO reservas (id_reserva, id_aparato, id_cliente, dia_semana, hora_inicio, hora_final)
            VALUES (9, 4, 6, "Miercoles", "13:00", "13:30")
        ''')
        self.cursor.execute('''
            INSERT INTO reservas (id_reserva, id_aparato, id_cliente, dia_semana, hora_inicio, hora_final)
            VALUES (10, 5, 1, "Jueves", "10:30", "11:00")
        ''')
        self.cursor.execute('''
            INSERT INTO reservas (id_reserva, id_aparato, id_cliente, dia_semana, hora_inicio, hora_final)
            VALUES (11, 6, 4, "Viernes", "14:00", "14:30")
        ''')

        self.conn.commit()

    def close(self):
        self.conn.close()


    def drop_tablas(self):
        # Obtener todas las tablas en la base de datos
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tablas = self.cursor.fetchall()

        # Dropear cada tabla encontrada
        for tabla in tablas:
            self.cursor.execute(f"DROP TABLE IF EXISTS {tabla[0]}")

        self.conn.commit()
