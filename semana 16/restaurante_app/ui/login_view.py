from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import ttk, messagebox, PhotoImage


class LoginView:
    """Ventana de inicio de sesion."""

    def __init__(self, root, on_login):
        self.root = root
        self.on_login = on_login

        self.root.title("Restaurante App - Inicio de sesion")
        self.root.geometry("700x600")
        self.root.resizable(False, False)

        contenedor = ttk.Frame(self.root, padding=30)
        contenedor.pack(fill="both", expand=True)

        BASE_DIR = Path(__file__).resolve().parent.parent
        
        #icono de la ventana
        self.icono=PhotoImage(file=str(BASE_DIR/"assets/icono.png"))
        self.root.iconphoto(True, self.icono)
        
        #logo
        self.logo = PhotoImage(file=str(BASE_DIR/"assets/logo.png"))
        
        ttk.Label(
            contenedor,
            image=self.logo
        ).pack(pady=5)
        
        #recurso visual
        self.recurso_visual = PhotoImage(file=str(BASE_DIR/"assets/recurso visual.png"))
        ttk.Label(
            contenedor,
            image=self.recurso_visual
        ).pack(pady=5)
        
        ttk.Label(
            contenedor,
            text="RESTAURANTE APP",
            font=("Arial", 22, "bold")
        ).pack(pady=10)

        ttk.Label(
            contenedor,
            text="Semana 16 - Manejo de eventos"
        ).pack(pady=5)

        formulario = ttk.LabelFrame(contenedor, text="Inicio de sesion", padding=15)
        formulario.pack(fill="x", pady=15)

        ttk.Label(formulario, text="Usuario:").grid(row=0, column=0, padx=5, pady=8)
        self.entry_usuario = ttk.Entry(formulario, width=25)
        self.entry_usuario.grid(row=0, column=1, padx=5, pady=8)

        ttk.Label(formulario, text="Contraseña:").grid(row=1, column=0, padx=5, pady=8)
        self.entry_clave = ttk.Entry(formulario, width=25, show="*")
        self.entry_clave.grid(row=1, column=1, padx=5, pady=8)

        ttk.Button(contenedor, text="Ingresar", command=self.validar).pack(pady=10)

        self.root.bind("<Return>", self.evento_enter)
        self.entry_usuario.focus()

    def evento_enter(self, event=None):
        """Permite iniciar sesion presionando Enter."""
        self.validar()

    def validar(self):
        """Valida los datos de inicio de sesion."""
        usuario = self.entry_usuario.get().strip()
        clave = self.entry_clave.get().strip()

        if usuario == "admin" and clave == "1234":
            if self.on_login is not None:
                self.on_login()
        else:
            messagebox.showerror(
                "Acceso",
                "Usuario o contraseña incorrecta.\n\n"
                "Usuario: admin\n"
                "Contraseña: 1234"
            )