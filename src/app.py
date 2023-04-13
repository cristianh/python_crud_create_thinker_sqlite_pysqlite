import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# SQLLITE
import sqlite3

# IMPORT DBCONTROLLER
import DB.dbcontroller as db
# MODEL
from Models.User import User


def saveUser():
    # GET DATA FORM
    id = input_id.get()
    nombre = input_nombre.get()
    apellido = input_apellido.get()
    edad = input_edad.get()
    user = User(id=id,nombre=nombre,apellido=apellido,edad=edad)
    

    try:
        con = sqlite3.connect('dbtienda.db')
    except Error as e:
        print(e)


    
    cursordb = con.cursor()


    query = f"""INSERT INTO usuarios(id,nombre,apellido,edad) VALUES({user.id},'{user.nombre}','{user.apellido}',{user.edad})"""

    insert = cursordb.execute(query)
    con.commit()
    if insert.lastrowid:
        id = input_id.delete(0, "end")
        nombre = input_nombre.delete(0, "end")
        apellido = input_apellido.delete(0, "end")
        edad = input_edad.delete(0, "end")
        messagebox.showinfo(message="Usuario registrado", title="Título")
        print(insert.lastrowid)        

    

    cursordb.close()
    con.close()
     


window = tk.Tk()
# CONFIGURACION DE LA VENTANA PRINCIPAL
window.title('Registro usuario')
window.config(width=300, height=200)

# LABELS Y INPUTS

# ID -  CEDULA:
label_id = ttk.Label(text="Cedula:")
label_id.place(x=20, y=20)
input_id = ttk.Entry()
input_id.place(x=80, y=20, width=160)

# FIRST_NAME:
label_nombre = ttk.Label(text="Nombre:")
label_nombre.place(x=20, y=50)
input_nombre = ttk.Entry()
input_nombre.place(x=80, y=50, width=160)

# LAST_NAME:
label_apellido = ttk.Label(text="Apellido:")
label_apellido.place(x=20, y=80)
input_apellido = ttk.Entry()
input_apellido.place(x=80, y=80, width=160)

# AGE:
label_edad = ttk.Label(text="Edad:")
label_edad.place(x=20, y=110)
input_edad = ttk.Entry()
input_edad.place(x=80, y=110, width=160)

# BTN_SAVE
boton_guardar = ttk.Button(text="GUARDAR", command=saveUser)
boton_guardar.place(x=100, y=140)


window.mainloop()
