import tkinter as tk
from tkinter import messagebox
import re
import os
import mysql.connector 

def InsertarRegistro(nombres, apellidos, edad, estatura, telefono, genero):
    try: 
        conexion = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            password="V3ntur1n0",
            database="practica"
        )
        
        cursor = conexion.cursor()
        query = "INSERT INTO registros(nombres, apellidos, edad, estatura, telefono, genero) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (nombres, apellidos, edad, estatura, telefono, genero)
        cursor.execute(query, valores)
        conexion.commit() 
        cursor.close()
        conexion.close()
        messagebox.showinfo("Informacion", "Datos guardados en la base de datos con exito.")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error al insertar los datos: {err}")

class Formulario:
    def __init__(self, root):  
        self.root = root
        self.root.title("Formulario")
        self.root.geometry("400x350")

        self.nombres_var = tk.StringVar()
        self.apellidos_var = tk.StringVar()
        self.edad_var = tk.StringVar()
        self.estatura_var = tk.StringVar()
        self.telefono_var = tk.StringVar()
        self.genero_var = tk.StringVar()

        # Campos de texto con eventos para validar mientras se escribe
        tk.Label(root, text="Nombre(s):").grid(row=0, column=0, padx=10, pady=5, sticky='e')
        self.nombre_entry = tk.Entry(root, textvariable=self.nombres_var)
        self.nombre_entry.grid(row=0, column=1)
        self.nombre_entry.bind("<KeyRelease>", self.validar_nombre)

        tk.Label(root, text="Apellidos:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.nombre_entry = tk.Entry(root, textvariable=self.nombres_var)
        self.nombre_entry.grid(row=0, column=1)
        self.nombre_entry.bind("<KeyRelease>", self.validar_nombre)

        tk.Label(root, text="Apellidos:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.apellidos_entry = tk.Entry(root, textvariable=self.apellidos_var)
        self.apellidos_entry.grid(row=1, column=1)
        self.apellidos_entry.bind("<KeyRelease>", self.validar_apellidos)

        tk.Label(root, text="Edad:").grid(row=2, column=0, padx=10, pady=5, sticky='e')
        self.edad_entry = tk.Entry(root, textvariable=self.edad_var)
        self.edad_entry.grid(row=2, column=1)
        self.edad_entry.bind("<KeyRelease>", self.validar_edad)

        tk.Label(root, text="Estatura:").grid(row=3, column=0, padx=10, pady=5, sticky='e')
        self.estatura_entry = tk.Entry(root, textvariable=self.estatura_var)
        self.estatura_entry.grid(row=3, column=1)
        self.estatura_entry.bind("<KeyRelease>", self.validar_estatura)

        tk.Label(root, text="Telefono:").grid(row=4, column=0, padx=10, pady=5, sticky='e')
        self.telefono_entry = tk.Entry(root, textvariable=self.telefono_var)
        self.telefono_entry.grid(row=4, column=1)
        self.telefono_entry.bind("<KeyRelease>", self.validar_telefono)

        # Radio buttons para genero
        tk.Label(root, text="Genero:").grid(row=5, column=0, padx=10, pady=5, sticky='e')
        tk.Radiobutton(root, text="Hombre", variable=self.genero_var, value="Hombre").grid(row=5, column=1)
        tk.Radiobutton(root, text="Mujer", variable=self.genero_var, value="Mujer").grid(row=5, column=2)

        # Botones
        tk.Button(root, text="Guardar", command=self.guardar_datos).grid(row=6, column=0, padx=10, pady=20)
        tk.Button(root, text="Limpiar", command=self.limpiar_datos).grid(row=6, column=1)
        tk.Button(root, text="Cerrar", command=self.root.quit).grid(row=6, column=2)

    def guardar_datos(self):
        nombres = self.nombres_var.get()
        apellidos = self.apellidos_var.get()
        edad = self.edad_var.get()
        estatura = self.estatura_var.get()
        telefono = self.telefono_var.get()
        genero = self.genero_var.get()

        if not self.validar_entrada():
            return

        InsertarRegistro(nombres, apellidos, edad, estatura, telefono, genero)

        datos = f"Nombre(s): {nombres}\nApellidos: {apellidos}\nEdad: {edad}\nEstatura: {estatura}\nTelefono: {telefono}\nGenero: {genero}"

        ruta_archivo = os.path.expanduser("~/datos.txt")
        with open(ruta_archivo, "a") as archivo:
            archivo.write(datos + "\n\n")

        messagebox.showinfo("Informacion", f"Datos guardados con exito:\n\n{datos}")

    def validar_entrada(self):
        if not self.validar_nombre(None):
            return False
        if not self.validar_apellidos(None):
            return False
        if not self.validar_edad(None):
            return False
        if not self.validar_estatura(None):
            return False
        if not self.validar_telefono(None):
            return False
        return True

    def limpiar_datos(self):
        self.nombres_var.set("")
        self.apellidos_var.set("")
        self.edad_var.set("")
        self.estatura_var.set("")
        self.telefono_var.set("")
        self.genero_var.set("")

        messagebox.showinfo("Informacion", "Datos borrados exitosamente")

    def validar_nombre(self, event):
        nombre = self.nombres_var.get()
        if not re.match(r"^[a-zA-Z\s]+$", nombre):
            self.nombre_entry.config(bg="pink")
            return False
        self.nombre_entry.config(bg="white")
        return True

    def validar_apellidos(self, event):
        apellidos = self.apellidos_var.get()
        if not re.match(r"^[a-zA-Z\s]+$", apellidos):
            self.apellidos_entry.config(bg="pink")
            return False
        self.apellidos_entry.config(bg="white")
        return True

    def validar_edad(self, event):
        edad = self.edad_var.get()
        if not edad.isdigit():
            self.edad_entry.config(bg="pink")
            return False
        self.edad_entry.config(bg="white")
        return True

    def validar_estatura(self, event):
        estatura = self.estatura_var.get()
        if not re.match(r"^\d+(\.\d+)?$", estatura):
            self.estatura_entry.config(bg="pink")
            return False
        self.estatura_entry.config(bg="white")
        return True

    def validar_telefono(self, event):
        telefono = self.telefono_var.get()
        if not re.match(r"^\d{10}$", telefono):
            self.telefono_entry.config(bg="pink")
            return False
        self.telefono_entry.config(bg="white")
        return True

if __name__ == "__main__":  
    root = tk.Tk()
    formulario = Formulario(root)
    root.mainloop()
