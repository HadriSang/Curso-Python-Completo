import tkinter as tk
from tkinter import	ttk
from model.peliculasDao import crearTabla, borrarTabla
from model.peliculasDao import Pelicula,guardarDatos,listar,editar,eliminar
from tkinter import messagebox
#aca creamos la clase frame que importa de la propia clase frame
def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width= 300, height = 300)
    menu_inicio= tk.Menu(barra_menu,tearoff = 0)
    menu_consultas = tk.Menu(barra_menu,tearoff = 0)
    menu_2= tk.Menu(barra_menu,tearoff = 0)
    barra_menu.add_cascade(label='Inicio', menu= menu_inicio)
    menu_inicio.add_command(label = 'Crear Registro en DB' ,command= crearTabla)
    menu_inicio.add_command(label = 'Eliminar Registro en DB', command= borrarTabla)
    menu_inicio.add_command(label = 'Salir', command = root.destroy)


    barra_menu.add_cascade(label='Consultas', menu= menu_consultas)
    menu_consultas.add_command(label= 'Prueba')
    
    barra_menu.add_cascade(label='Configuracion')
    barra_menu.add_cascade(label='Reporte')
class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root,width = 480, height=380 )
        self.root = root
        self.pack()
        # self.config(bg='red')
        self.idPelicula = None
        self.camposPeliculas() # es necesario llamar a la funcion dentro del constructor para que se ejecute
        self.botones()
        self.deshabilitarCampos()
        self.tablaPeliculas()
    
    def camposPeliculas(self):
        #aca creamos el objeto label dentro del self
        self.labelNombre = tk.Label(self,text='Nombre: ')
        # con el grid estamos indicando en que posicion de la ventana se ubicara ese label
        self.labelNombre.config(font=('Arial',12,'bold'))
        self.labelNombre.grid(row = 0, column = 0, padx = 10 , pady = 10)

        self.labelDuracion = tk.Label(self,text='Duracion: ')
        self.labelDuracion.config(font=('Arial',12,'bold'))
        self.labelDuracion.grid(row = 1, column = 0, padx = 10 , pady = 10)

        self.labelGenero = tk.Label(self,text='Genero: ')
        self.labelGenero.config(font=('Arial',12,'bold'))
        self.labelGenero.grid(row = 2, column = 0, padx = 10 , pady = 10)

        #entrys de campos
        self.miNombre = tk.StringVar()#Esta es la variable que guarda lo que se escriba
        self.entryNombre = tk.Entry(self, textvariable = self.miNombre) 
        self.entryNombre.config(width = 50, font=('Arial',12))
        self.entryNombre.grid(row=0, column=1, padx = 10 , pady = 10,columnspan=2)
        self.miDuracion = tk.StringVar()#Esta es la variable que guarda lo que se escriba
        self.entryDuracion = tk.Entry(self, textvariable = self.miDuracion)
        self.entryDuracion.config(width = 50, font=('Arial',12))
        self.entryDuracion.grid(row=1, column=1, padx = 10 , pady = 10,columnspan=2)
        self.miGenero = tk.StringVar() #Esta es la variable que guarda lo que se escriba
        self.entryGenero = tk.Entry(self, textvariable= self.miGenero)
        self.entryGenero.config(width = 50, font=('Arial',12))
        self.entryGenero.grid(row=2, column=1, padx = 10 , pady = 10,columnspan=2)

#se puede agregar los botones dentro del metodo de arriba
    def botones(self):
        self.botonNuevo = tk.Button(self,text='Nuevo',command=self.habilitarCampos)
        self.botonNuevo.config(width = 20, font=('Arial',12,'bold'),fg='#FFFFFF',
         bg='#1AD607', cursor='hand2', activebackground='#159708', activeforeground='#FFFFFF')
        self.botonNuevo.grid(row=3, column=0, padx = 10 , pady = 10)

        self.botonGuardar = tk.Button(self,text='Guardar', command=self.guardarDatos)
        self.botonGuardar.config(width = 20, font=('Arial',12,'bold'),fg='#FFFFFF',
         bg='#0C74E9', cursor='hand2', activebackground='#0A52A2', activeforeground='#FFFFFF')
        self.botonGuardar.grid(row=3, column=1, padx = 10 , pady = 10)

        
        self.botonCancelar = tk.Button(self,text='Cancelar', command=self.deshabilitarCampos)
        self.botonCancelar.config(width = 20, font=('Arial',12,'bold'),fg='#FFFFFF',
         bg='#EC0A0A', cursor='hand2', activebackground='#B30A0A', activeforeground='#FFFFFF')
        self.botonCancelar.grid(row=3, column=2, padx = 10 , pady = 10)

    def habilitarCampos(self):
        self.miNombre.set('')
        self.miDuracion.set('')
        self.miGenero.set('')
         
        self.entryNombre.config(state='normal')
        self.entryDuracion.config(state='normal')
        self.entryGenero.config(state='normal')

        self.botonGuardar.config(state='normal')
        self.botonCancelar.config(state='normal')

    def deshabilitarCampos(self):
        
        self.miNombre.set('')
        self.miDuracion.set('')
        self.miGenero.set('')
         

        self.entryNombre.config(state='disable')
        self.entryDuracion.config(state='disable')
        self.entryGenero.config(state='disable')

        self.botonGuardar.config(state='disable')
        self.botonCancelar.config(state='disable')
        self.idPelicula= None

    def guardarDatos(self):
        pelicula = Pelicula(
        self.miNombre.get(),
        self.miDuracion.get(),
        self.miGenero.get(),
        )
        if self.idPelicula == None:
          guardarDatos(pelicula)
        else:
              editar(pelicula, self.idPelicula)

        
        self.deshabilitarCampos()
        self.tablaPeliculas()
     
    def tablaPeliculas(self):
        self.lista_peliculas = listar()
        self.lista_peliculas.reverse() # hace que se ordenen
        self.tabla = ttk.Treeview(self, 
        columns=('Nombre', 'Duracion', 'Genero') )
        self.tabla.grid(row= 4, column = 0, columnspan=4, sticky='nse')

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Nombre')
        self.tabla.heading('#2', text='Duracion')
        self.tabla.heading('#3', text='Genero')
    # ITERAR LA LISTA DE PELICULAS
        for p in self.lista_peliculas:
         self.tabla.insert('', 0, text= p[0],
         values=(p[1], p[2], p[3]))

        #  scrollbar par ala tabla si excede los 10 registros
        self.scroll = ttk.Scrollbar(self,
        orient= 'vertical', command=self.tabla.yview)
        self.scroll.grid(row = 4, column = 4, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.botonEditar = tk.Button(self,text='Editar', command=self.editarDatos)
        self.botonEditar.config(width = 20, font=('Arial',12,'bold'),fg='#FFFFFF',
         bg='#1AD607', cursor='hand2', activebackground='#159708', activeforeground='#FFFFFF')
        self.botonEditar.grid(row=5, column=0, padx = 10 , pady = 10)


        self.botonEliminar = tk.Button(self,text='Eliminar', command=self.eliminarDatos)
        self.botonEliminar.config(width = 20, font=('Arial',12,'bold'),fg='#FFFFFF',
         bg='#EC0A0A', cursor='hand2', activebackground='#B30A0A', activeforeground='#FFFFFF')
        self.botonEliminar.grid(row=5, column=1, padx = 10 , pady = 10)

    def editarDatos(self):
         try: 
            self.idPelicula = self.tabla.item(self.tabla.selection())['text']
            self.nombrePelicula = self.tabla.item(
                self.tabla.selection())['values'][0]
        
            self.duracionPelicula = self.tabla.item(
                self.tabla.selection())['values'][1]
            
            self.generoPelicula = self.tabla.item(
                self.tabla.selection())['values'][2]
            
            self.habilitarCampos()

            self.entryNombre.insert(0, self.nombrePelicula)
            self.entryDuracion.insert(1, self.duracionPelicula)
        
            self.entryGenero.insert(2, self.generoPelicula)
         except:
              titulo = 'Edicion de Datos'
              mensaje = 'No a seleccionado ningun registro'
              messagebox.showerror(titulo, mensaje)
    def eliminarDatos(self):
           try:
           
            self.idPelicula2 = self.tabla.item(self.tabla.selection())['text']
            
          
             # NOTA: Yo cree la variable id pelicula 2 pero tambien se puede usar la misma
             # solo que al final debo declararla nuevamnete como none
            
            eliminar(self.idPelicula2)
            
            self.tablaPeliculas()
            

          
           except:
               titulo = 'Eliminar Datos'
               mensaje = 'No a seleccionado ningun registro'
               messagebox.showerror(titulo, mensaje)
       
