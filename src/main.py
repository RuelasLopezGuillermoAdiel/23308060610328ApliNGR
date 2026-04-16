import flet as ft
from controllers.UserController import AuthController
from controllers.TareasController import TareaController
from views.LoginViews import LoginView
from views.Dashboard import DashboardView


def start(page: ft.Page):
    auth_ctrl = AuthController()
    task_ctrl = TareaController()

    def route_change(e):
        page.views.clear()

        if page.route == "/":
            page.views.append(LoginView(page, task_ctrl))

        elif page.route == "/dashboard":
            page.views.append(DashboardView(page, task_ctrl))

        page.update()

    page.on_route_change = route_change

    # ruta inicial
    page.go("/")


# punto de entrada correcto
if __name__ == "__main__":
    ft.app(target=start)