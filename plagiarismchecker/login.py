import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()

    # Aquí iría la lógica para verificar el nombre de usuario y la contraseña
    # En este ejemplo, simplemente se mostrará un mensaje de éxito o error
    if username == "admin" and password == "password":
        messagebox.showinfo("Login", "Inicio de sesión exitoso")
    else:
        messagebox.showerror("Login", "Nombre de usuario o contraseña incorrectos")

# Crear la ventana principal
root = tk.Tk()
root.title("Login")

# Crear y colocar los widgets en la ventana
username_label = tk.Label(root, text="Nombre de usuario:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Contraseña:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

login_button = tk.Button(root, text="Iniciar sesión", command=login)
login_button.pack()

# Ejecutar el bucle principal de la aplicación
root.mainloop()
