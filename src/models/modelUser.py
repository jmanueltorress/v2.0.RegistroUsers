from models import *
class modelUser():

    @classmethod
    def login(self,db,user):
        try:
            cursor=db.connection.cursor()
            sql="""SELECT id, Matricula, password, Nombre FROM usuarios WHERE Matricula='{}'""".format(user.Matricula)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row!=None:
                user=User(row[0],row[1],User.check_password(row[7],user.password), row[2])
                return user

            else:
                return None 
        except Exception as ex:
            raise Exception(ex)