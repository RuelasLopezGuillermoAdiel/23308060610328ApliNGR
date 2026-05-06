import flet as ft

def LoginView(page: ft.Page, auth_controller):
    
    # 🎨 FONDO GENERAL
    page.bgcolor = "#0f172a"
    page.theme_mode = ft.ThemeMode.DARK
    
    correo = ft.TextField(
        label="Correo electrónico",
        prefix_icon=ft.Icons.PERSON,
        width=500,
        border_radius=8,
        keyboard_type=ft.KeyboardType.EMAIL,
        bgcolor="#1e293b",
        color="white"
    )

    contraseña = ft.TextField(
        label="Contraseña",
        prefix_icon=ft.Icons.KEY,
        password=True,
        can_reveal_password=True,
        width=500,
        border_radius=8,
        bgcolor="#1e293b",
        color="white"
    )
    
    mensaje = ft.Text("", color="#ef4444")  # rojo suave

    def mostrar_snackbar(mensaje_texto, color="#16a34a"):
        page.snack_bar = ft.SnackBar(
            content=ft.Text(mensaje_texto, color="white"),
            bgcolor=color,
            duration=2000,
        )
        page.snack_bar.open = True
        page.update()

    def login_click(e):
        if not correo.value or not contraseña.value:
            mensaje.value = "Por favor, llene todos los campos"
            mensaje.color = "#ef4444"
            page.update()
            return
        
        user, msg = auth_controller.login(correo.value, contraseña.value)
        if user:
            page.user_data = user
            mostrar_snackbar("¡Sesión iniciada correctamente!", "#16a34a")
            page.go("/dashboard")
        else:
            mensaje.value = msg
            mensaje.color = "#ef4444"
            page.update()

    iniciar_sesion = ft.ElevatedButton(
        "Iniciar sesión",
        width=250,
        on_click=login_click,
        style=ft.ButtonStyle(
            bgcolor="#2563eb",  # azul principal
            color="white",
            padding=20,
            shape=ft.RoundedRectangleBorder(radius=12),
        ),
    )
    
    btn_registro = ft.TextButton(
        "¿No tienes cuenta? Regístrate",
        on_click=lambda _: page.go("/register"),
        style=ft.ButtonStyle(color="#38bdf8")  # azul claro
    )
    
    contraseña.on_submit = login_click

    return ft.View(
        route="/",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        appbar=ft.AppBar(
            title=ft.Text("SIGE - Login"),
            bgcolor="#1e293b",
            color="white"
        ),
        controls=[
            ft.Column(
                [
                    ft.Text("Acceso al Sistema", size=24, weight="bold", color="white"),
                    ft.Container(height=10),
                    correo,
                    ft.Container(height=10),
                    contraseña,
                    ft.Container(height=10),
                    mensaje,
                    ft.Container(height=10),
                    ft.Row(
                        [iniciar_sesion],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Container(height=10),
                    btn_registro
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                tight=True,
                spacing=10
            )
        ]
    )
