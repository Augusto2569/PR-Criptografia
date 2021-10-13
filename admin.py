"""Esta idea me parece más fácil de implementar (todo en una única clase que hereda del resto)"""
from user import User
from password import Password
from password_list import PasswordList

class Admin(): 

    def __init__(self):
        self.users = []
        self.passwords = PasswordList()


    def add_user(self,user_name:str,password:str):
        user = User(user_name,password)
        self.users.append(user)
        self.passwords.password[user_name] = Password(0,user_name,password,"","") #obviamente esto hay que controlarlo y mejorarlo

    def delete_user(self,user_name:str):
        self.users.pop(self.user.index("user_name"))


    
    
