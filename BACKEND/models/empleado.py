class Empleado:
    def __init__(self, codigo, nombre, puesto):
        self.codigo = codigo
        self.nombre = nombre
        self.puesto = puesto

    def __dict__(self):
        return {
            'codigo': self.codigo,
            'nombre': self.nombre,
            'puesto': self.puesto
        }

