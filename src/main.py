import flet as ft
from controllers.UserController import AuthController
from controllers.TareasController import TareaController
from views.LoginViews import LoginView
from views.Dashboard import DashboardView


def start(page: ft.Page):
    
    page.title = "SIstema SIGE"
    page.window:width = 450
    page.window_height = 700
    
    auth_ctrl = AuthController()
    task_ctrl = TareaController()

    def route_change(e):
        
        page.views.clear()
        
        if page.route == "/":
            page.views.append(LoginView(page,auth_ctrl))
        
        elif page.route == "/dashboard":
            page.views.append(DashboardView(page, task_ctrl))
                
        page.update()
    def view_pop(e):
        if len(page.views) > 1:
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    
    
    print("Iniciando navegacion...")
    if page.route == "/":
        route_change(None)
    else:
        page.go("/")
    
def main():
    ft.app(target=start)


# punto de entrada correcto
if __name__ == "__main__":
    ft.app(target=start)