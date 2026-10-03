class Venta:
    """Representa una venta del restaurante."""

    def __init__(self, cliente, producto, cantidad, total):
      self.cliente = cliente
      self.producto = producto
      self.cantidad = int(cantidad)
      self.total = float(total)

    def to_dict(self):
       return {
          "cliente": self.cliente,
          "producto": self.producto,
          "cantidad": self.cantidad,
          "total": self.total
       }
    @staticmethod
    def from_dict(data):
        return Venta(
            data.get("cliente", ""),
            data.get("producto", ""),
            data.get("cantidad", 0),
            data.get("total", 0)
        )  