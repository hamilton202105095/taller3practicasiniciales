class Compra:
    def __init__(self, numero, usuarioId, usuarioNombre, total, productos):
        self.numero = numero
        self.usuarioId = usuarioId
        self.usuarioNombre = usuarioNombre
        self.total = total
        self.productos = productos

    def __dict__(self):
        return {
            'numero': self.numero,
            'usuarioId': self.usuarioId,
            'usuarioNombre': self.usuarioNombre,
            'total': self.total,
            'productos': self.productos
        }