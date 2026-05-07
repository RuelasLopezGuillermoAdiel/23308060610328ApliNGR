import flet as ft

def LoginView(page: ft.Page, auth_controller):

    
    page.bgcolor = "#0b1120"
    page.theme_mode = ft.ThemeMode.DARK

   
    correo = ft.TextField(
        label="Correo electrónico",
        prefix_icon=ft.Icons.EMAIL_ROUNDED,
        width=430,
        height=58,
        border_radius=14,
        keyboard_type=ft.KeyboardType.EMAIL,
        bgcolor="#111827",
        border_color="#334155",
        focused_border_color="#3b82f6",
        color="white",
    )

   
    contraseña = ft.TextField(
        label="Contraseña",
        prefix_icon=ft.Icons.LOCK_ROUNDED,
        password=True,
        can_reveal_password=True,
        width=430,
        height=58,
        border_radius=14,
        bgcolor="#111827",
        border_color="#334155",
        focused_border_color="#3b82f6",
        color="white",
    )

    mensaje = ft.Text(
        "",
        color="#ef4444",
        size=14
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

    
    def login_click(e):

        if not correo.value or not contraseña.value:

            mensaje.value = "Por favor, llene todos los campos"
            mensaje.color = "#ef4444"

            page.update()
            return

        user, msg = auth_controller.login(
            correo.value,
            contraseña.value
        )

        if user:

            page.user_data = user

            mostrar_snackbar(
                "¡Sesión iniciada correctamente!",
                "#16a34a"
            )

            page.go("/dashboard")

        else:

            mensaje.value = msg
            mensaje.color = "#ef4444"

            page.update()

   
    iniciar_sesion = ft.ElevatedButton(
        "Iniciar sesión",
        icon=ft.Icons.LOGIN,
        width=260,
        height=55,
        on_click=login_click,

        style=ft.ButtonStyle(
            bgcolor="#2563eb",
            color="white",
            padding=20,
            shape=ft.RoundedRectangleBorder(radius=14),
        ),
    )

    
    btn_registro = ft.TextButton(
        "¿No tienes cuenta? Regístrate",

        on_click=lambda _: page.go("/register"),

        style=ft.ButtonStyle(
            color="#38bdf8",
            overlay_color="#1e293b"
        )
    )

    contraseña.on_submit = login_click

    return ft.View(

        route="/",

        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,

        appbar=ft.AppBar(

            title=ft.Text(
                "SIGE - Login",
                weight="bold"
            ),

            bgcolor="#111827",
            center_title=True,
            color="white"
        ),

        controls=[

            ft.Container(

                width=520,
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

                    spacing=18,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,

                    controls=[

                       
                        ft.Container(
                            width=90,
                            height=90,

                            border_radius=50,

                            bgcolor="#1d4ed8",

                            alignment=ft.alignment.center,

                            content=ft.Icon(
                                ft.Icons.PERSON,
                                size=45,
                                color="white"
                            )
                        ),

                        ft.Text(
                            "Acceso al Sistema",
                            size=30,
                            weight="bold",
                            color="white"
                        ),

                        ft.Text(
                            "Inicia sesión para continuar",
                            size=14,
                            color="#94a3b8"
                        ),

                        ft.Container(height=5),

                        correo,

                        contraseña,

                        mensaje,

                        ft.Container(height=5),

                        ft.Row(
                            [iniciar_sesion],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),

                        btn_registro
                    ]
                )
            )
        ]
    )
