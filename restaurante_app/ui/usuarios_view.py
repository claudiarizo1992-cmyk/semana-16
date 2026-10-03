import tkinter as tk
from tkinter import ttk, messagebox

from modelos.usuario import Usuario
from servicios.restaurante_servicio import RestauranteServicio


class UsuariosView:
    def __init__(self, root):
        self.root = root
        self.servicio = RestauranteServicio()
        self.usuario_seleccionado = None

        self.crear_interfaz()
        self.configurar_eventos()
        self.cargar_usuarios()

    def crear_interfaz(self):
        self.root.title("Gestion de Usuarios - Restaurante")
        self.root.geometry("950x650")
        self.root.minsize(850, 550)

        titulo = ttk.Label(self.root, text="Gestion de Usuarios", font=("Arial", 22, "bold"))
        titulo.pack(pady=(20, 5))

        subtitulo = ttk.Label(
            self.root,
            text="Registro, consulta, actualizacion y eliminacion de usuarios",
        )
        subtitulo.pack(pady=(0, 15))

        formulario = ttk.LabelFrame(self.root, text="Informacion del usuario", padding=15)
        formulario.pack(fill="x", padx=25, pady=5)

        ttk.Label(formulario, text="Identificacion:").grid(row=0, column=0, sticky="w", padx=5, pady=8)
        self.identificacion_entry = ttk.Entry(formulario, width=30)
        self.identificacion_entry.grid(row=0, column=1, padx=5, pady=8)

        ttk.Label(formulario, text="Nombre completo:").grid(row=0, column=2, sticky="w", padx=5, pady=8)
        self.nombre_entry = ttk.Entry(formulario, width=35)
        self.nombre_entry.grid(row=0, column=3, padx=5, pady=8)

        ttk.Label(formulario, text="Usuario:").grid(row=1, column=0, sticky="w", padx=5, pady=8)
        self.usuario_entry = ttk.Entry(formulario, width=30)
        self.usuario_entry.grid(row=1, column=1, padx=5, pady=8)

        ttk.Label(formulario, text="Rol:").grid(row=1, column=2, sticky="w", padx=5, pady=8)
        self.rol_combo = ttk.Combobox(
            formulario,
            values=["Administrador", "Cajero", "Empleado"],
            state="readonly",
            width=32,
        )
        self.rol_combo.grid(row=1, column=3, padx=5, pady=8)
        self.rol_combo.set("Empleado")

        ttk.Label(formulario, text="Estado:").grid(row=2, column=0, sticky="w", padx=5, pady=8)
        self.estado_combo = ttk.Combobox(
            formulario,
            values=["Activo", "Inactivo"],
            state="readonly",
            width=27,
        )
        self.estado_combo.grid(row=2, column=1, padx=5, pady=8)
        self.estado_combo.set("Activo")

        botones = ttk.Frame(self.root)
        botones.pack(pady=15)

        self.registrar_button = ttk.Button(botones, text="Registrar", command=self.registrar_usuario)
        self.registrar_button.grid(row=0, column=0, padx=6)

        self.actualizar_button = ttk.Button(botones, text="Actualizar", command=self.actualizar_usuario)
        self.actualizar_button.grid(row=0, column=1, padx=6)

        self.eliminar_button = ttk.Button(botones, text="Eliminar", command=self.eliminar_usuario)
        self.eliminar_button.grid(row=0, column=2, padx=6)

        self.limpiar_button = ttk.Button(botones, text="Limpiar", command=self.limpiar_formulario)
        self.limpiar_button.grid(row=0, column=3, padx=6)

        tabla_frame = ttk.Frame(self.root)
        tabla_frame.pack(fill="both", expand=True, padx=25, pady=(0, 20))

        columnas = ("identificacion", "nombre", "usuario", "rol", "estado")
        self.tabla = ttk.Treeview(tabla_frame, columns=columnas, show="headings", selectmode="browse")

        self.tabla.heading("identificacion", text="Identificacion")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("usuario", text="Usuario")
        self.tabla.heading("rol", text="Rol")
        self.tabla.heading("estado", text="Estado")

        self.tabla.column("identificacion", width=140, anchor="center")
        self.tabla.column("nombre", width=230)
        self.tabla.column("usuario", width=160)
        self.tabla.column("rol", width=150, anchor="center")
        self.tabla.column("estado", width=120, anchor="center")

        scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scrollbar.set)
        self.tabla.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.estado_label = ttk.Label(self.root, text="Listo para trabajar.")
        self.estado_label.pack(pady=(0, 10))

    def configurar_eventos(self):
        self.tabla.bind("<<TreeviewSelect>>", self.evento_treeview_select)
        self.root.bind("<Return>", self.evento_return)
        self.root.bind("<Escape>", self.evento_escape)
        self.rol_combo.bind("<<ComboboxSelected>>", self.evento_combobox_rol)
        self.estado_combo.bind("<<ComboboxSelected>>", self.evento_combobox_estado)

    def cargar_usuarios(self):
        for elemento in self.tabla.get_children():
            self.tabla.delete(elemento)

        usuarios = self.servicio.listar_usuarios()
        for usuario in usuarios:
            self.tabla.insert(
                "",
                "end",
                values=(
                    usuario.identificacion,
                    usuario.nombre,
                    usuario.usuario,
                    usuario.rol,
                    usuario.estado,
                ),
            )

        self.estado_label.config(text=f"Usuarios registrados: {len(usuarios)}")

    def evento_treeview_select(self, event=None):
        seleccion = self.tabla.selection()
        if not seleccion:
            return

        item = self.tabla.item(seleccion[0])
        valores = item.get("values", [])

        if len(valores) < 5:
            return

        self.identificacion_entry.delete(0, tk.END)
        self.identificacion_entry.insert(0, valores[0])

        self.nombre_entry.delete(0, tk.END)
        self.nombre_entry.insert(0, valores[1])

        self.usuario_entry.delete(0, tk.END)
        self.usuario_entry.insert(0, valores[2])

        self.rol_combo.set(valores[3])
        self.estado_combo.set(valores[4])
        self.usuario_seleccionado = str(valores[0])

    def registrar_usuario(self):
        identificacion = self.identificacion_entry.get().strip()
        nombre = self.nombre_entry.get().strip()
        usuario = self.usuario_entry.get().strip()
        rol = self.rol_combo.get().strip()
        estado = self.estado_combo.get().strip()

        if not identificacion or not nombre or not usuario:
            messagebox.showwarning("Datos incompletos", "Complete identificacion, nombre y usuario.")
            return

        nuevo_usuario = Usuario(identificacion, nombre, usuario, rol, estado)
        correcto, mensaje = self.servicio.registrar_usuarios(nuevo_usuario)

        if correcto:
            messagebox.showinfo("Registro", mensaje)
            self.cargar_usuarios()
            self.limpiar_formulario()
        else:
            messagebox.showerror("Registro", mensaje)

    def registar_usuario(self):
        self.registrar_usuario()

    def actualizar_usuario(self):
        if not self.usuario_seleccionado:
            messagebox.showwarning("Actualizar", "Seleccione un usuario de la tabla.")
            return

        identificacion = self.identificacion_entry.get().strip()
        nombre = self.nombre_entry.get().strip()
        usuario = self.usuario_entry.get().strip()
        rol = self.rol_combo.get().strip()
        estado = self.estado_combo.get().strip()

        if not identificacion or not nombre or not usuario:
            messagebox.showwarning("Datos incompletos", "Complete todos los datos.")
            return

        usuario_actualizado = Usuario(identificacion, nombre, usuario, rol, estado)
        correcto, mensaje = self.servicio.actualizar_usuario(self.usuario_seleccionado, usuario_actualizado)

        if correcto:
            messagebox.showinfo("Actualizar", mensaje)
            self.cargar_usuarios()
            self.limpiar_formulario()
        else:
            messagebox.showerror("Actualizar", mensaje)

    def eliminar_usuario(self):
        if not self.usuario_seleccionado:
            messagebox.showwarning("Eliminar", "Seleccione un usuario.")
            return

        confirmar = messagebox.askyesno(
            "Confirmar eliminacion",
            "¿Esta seguro de eliminar el usuario seleccionado?",
        )
        if not confirmar:
            return

        correcto, mensaje = self.servicio.eliminar_usuario(self.usuario_seleccionado)

        if correcto:
            messagebox.showinfo("Eliminar", mensaje)
            self.cargar_usuarios()
            self.limpiar_formulario()
        else:
            messagebox.showerror("Eliminar", mensaje)

    def limpiar_formulario(self):
        self.identificacion_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.usuario_entry.delete(0, tk.END)
        self.rol_combo.set("Empleado")
        self.estado_combo.set("Activo")
        self.usuario_seleccionado = None

        for item in self.tabla.selection():
            self.tabla.selection_remove(item)

        self.identificacion_entry.focus()

    def evento_return(self, event=None):
        self.registrar_usuario()

    def evento_escape(self, event=None):
        self.limpiar_formulario()

    def evento_combobox_rol(self, event=None):
        self.root.title(f"Gestion de Usuarios - Rol: {self.rol_combo.get()}")

    def evento_combobox_estado(self, event=None):
        self.estado_label.config(text=f"Estado seleccionado: {self.estado_combo.get()}")


