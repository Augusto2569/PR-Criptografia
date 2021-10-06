
from password import Password

class PasswordList():
    """Lista de todas las contraseñas """

    def __init__(self):
        self.passwords = {} #podemos ponerlo como un diccionario y buscarlo por user_id 


    #Jorge: yo aquí metería los atributos a mano y dentro de la función crearía un objeto password
    def add_password(self,user_id:int, username:str, password:str,security_questions:str, notes:str ):
        """Añadir contraseña a la lista de contraseñas"""

        pswd = Password(user_id,username, password,security_questions, notes) #aquí igual sobra guardar la info del user_id dos veces
        self.passwords[user_id] = pswd #aquí podríamos meterlo en una lista, porque el usuario querrá almacenar + de 1 password
        return


    def delete_password(self, user_id:int):
        """Eliminar una contraseña de la lista"""
        #aquí es útil user_id porque podemos identificarle para buscarle y borrarlo
        self.passwords[user_id].password = ""
    

    def check_password(self,input:str,password:str): 
        """Método auxiliar para comprobar si coincide la contraseña introducida con la real"""
        return(input == password)

    def modify_password(self, user_id:int,input_old_password:str, real_old_password:str, new_password:str):
        """Modificar una contraseña de la lista"""
        #para borrar la contraseña, tiene que conocer la antigua antes
        bool = False
        print("Introduzca la contraseña antigua para borrar la nueva:\n")
        bool = self.check_password(input_old_password,real_old_password)
        if bool:
            print("Contraseña correcta. Puede proceder a cambiar su contraseña")
        else:
            print("Error")
            return False #error al cambiar la contraseña

        #contraseña antigua reconocida
        print("Introduzca la nueva contraseña")
        
        self.passwords[user_id].password = new_password #cambiamos la contraseña
        return True #éxito


    def view_all_passwords(self):
        """Visualizar todas las contraseñas de la lista"""
        for user in self.passwords:
            print("User: %s, password: %s\n",self.passwords[user],self.passwords[user].password)
        