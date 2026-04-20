import flet as ft 

def LoginView(page: ft.Page, auth_controller):
    email_input = ft.TextField(
        label="Correo electronico".
        width=150,
        border_radius=10,
        keyboard_type=ft.KeyboardType
    )
    
    pass_input = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        width=350,
        border_radius=10
    )
    
    def login_click(e):
        if not gmail.input.value