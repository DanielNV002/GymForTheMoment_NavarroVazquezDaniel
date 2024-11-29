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
                hora TEXT NOT NULL,
                FOREIGN KEY (id_aparato) REFERENCES aparatos(id_aparato),
                FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
            )
        ''')

        # Commit para asegurarse de que las tablas se creen
        self.conn.commit()

    def close(self):
        # Cerrar la conexión con la base de datos cuando ya no se necesite
        self.conn.close()
