class Cliente:
    def __init__(self, id_cliente, nombre, ha_pagado=False):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.ha_pagado = ha_pagado

    def __str__(self):
        return f"Cliente {self.nombre} (ID: {self.id_cliente})"
