import flet as ft
from src.controllers.UserController import AuthController
from src.controllers.TareaController import TareaController
from src.views.LoginView import LoginVIew
from src.views.dashboard import DashboardView

def main(page: ft.page):
    auth_ctrl = AuthController()
    task_ctrl = TareaController()
    
    def route_challenge(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(LoginView(page, auth_ctrl))
        elif page.route == "/dashboard":
            page.views.append(dashboardView(page, task_ctrl))
        
        page.update()
        
    page.on_route_change = route_change
    page.go("/")
    
if __name__=="__main__":
    ft.run(main)