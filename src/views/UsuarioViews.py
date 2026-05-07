import flet as ft

def UserView(page, auth_controller):
    page.title = "Perfil"
    
    
    page.bgcolor = "#0f172a"
    page.theme_mode = ft.ThemeMode.DARK
    
    user = getattr(page, "user_data", None)
    
    nombre = ft.Text(f"Nombre: {user['nombre'] if user else 'Usuario'}", size=20, color="white")
    apellido = ft.Text(f"Apellido: {user['apellido'] if user else 'Usuario'}", size=20, color="white")
    email = ft.Text(f"Email: {user['email'] if user else 'Usuario'}", size=20, color="white")
    fecha_registro = ft.Text(f"Fecha de creacion de la cuenta: {user['fecha_registro'] if user else 'Usuario'}", size=20, color="white")
    ultimo_acceso = ft.Text(f"Último acceso: {user['ultimo_acceso'] if user else 'Usuario'}", size=20, color="white")

    return ft.View(
        route="/perfil",
        controls=[
            ft.AppBar(
                title=ft.Text("Perfil de Usuario", size=30),
                bgcolor="#1e293b",
                color="white",
                actions=[
                    ft.IconButton(ft.Icons.BOOK, icon_color="#38bdf8", on_click=lambda _: page.go("/dashboard")),
                    ft.IconButton(ft.Icons.EXIT_TO_APP, icon_color="#ef4444", on_click=lambda _: page.go("/"))
                ],
            ),
            ft.Container(
                ft.Column([
                    ft.Divider(thickness=8, color="#2563eb"),
                    ft.Row([nombre]),
                    ft.Divider(thickness=6, color="#2563eb"),
                    ft.Row([apellido]),
                    ft.Divider(thickness=6, color="#2563eb"),
                    ft.Row([email]),
                    ft.Divider(thickness=6, color="#2563eb"),
                    ft.Divider(thickness=8, color="#2563eb"),
                    ft.Row([fecha_registro]),
                    ft.Divider(thickness=8, color="#2563eb"),
                    ft.Row([ultimo_acceso]),
                ], expand=True),
                padding=20,
                expand=True,
                bgcolor="#1e293b" 
            ),
        ]
    )
