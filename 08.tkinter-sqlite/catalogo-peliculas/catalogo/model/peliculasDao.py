from .conexionDB import conexionDB
from tkinter import messagebox

def crearTabla():
    conexion = conexionDB()

    sql = ''' 
    CREATE TABLE peliculas(
    id_pelicula INTEGER,
    nombre VARCHAR(100),
    duracion VARCHAR(10),
    genero VARCHAR(100),
    PRIMARY KEY(id_pelicula AUTOINCREMENT)
    )
    ''' 
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarDB()
        titulo = 'Crear Registro'
        mensaje = 'Se creo la tabla en la DB'
        messagebox.showinfo(titulo,mensaje)
    except:
        titulo = 'Crear Registro'
        mensaje = 'Error ya existe la tabla en la DB'
        messagebox.showwarning(titulo, mensaje)
        


def borrarTabla():
    try:
        conexion = conexionDB()
        sql = 'DROP TABLE peliculas'
        conexion.cursor.execute(sql)
        conexion.cerrarDB()
        titulo = 'Eliminar Registro'
        mensaje = 'Se Elimino la tabla de la DB'
        messagebox.showinfo(titulo,mensaje)
    except:
        titulo = 'Eliminar Registro'
        mensaje = 'No hay tabla para borrar'
        messagebox.showwarning(titulo, mensaje)

class Pelicula:
    def __init__(self, nombre, duracion, genero):
        self.id_pelicula= None
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero
        

    def __str__(self):
        return f'Pelicula[{self.nombre}, {self.duracion}, {self.genero}]'


def guardarDatos(pelicula):
    conexion = conexionDB()

    sql = f'''INSERT INTO peliculas (nombre,duracion,genero)
     VALUES('{pelicula.nombre}', '{pelicula.duracion}','{pelicula.genero}')
     '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarDB()
        
    except:
        titulo = 'Guardar Registro'
        mensaje = 'Error no existe la tabla'
        messagebox.showerror(titulo, mensaje)
    

def listar():
    conexion = conexionDB()
    lista_peliculas= []
    sql = 'SELECT * FROM peliculas'
    try:
        conexion.cursor.execute(sql)
        lista_peliculas= conexion.cursor.fetchall()
        conexion.cerrarDB()
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'Crea la tabla en la DB'
        messagebox.showerror(titulo, mensaje)
    return lista_peliculas

    
def editar(pelicula,idPelicula):
    conexion = conexionDB()
    sql = f''' UPDATE peliculas 
    SET nombre = '{pelicula.nombre}', duracion='{pelicula.duracion}',genero='{pelicula.genero}'
    WHERE id_pelicula = {idPelicula}
    '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarDB()
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'No existe el registro'
        messagebox.showerror(titulo, mensaje)
    
def eliminar(idPelicula2):
    conexion = conexionDB()
    sql = f'''DELETE FROM peliculas WHERE id_pelicula = {idPelicula2} '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarDB()
    except:
        titulo = 'Eliminar Registro'
        mensaje = 'No existe el registro'
        messagebox.showerror(titulo, mensaje)