def LoginView(pago, auth_controller):
    email_input = ft.TextField(label = "Correo electronico", width=350, border_radius=10)
    pass_input = ft.TextField(label = "Contraseña",password=True, can_reveal_password=True, width=150, border_radius=10)
    
    def login_click(e):
        user, nsg = auth_controller.login(email_input.value, pass_input.value)
        if user:
            page.session.set("user", user) 
            page.go("/dashboard")
        else:
            page.snack_bar = ft.SnackBar(ft.Text(msg))
            page.snack_bar.open = True
            page.update()
            
    return ft.View("/", [
        ft.AppBar(title=ft.Text("SIGE - Login"), bgcolor=ft.Colors.blue_grey_900, color="white"),
        ft. Column([
            ft.icon(ft.icons.LOCK_PERSON, size=50, color=ft.Colors.blue),
            ft.Text("Acceso al Sistema", size=24, weight="bold"),
            email_input,
            pass_input,
            ft.ElevatedButton("Entrar",  on_click=login_click, width=350),
            fr.TextButton("Crear una cuenta nueva", on_click=lambda _: page.go("/registro"))
            
        ], horizontal_alignment=ft.CrossAxisAlignnment.CENTER, alignment=ft.MainAxisAlignment.CENTER)
    ])
    

    AGREGAR .env





#user model 
        
        
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


#Databasemodel

import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    @staticmethod
    def get_connection():
        try:
            connection = mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME")
            )
        
            if connection.is_connected():
                return connection
            
            except mysql.connector.Error as err: