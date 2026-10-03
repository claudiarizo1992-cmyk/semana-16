import json
import os

from modelos.usuario import Usuario


class RestauranteServicio:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        self.ruta_usuarios = os.path.join(base_dir, "datos", "usuarios.json")
        self.crear_archivo_usuarios()

    def crear_archivo_usuarios(self):
        """Crea la carpeta y el archivo JSON si no existen."""
        carpeta = os.path.dirname(self.ruta_usuarios)
        if not os.path.exists(carpeta):
            os.makedirs(carpeta, exist_ok=True)

        if not os.path.exists(self.ruta_usuarios):
            with open(self.ruta_usuarios, "w", encoding="utf-8") as archivo:
                json.dump([], archivo, ensure_ascii=False, indent=4)

    def leer_usuarios(self):
        """Lee la lista de usuarios desde el archivo JSON."""
        try:
            with open(self.ruta_usuarios, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

        if not isinstance(datos, list):
            return []

        return [Usuario.from_dict(dato) for dato in datos]

    def guardar_usuarios(self, usuarios):
        """Guarda la lista de usuarios en formato JSON."""
        datos = [usuario.to_dict() for usuario in usuarios]
        with open(self.ruta_usuarios, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=4)

    def listar_usuarios(self):
        """Devuelve todos los usuarios registrados."""
        return self.leer_usuarios()

    def registrar_usuarios(self, usuario):
        """Registra un nuevo usuario."""
        usuarios = self.leer_usuarios()

        for usuario_existente in usuarios:
            if usuario_existente.identificacion == usuario.identificacion:
                return False, "La identificacion ya esta registrada."
            if usuario_existente.usuario.lower() == usuario.usuario.lower():
                return False, "El nombre de usuario ya esta registrado."

        usuarios.append(usuario)
        self.guardar_usuarios(usuarios)
        return True, "Usuario registrado correctamente."

    def registar_usuarios(self, usuario):
        return self.registrar_usuarios(usuario)

    def actualizar_usuario(self, identificacion_original, usuario_actualizado):
        """Actualiza un usuario existente."""
        usuarios = self.leer_usuarios()
        posicion_encontrada = -1

        for posicion, usuario in enumerate(usuarios):
            if usuario.identificacion == identificacion_original:
                posicion_encontrada = posicion
                break

        if posicion_encontrada == -1:
            return False, "No se encontro el usuario seleccionado."

        for posicion, usuario in enumerate(usuarios):
            if posicion == posicion_encontrada:
                continue
            if usuario.usuario.lower() == usuario_actualizado.usuario.lower():
                return False, "El nombre de usuario ya esta registrado."

        usuarios[posicion_encontrada] = usuario_actualizado
        self.guardar_usuarios(usuarios)
        return True, "Usuario actualizado correctamente."

    def eliminar_usuarios(self, identificacion):
        """Elimina un usuario por su identificacion."""
        usuarios = self.leer_usuarios()
        usuarios_nuevos = []
        encontrado = False

        for usuario in usuarios:
            if usuario.identificacion == identificacion:
                encontrado = True
            else:
                usuarios_nuevos.append(usuario)

        if not encontrado:
            return False, "No se encontro el usuario seleccionado."

        self.guardar_usuarios(usuarios_nuevos)
        return True, "Usuario eliminado correctamente."

    def eliminar_usuario(self, identificacion):
        return self.eliminar_usuarios(identificacion)