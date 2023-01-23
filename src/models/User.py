from werkzeug.security import check_password_hash 
# ,generate_password_hash

class User():
    def __init__(self,id, Matricula, password, Nombre="") -> None:
        self.id=id
        self.Matricula=Matricula
        self.password=password
        self.Nombre=Nombre
        
    def check_password(self,hashed_password,password):
        return check_password_hash(hashed_password, password)
# print(generate_password_hash("UserVerify"))