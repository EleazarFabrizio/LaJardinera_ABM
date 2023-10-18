from tkinter import *
from comandosSQL import *
from agregarProducto import * 
from buscarProducto import * 

ventana = Tk()
ventana.resizable(width=False, height=False)
ventana.title('Textil La Jardinera')

tiutlo = Label(ventana, text='Gestion de Stock', font=60)
tiutlo.grid(row=0, columnspan=3, padx=10, pady=10)

boton_agregar = Button(ventana, text='Agregar Productos', command=lambda:ventana_agregar_producto(ventana), font=45)
boton_agregar.grid(row=1, column=0, padx=10, pady=10)

boton_mostrar_productos = Button(ventana, text='Consultar Productos', command=lambda:buscar_producto(ventana), font=45)
boton_mostrar_productos.grid(row=1, column=1, padx=10, pady=10)

boton_buscar = Button(ventana, text='Consultar Informes', command="", font=45)
boton_buscar.grid(row=1, column=2, padx=10, pady=10)

ventana.mainloop()