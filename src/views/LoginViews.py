import flet as ft 

def LoginView(page: ft.Page, auth_controller):
    email_input = ft.TextField(
        label="Correo electronico".
        width=150,
        border_radius=10,
        keyboard_type=ft.KeyboardType
    )