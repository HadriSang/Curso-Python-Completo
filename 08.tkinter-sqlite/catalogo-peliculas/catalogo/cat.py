import tkinter as tk

def main():
    root = tk.Tk()
    root.title('Catalogo Peliculas')
    root.iconbitmap('img/pelicula.ico')
    
    #root.resizable(0,0) #esto nos permite que al colocar 00 no se pueda cambiar de tamaño
    # si colocamos un 1 en la primera posicion solo nos deja editar el tamaño de los lados
    # si colocamos 1 en el segundo solo nos deja modificar el tamaño de la ventana para arriba
    
    frame = tk.Frame()
    root.mainloop()



# from tkinter import *
# from tkinter import ttk

# def main():
#     root = Tk()  #esto crea una interfaz
#     frm = ttk.Frame(root,padding=10)
#     frm.grid()
#     ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
#     ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
#     root.mainloop()

if __name__ == '__main__':
    main()