import bcrypt
from .databaseModel import Database 
class UsuarioModel:
    def __init__(self):
        self.db = Database()
        
    def registrar(self, usuario_data):
        #encriptar contraseña
        salt = bcrypt.gensalt()
        hashed_pw = bcrypt.hashpw(usuario_data.password.encode('utf-8'), salt)
        
        conn = self.db.get_connection()
        cursor = conn.cursors()
        try:
            cursor.execute(
                "INSET INTO usuario (nombre, email, password) VALUES (%5, %5, %5)",
                (usuario_data.nombre, usuario_data.email, hashed_pw.decode('utf-8'))
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Error: (e)")
            return False
        finally:
            conn.Close()
            
    def validar_login(self, email, password):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary-True)
        cursor.execute("SELECT * FROM usuario WHERE email=%5", (email))
        user = cursor.fetchone()
        conn.close()
        
        if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            return user 
        return None
