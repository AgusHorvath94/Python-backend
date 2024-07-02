from app.database import get_db

class Usuario:
    # Constructor
    def __init__(self, id_usuario=None, nombre=None, apellido=None, email=None, contraseña=None, nacimiento=None):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contraseña = contraseña
        self.nacimiento = nacimiento

    def serialize(self):
        return {
            'id_usuario': self.id_usuario,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            'contraseña': self.contraseña,
            'nacimiento': self.nacimiento,
        }

    @staticmethod
    def get_all():
        # Lógica de buscar en la base todos los usuarios
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM register"
        cursor.execute(query)
        # Obtengo resultados
        rows = cursor.fetchall()
        usuarios = [Usuario(id_usuario=row[0], nombre=row[1], apellido=row[2], email=row[3], contraseña=row[4], nacimiento=row[5]) for row in rows]
        # Cerramos el cursor
        cursor.close()
        return usuarios
    
    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id_usuario:
            cursor.execute("""
                UPDATE register SET nombre = %s, apellido = %s, email = %s, contraseña = %s, nacimiento = %s
                WHERE id_usuario = %s
            """, (self.nombre, self.apellido, self.email, self.contraseña, self.nacimiento, self.id_usuario))
        else:
            cursor.execute("""
                INSERT INTO register (nombre, apellido, email, contraseña, nacimiento) VALUES (%s, %s, %s, %s, %s)
            """, (self.nombre, self.apellido, self.email, self.contraseña, self.nacimiento))           
            # Voy a obtener el último id generado
            self.id_usuario = cursor.lastrowid
        db.commit()  # Confirmar acción
        cursor.close()
        return self

    @staticmethod
    def get_by_id(usuario_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM register WHERE id_usuario = %s", (usuario_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Usuario(id_usuario=row[0], nombre=row[1], apellido=row[2], email=row[3], contraseña=row[4], nacimiento=row[5])
        return None
    
    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM register WHERE id_usuario = %s", (self.id_usuario,))
        db.commit()
        cursor.close()