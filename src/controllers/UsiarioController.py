from models.UserModel import UsuarioModel
from models.schemasModel import UsuarioSchema

class AuthController:
    def __init__(self):
        self.model = UsuarioModel()
        
    def registrar_usuario(self, nombre, email, password):
        try:
            
            nuevo_usuario = UsuarioSchema(nombre=nombre)
            sucess = self.model.registrar(nuevo_usuario)
            return sucess, "Usuario creado correctamente"
        except ValidationError as e:
            
            return False, e.errors()[0]['msg']