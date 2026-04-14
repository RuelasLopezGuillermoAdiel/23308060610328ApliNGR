import flet as ft
from controllers.UsiarioController import AuthController
from controllers.TareasController import TareaController
from views.LoginViews import LoginView
from views.Dashboard import DashboardView

#uv sync
def start(page: ft.Page):
    auth_ctrl = AuthController()
    task_ctrl = TareaController()
    
    def route_change(e):
        page.views.clear()
        if page.route == "/":
            
            page.views.append(LoginView(page,task_ctrl))
        elif page.route == "/dashboard":
            page.views.append(DashboardView(page, task_ctrl))
            
        page.update()
    page.on_route_change = route_change
    page.go("/")
    
def main():
    ft.app(target=start)
    
if __name__=="__main__":
    ft.run(main)