from app.database import get_db

class Producto:
    #CONSTRUCTOR
    def __init__(self,id_producto=None,categoría=None,nombre=None,material=None,descripción=None,precio=None,foto=None):
        self.id_producto = id_producto
        self.categoría = categoría
        self.nombre = nombre
        self.material = material
        self.descripción= descripción
        self.precio=precio
        self.foto= foto

    @staticmethod    
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM productos")
        rows = cursor.fetchall()
        # movies = []
        productos = [Producto(id_producto=row[0], categoría=row[1], nombre=row[2], material=row[3], descripción=row[4],precio=row[5],foto=row[6]) for row in rows]
        # for row in rows:
        #     new_movie =  Movie(row[0],row[1],row[2],row[3],row[4])
        #     movies.append(new_movie)
        cursor.close()
        return productos

        #def save(self):
        #logica para INSERT/UPDATE en base datos
         #       pass

        #def delete(self):
        #logica para hacer un DELETE en la BASE
        pass
        #logica para hacer un DELETE en la BASE
         #        pass


    def serialize(self):
        return {
           'id_producto': self.id_producto,
           'categoría': self.categoría,
           'nombre': self.nombre,
           'material': self.material,
           'descripción': self.descripción,
           'precio': self.precio,
           'foto': self.foto,
                }
    
    