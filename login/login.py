import tkinter as tk

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventana de Inicio de Sesión")

        self.frame_izquierda = tk.Frame(self, width=200, height=400, bg="white")
        self.frame_izquierda.pack(side="left", fill="both", expand=True)

        self.logo = tk.PhotoImage(file="logo2.png")
        self.logo_label = tk.Label(self.frame_izquierda, image=self.logo)
        self.logo_label.pack(pady=20)

        self.frame_derecha = tk.Frame(self, width=400, height=400, bg="lightblue")
        self.frame_derecha.pack(side="right", fill="both", expand=True)
 
        self.label_titulo = tk.Label(self.frame_derecha, text="Inicio de Sesión", font=("Arial", 20))
        self.label_titulo.pack(pady=20)

        self.label_usuario = tk.Label(self.frame_derecha, text="Usuario:", font=("Arial", 12))
        self.label_usuario.pack()
        self.entry_usuario = tk.Entry(self.frame_derecha, font=("Arial", 12))
        self.entry_usuario.pack(pady=5)

        self.label_clave = tk.Label(self.frame_derecha, text="Contraseña:", font=("Arial", 12))
        self.label_clave.pack()
        self.entry_clave = tk.Entry(self.frame_derecha, show="*", font=("Arial", 12))
        self.entry_clave.pack(pady=5)

        self.boton_ingresar = tk.Button(self.frame_derecha, text="Ingresar", font=("Arial", 12), command=self.ingresar)
        self.boton_ingresar.pack(pady=20)

    def ingresar(self):
        usuario = self.entry_usuario.get()
        clave = self.entry_clave.get()
        print(usuario)
        print(clave)

if __name__ == "__main__":
    ventana = VentanaPrincipal()
    ventana.mainloop()