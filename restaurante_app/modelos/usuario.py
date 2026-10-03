class Usuario:
    def __init__(
        self,
        identificacion,
        nombre,
        usuario,
        rol,
        estado="Activo"
    ):
        self.identificacion = identificacion
        self.nombre = nombre
        self.usuario = usuario
        self.rol = rol
        self.estado = estado

    def to_dict(self):
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "usuario": self.usuario,
            "rol": self.rol,
            "estado": self.estado,
        }

    @classmethod
    def from_dict(cls, datos):
        return cls(
            datos.get("identificacion", ""),
            datos.get("nombre", ""),
            datos.get("usuario", ""),
            datos.get("rol", "Empleado"),
            datos.get("estado", "Activo"),
        )
