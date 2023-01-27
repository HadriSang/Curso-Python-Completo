import sqlite3 

class conexionDB:
    def __init__(self):
        self.baseDatos = 'database/peliculas.db'
        self.conexion = sqlite3.connect(self.baseDatos)
        self.cursor = self.conexion.cursor()
    
    def cerrarDB(self):
        self.conexion.commit()
        self.conexion.close()
