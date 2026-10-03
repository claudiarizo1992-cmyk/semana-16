import json
import os

class ArchivoServicio:
    """Se encarga de leer y guardar informacion en archivos JSON."""

    @staticmethod
    def asegurar_archivo(ruta):
        carpeta = os.path.dirname(ruta)

        if carpeta:
            os.makedirs(carpeta, exist_ok=True)

        if not os.path.exists(ruta):
            with open(
                ruta,
                "w",
                encoding="utf-8"
            ) as archivo:
                json.dump(
                    [],
                    archivo,
                    ensure_ascii=False,
                    indent=4
            )

        @staticmethod
        def leer(ruta):
            ArchivoServicio.asegurar_archivo(ruta)

            try:
                with open(
                    ruta,
                    "r",
                    encoding="utf-8"
                ) as archivo:

                    contenido = json.load(archivo)

                    if isinstance(contenido, list):
                        return contenido

                    return []
            except (json.JSONDecodeError, OSError):
                return []

            @staticmethod
            def guardar(ruta, datos):
                ArchivoServicio.asegurar_archivo(ruta)

                with open(
                    ruta,
                    "w",
                    encoding="utf-8"
                ) as archivo:

                    json.dump(
                        datos,
                        archivo,
                        ensure_ascii=False,
                        indent=4
                    ) 