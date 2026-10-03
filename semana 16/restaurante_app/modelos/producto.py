class Producto:
    """Representa un producto del restaurante."""

    def __init__(self, nombre, categoria, precio, disponible="Si"):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = float(precio)
        self.disponible = disponible

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "disponible": self.disponible,
        }

    @staticmethod
    def from_dict(data):
        return Producto(
            data.get("nombre", ""),
            data.get("categoria", ""),
            data.get("precio", 0),
            data.get("disponible", "Si"),
        )