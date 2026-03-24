from src.models.UserModel import UsuarioModel
from src.models.schemaModel import UsuarioSchema
from pydantic import ValidationError

class AuthController:
    def __init__(self):
        self.model=UsuarioModel()
        
    def registrar_usuario(self, nombre, email, password):
        try:
            nuevo_usuario = UsuarioSchema(nombre=nombre, email=email, password=password)
            succes = self.model.registrar(nuevo_usuario)
            return succes, "Usuario creado correctamente"
    except ValidationError as e:
        
        return False, e,error()[0]['msg']