import tkinter as tk

from ui.login_view import LoginView
from ui.main_view import MainView


def iniciar_aplicacion():
    global root

    ventana_principal = tk.Toplevel(root)
    MainView(ventana_principal)
    root.withdraw()

    def cerrar_aplicacion():
        ventana_principal.destroy()
        root.destroy()

    ventana_principal.protocol("WM_DELETE_WINDOW", cerrar_aplicacion)


def main():
    global root
    root = tk.Tk()
    LoginView(root, iniciar_aplicacion)
    root.mainloop()


if __name__ == "__main__":
    main()