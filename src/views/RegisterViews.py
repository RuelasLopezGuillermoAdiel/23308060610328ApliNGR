import flet as ft
import re
from models.schemasModel import UsuarioSchema

def RegisterView(page: ft.Page, auth_controller):

   
    page.bgcolor = "#0b1120"
    page.theme_mode = ft.ThemeMode.DARK

    
    estilo_inputs = {
        "width": 420,
        "height": 58,
        "border_radius": 14,
        "bgcolor": "#111827",
        "border_color": "#334155",
        "focused_border_color": "#3b82f6",
        "color": "white",
    }

    nombre = ft.TextField(
        label="Nombre(s)",
        prefix_icon=ft.Icons.PERSON_ROUNDED,
        **estilo_inputs
    )

    apellido = ft.TextField(
        label="Apellidos",
        prefix_icon=ft.Icons.PERSON_OUTLINE_ROUNDED,
        **estilo_inputs
    )

    email = ft.TextField(
        label="Correo electrónico",
        prefix_icon=ft.Icons.EMAIL_ROUNDED,
        keyboard_type=ft.KeyboardType.EMAIL,
        **estilo_inputs
    )

    password = ft.TextField(
        label="Contraseña",
        prefix_icon=ft.Icons.LOCK_ROUNDED,
        password=True,
        can_reveal_password=True,
        **estilo_inputs
    )

    confirm_password = ft.TextField(
        label="Confirmar contraseña",
        prefix_icon=ft.Icons.LOCK_OUTLINE_ROUNDED,
        password=True,
        can_reveal_password=True,
        **estilo_inputs
    )

    mensaje = ft.Text(
        "",
        color="#ef4444",
        size=13
    )

   
    def mostrar_snackbar(mensaje_texto, color="#16a34a"):

        page.snack_bar = ft.SnackBar(
            content=ft.Text(
                mensaje_texto,
                color="white"
            ),

            bgcolor=color,
            duration=2000,
        )

        page.snack_bar.open = True
        page.update()

    
    def registrar_click(e):

        if not nombre.value or not email.value or not password.value or not confirm_password.value:

            mensaje.value = "Todos los campos son obligatorios"
            mensaje.color = "#ef4444"

            page.update()
            return

        if password.value != confirm_password.value:

            mensaje.value = "Las contraseñas no coinciden"
            mensaje.color = "#ef4444"

            page.update()
            return

        if len(password.value) < 6:

            mensaje.value = "La contraseña debe tener al menos 6 caracteres"
            mensaje.color = "#ef4444"

            page.update()
            return

        if not re.match(
            r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
            email.value
        ):

            mensaje.value = "Correo electrónico inválido"
            mensaje.color = "#ef4444"

            page.update()
            return

        usuario_data = UsuarioSchema(
            nombre=nombre.value,
            apellido=apellido.value,
            email=email.value,
            password=password.value
        )

        exito, msg = auth_controller.registrar(usuario_data)

        if exito:

            mostrar_snackbar(
                "¡Registro exitoso! Ahora inicia sesión",
                "#16a34a"
            )

            nombre.value = ""
            apellido.value = ""
            email.value = ""
            password.value = ""
            confirm_password.value = ""
            mensaje.value = ""

            page.update()
            page.go("/")

        else:

            mensaje.value = msg or "Error al registrar usuario"
            mensaje.color = "#ef4444"

            page.update()

    def ir_login(e):
        page.go("/")

    
    btn_registrar = ft.ElevatedButton(
        "Registrarse",
        icon=ft.Icons.PERSON_ADD,
        width=260,
        height=55,
        on_click=registrar_click,

        style=ft.ButtonStyle(
            bgcolor="#22c55e",
            color="white",
            padding=20,
            shape=ft.RoundedRectangleBorder(radius=14),
        ),
    )

   
    btn_login = ft.TextButton(
        "¿Ya tienes cuenta? Inicia sesión",

        on_click=ir_login,

        style=ft.ButtonStyle(
            color="#38bdf8",
            overlay_color="#1e293b"
        )
    )

    return ft.View(

        route="/register",

        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,

        appbar=ft.AppBar(

            title=ft.Text(
                "SIGE - Registro",
                weight="bold"
            ),

            bgcolor="#111827",
            center_title=True,
            color="white",

            leading=ft.IconButton(
                ft.Icons.ARROW_BACK,
                icon_color="white",
                on_click=lambda _: page.go("/")
            )
        ),

        controls=[

            ft.Container(

                width=540,
                padding=35,

                border_radius=25,

                bgcolor="#111827",

                border=ft.border.all(
                    1,
                    "#1e293b"
                ),

                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=18,
                    color="#00000055",
                    offset=ft.Offset(0, 5)
                ),

                content=ft.Column(

                    spacing=16,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,

                    controls=[

                       
                        ft.Container(
                            width=95,
                            height=95,

                            border_radius=50,

                            bgcolor="#16a34a",

                            alignment=ft.alignment.center,

                            content=ft.Icon(
                                ft.Icons.PERSON_ADD_ALT_1,
                                size=50,
                                color="white"
                            )
                        ),

                        ft.Text(
                            "Crear Nueva Cuenta",
                            size=30,
                            weight="bold",
                            color="white"
                        ),

                        ft.Text(
                            "Completa los datos para registrarte",
                            size=14,
                            color="#94a3b8"
                        ),

                        ft.Container(height=5),

                        nombre,
                        apellido,
                        email,
                        password,
                        confirm_password,

                        mensaje,

                        ft.Container(height=5),

                        btn_registrar,

                        btn_login
                    ]
                )
            )
        ]
    )
