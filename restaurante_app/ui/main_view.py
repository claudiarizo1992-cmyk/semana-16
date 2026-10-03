import tkinter as tk
from tkinter import ttk
from pathlib import Path
from ui.usuarios_view import UsuariosView


class MainView:
    """Ventana principal del sistema."""

    def __init__(self, root):
        self.root = root

        self.root.title("Restaurante App")
        self.root.geometry("980x650")
        self.root.minsize(900, 600)
          
        self.crear_interfaz()

        
    def crear_interfaz(self):
        barra = ttk.Frame(self.root, padding=10)
        barra.pack(fill="x")

        contenedor = tk.Frame(
            self.root,
            bg="white"
        )
        contenedor.pack(
              expand=True,
                fill="both",
                padx=30,
                pady=20
        
        )
               
        ttk.Label(
            barra,
            text="RESTAURANTE APP",
            font=("Arial", 20, "bold")
        ).pack(side="left")

        ttk.Button(
            barra,
            text="Gestion de Usuarios",
            command=self.abrir_usuarios,
        ).pack(side="right")

        ttk.Separator(self.root, orient="horizontal").pack(fill="x", pady=(10, 0))

        contenido = ttk.Frame(self.root, padding=30)
        contenido.pack(fill="both", expand=True)

        ttk.Label(
            contenido,
            text="Panel principal",
            font=("Arial", 24, "bold")
        ).pack(pady=(80, 15))

        ttk.Label(
            contenido,
            text=(
                "Sistema de gestion para restaurante\n\n"
                "Sistema 16: Manejo de eventos en Tkinter"
            ),
            justify="center",
            font=("Arial", 12)
        ).pack()

        ttk.Button(
            contenido,
            text="Abrir gestion de usuarios",
            command=self.abrir_usuarios
        ).pack(pady=25)

    def abrir_usuarios(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Gestion de Usuarios")
        ventana.grab_set()
        UsuariosView(ventana)