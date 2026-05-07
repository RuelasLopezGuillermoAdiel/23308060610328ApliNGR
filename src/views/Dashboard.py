import flet as ft
from datetime import datetime

def DashboardView(page, tarea_controller):
    user = getattr(page, "user_data", None)

   
    page.bgcolor = "#0b1120"
    page.theme_mode = ft.ThemeMode.DARK

    lista_tareas = ft.Column(
        scroll=ft.ScrollMode.ALWAYS,
        expand=True,
        spacing=15
    )

    fecha_limite = ft.DatePicker(
        first_date=datetime(2000, 1, 1),
        last_date=datetime(2030, 12, 31)
    )

    hora_limite = ft.TimePicker()

    page.overlay.append(fecha_limite)
    page.overlay.append(hora_limite)

    def abrir_calendario(e):
        fecha_limite.open = True
        page.update()

    def abrir_reloj(e):
        hora_limite.open = True
        page.update()

    
    estilo_btn = ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=12),
        padding=20,
    )

    btn_fecha = ft.ElevatedButton(
        "Seleccionar Fecha",
        icon=ft.Icons.CALENDAR_MONTH,
        on_click=abrir_calendario,
        bgcolor="#3b82f6",
        color="white",
        style=estilo_btn
    )

    btn_hora = ft.ElevatedButton(
        "Seleccionar Hora",
        icon=ft.Icons.ACCESS_TIME,
        on_click=abrir_reloj,
        bgcolor="#3b82f6",
        color="white",
        style=estilo_btn
    )

    txt_fecha_seleccionada = ft.Text(
        "Fecha: No seleccionada",
        color="#cbd5e1"
    )

    txt_hora_seleccionada = ft.Text(
        "Hora: No seleccionada",
        color="#cbd5e1"
    )

    def actualizar_fecha(e):
        if fecha_limite.value:
            txt_fecha_seleccionada.value = f"Fecha: {fecha_limite.value.strftime('%d/%m/%Y')}"
        else:
            txt_fecha_seleccionada.value = "Fecha: No seleccionada"
        page.update()

    def actualizar_hora(e):
        if hora_limite.value:
            txt_hora_seleccionada.value = f"Hora: {hora_limite.value.strftime('%H:%M')}"
        else:
            txt_hora_seleccionada.value = "Hora: No seleccionada"
        page.update()

    fecha_limite.on_change = actualizar_fecha
    hora_limite.on_change = actualizar_hora

    def eliminar_tarea(id_tarea):
        success, msg = tarea_controller.eliminar_tarea(id_tarea)
        if success:
            cargar_tareas()
        else:
            page.snack_bar = ft.SnackBar(
                ft.Text(msg),
                bgcolor="#dc2626"
            )
            page.snack_bar.open = True
            page.update()

    def cargar_tareas():
        if user and 'id_usuario' in user:
            lista_tareas.controls.clear()
            tareas = tarea_controller.obtener_lista(user['id_usuario'])

            for t in tareas:
                fecha_limite_texto = t.get('fecha_limite', '')
                fecha_texto = f"\nFecha límite: {formatear_fecha_limite(fecha_limite_texto)}" if fecha_limite_texto else ""

                hora_limite_val = t.get('hora_limite', '')
                hora_texto = f" | Hora: {hora_limite_val}" if hora_limite_val else ""

                lista_tareas.controls.append(
                    ft.Container(
                        border_radius=18,
                        bgcolor="#111827",
                        padding=15,
                        border=ft.border.all(1, "#1e293b"),
                        shadow=ft.BoxShadow(
                            spread_radius=1,
                            blur_radius=12,
                            color="#00000055",
                            offset=ft.Offset(0, 4)
                        ),
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.START,
                            controls=[
                                ft.Column(
                                    spacing=5,
                                    expand=True,
                                    controls=[
                                        ft.Text(
                                            t['titulo'],
                                            size=18,
                                            weight="bold",
                                            color="white"
                                        ),

                                        ft.Text(
                                            t.get('descripcion', ''),
                                            color="#cbd5e1",
                                            size=14
                                        ),

                                        ft.Row(
                                            wrap=True,
                                            spacing=10,
                                            controls=[
                                                ft.Container(
                                                    padding=8,
                                                    border_radius=10,
                                                    bgcolor="#1d4ed8",
                                                    content=ft.Text(
                                                        f"Prioridad: {t.get('prioridad', 'media')}",
                                                        size=12,
                                                        color="white"
                                                    )
                                                ),

                                                ft.Container(
                                                    padding=8,
                                                    border_radius=10,
                                                    bgcolor="#7c3aed",
                                                    content=ft.Text(
                                                        f"Categoría: {t.get('clasificacion', 'personal')}",
                                                        size=12,
                                                        color="white"
                                                    )
                                                ),

                                                ft.Container(
                                                    padding=8,
                                                    border_radius=10,
                                                    bgcolor="#059669",
                                                    content=ft.Text(
                                                        f"Estado: {t.get('estado', 'pendiente')}",
                                                        size=12,
                                                        color="white"
                                                    )
                                                ),
                                            ]
                                        ),

                                        ft.Text(
                                            f"{fecha_texto}{hora_texto}",
                                            color="#94a3b8",
                                            size=12
                                        )
                                    ]
                                ),

                                ft.IconButton(
                                    icon=ft.Icons.DELETE_ROUNDED,
                                    icon_color="#ef4444",
                                    bgcolor="#1e293b",
                                    on_click=lambda e, id_t=t['id_tarea']: eliminar_tarea(id_t)
                                )
                            ]
                        )
                    )
                )

            page.update()

    
    txt_titulo = ft.TextField(
        label="Título",
        expand=True,
        bgcolor="#111827",
        border_radius=15,
        border_color="#334155",
        color="white"
    )

    txt_descripcion = ft.TextField(
        label="Descripción",
        expand=True,
        multiline=True,
        max_lines=3,
        bgcolor="#111827",
        border_radius=15,
        border_color="#334155",
        color="white"
    )

    prioridad_dropdown = ft.Dropdown(
        label="Prioridad",
        value="media",
        width=170,
        bgcolor="#111827",
        border_radius=15,
        color="white",
        options=[
            ft.dropdown.Option("alta", "Alta"),
            ft.dropdown.Option("media", "Media"),
            ft.dropdown.Option("baja", "Baja"),
        ]
    )

    clasificacion_dropdown = ft.Dropdown(
        label="Clasificación",
        value="personal",
        width=170,
        bgcolor="#111827",
        border_radius=15,
        color="white",
        options=[
            ft.dropdown.Option("personal", "Personal"),
            ft.dropdown.Option("trabajo", "Trabajo"),
            ft.dropdown.Option("estudio", "Estudio"),
        ]
    )

    estado_dropdown = ft.Dropdown(
        label="Estado",
        value="pendiente",
        width=170,
        bgcolor="#111827",
        border_radius=15,
        color="white",
        options=[
            ft.dropdown.Option("pendiente", "Pendiente"),
            ft.dropdown.Option("en_progreso", "En Progreso"),
            ft.dropdown.Option("completada", "Completada"),
            ft.dropdown.Option("cancelada", "Cancelada"),
        ]
    )

    def agregar_tarea(e):
        if user and 'id_usuario' in user:

            if not txt_titulo.value:
                page.snack_bar = ft.SnackBar(
                    ft.Text("El título es obligatorio"),
                    bgcolor="#dc2626"
                )
                page.snack_bar.open = True
                page.update()
                return

            val_fecha = None
            val_hora = None

            if fecha_limite.value:
                val_fecha = fecha_limite.value.strftime('%Y-%m-%d')

            if hora_limite.value:
                val_hora = hora_limite.value.strftime('%H:%M:%S')

            success, msg = tarea_controller.guardar_nueva(
                user['id_usuario'],
                txt_titulo.value,
                txt_descripcion.value,
                prioridad_dropdown.value,
                clasificacion_dropdown.value,
                estado_dropdown.value,
                val_fecha,
                val_hora
            )

            if success:
                txt_titulo.value = ""
                txt_descripcion.value = ""
                fecha_limite.value = None
                hora_limite.value = None

                txt_fecha_seleccionada.value = "Fecha: No seleccionada"
                txt_hora_seleccionada.value = "Hora: No seleccionada"

                cargar_tareas()

                page.snack_bar = ft.SnackBar(
                    ft.Text(msg, color="white"),
                    bgcolor="#16a34a"
                )

                page.snack_bar.open = True
                page.update()

            else:
                page.snack_bar = ft.SnackBar(
                    ft.Text(msg, color="white"),
                    bgcolor="#dc2626"
                )

                page.snack_bar.open = True
                page.update()

    def formatear_fecha(fecha):
        if not fecha:
            return "No disponible"

        if isinstance(fecha, str) and ' ' in fecha:
            fecha_parte = fecha.split(' ')[0]
            hora_parte = fecha.split(' ')[1]
            año, mes, dia = fecha_parte.split('-')
            return f"{dia}/{mes}/{año} {hora_parte}"

        return str(fecha)

    def formatear_fecha_limite(fecha):
        if not fecha:
            return "Sin fecha límite"

        try:
            if isinstance(fecha, str):

                if ' ' in fecha:
                    fecha_parte = fecha.split(' ')[0]
                    hora_parte = fecha.split(' ')[1][:5]
                    año, mes, dia = fecha_parte.split('-')
                    return f"{dia}/{mes}/{año} {hora_parte}"

                else:
                    año, mes, dia = fecha.split('-')
                    return f"{dia}/{mes}/{año}"

        except:
            return str(fecha)

        return str(fecha)

    def mostrar_perfil(e):
        if not user:
            return

        dialogo = ft.AlertDialog(
            bgcolor="#111827",
            shape=ft.RoundedRectangleBorder(radius=20),

            title=ft.Text(
                "Perfil de Usuario",
                color="white",
                weight="bold"
            ),

            content=ft.Column([
                ft.Text(f"ID: {user.get('id_usuario', '')}", color="#cbd5e1"),
                ft.Text(f"Nombre: {user.get('nombre', '')}", color="#cbd5e1"),
                ft.Text(f"Apellido: {user.get('apellido', '')}", color="#cbd5e1"),
                ft.Text(f"Email: {user.get('email', '')}", color="#cbd5e1"),
                ft.Text(f"Fecha de registro: {formatear_fecha(user.get('fecha_registro'))}", color="#cbd5e1"),
                ft.Text(f"Último acceso: {formatear_fecha(user.get('ultimo_acceso'))}", color="#cbd5e1"),
            ], tight=True)
        )

        page.overlay.append(dialogo)
        dialogo.open = True
        page.update()

    cargar_tareas()

    return ft.View(
        route="/dashboard",

        controls=[
            ft.AppBar(
                title=ft.Text(
                    f"Hola, {user.get('nombre', 'Usuario') if user else 'Usuario'} 👋",
                    weight="bold"
                ),

                bgcolor="#111827",
                center_title=False,

                actions=[
                    ft.IconButton(
                        ft.Icons.PERSON,
                        icon_color="white",
                        on_click=mostrar_perfil
                    ),

                    ft.IconButton(
                        ft.Icons.EXIT_TO_APP,
                        icon_color="#ef4444",
                        on_click=lambda _: page.go("/")
                    )
                ],
            ),

            ft.Container(
                expand=True,
                padding=25,

                content=ft.Column(
                    spacing=20,
                    expand=True,

                    controls=[

                        ft.Container(
                            padding=20,
                            border_radius=20,
                            bgcolor="#111827",
                            border=ft.border.all(1, "#1e293b"),

                            content=ft.Column([
                                ft.Text(
                                    "Nueva Tarea",
                                    size=24,
                                    weight="bold",
                                    color="white"
                                ),

                                ft.Row([
                                    txt_titulo,
                                    txt_descripcion
                                ]),

                                ft.Row([
                                    prioridad_dropdown,
                                    clasificacion_dropdown,
                                    estado_dropdown,
                                ],
                                spacing=15,
                                wrap=True),

                                ft.Row([
                                    btn_fecha,
                                    btn_hora,
                                ],
                                spacing=15),

                                ft.Row([
                                    txt_fecha_seleccionada,
                                    txt_hora_seleccionada,
                                ],
                                spacing=20),

                                ft.ElevatedButton(
                                    "Guardar Tarea",
                                    icon=ft.Icons.SAVE,
                                    on_click=agregar_tarea,
                                    bgcolor="#22c55e",
                                    color="white",
                                    style=estilo_btn
                                ),
                            ])
                        ),

                        ft.Text(
                            "Mis Tareas",
                            size=24,
                            weight="bold",
                            color="white"
                        ),

                        lista_tareas
                    ]
                )
            )
        ]
    )
