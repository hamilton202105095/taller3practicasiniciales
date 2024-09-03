class Usuario:
    def __init__(self, id, nombre, password):
        self.id = id
        self.nombre = nombre
        self.password = password

    def __dict__(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'password': self.password,
            'edad': self.edad,
            'email': self.email,
            'telefono': self.telefono
        }
    
    def __str__(self):
        return f'Usuario: {self.nombre}',
        f'Edad: {self.edad}',
        f'Email: {self.email}',
        f'Telefono: {self.telefono}'