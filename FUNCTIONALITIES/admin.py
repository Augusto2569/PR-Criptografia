"""Esta idea me parece más fácil de implementar (todo en una única clase que hereda del resto)"""
from ELEMENTS import user
import time
import json


class Admin:
    def __init__(self):
        self.users = self.recover_json_information("./JSONS/app_users.json")["App_users"]
        self.external_accounts = self.recover_json_information("./JSONS/users_external_accounts.json")

    #versión para diccionario
    def add_user(self, user_name: str, password: str):
        try:
            # Si no hay error es que el usuario existe y por ello imprimimos el mensaje
            self.users[user_name]
            print("User already taken, choose another one.")
        except KeyError:
            self.users[user_name] = password
            external_accounts = self.recover_json_information("./JSONS/users_external_accounts.json")
            external_accounts[user_name] = {}
            self.save_users_information()

    def log_in_check_user(self, user_name, user_password):
        answer = [False, None]
        try:
            if (self.users[user_name] == user_password):
                answer[0] = True
                answer[1] = self.users #Ver como devolver la informacion del usuario
                return answer
            print("Error - User not registered!")
            return answer
            #si existe, está bien


        except KeyError:
            #no existe
            return answer

    # -------- Esta funcion seria parte del guardar los datos de los usuarios
    def recover_json_information(self, route):
        with open(route, "r", encoding="utf-8", newline="") as file:
            json_content = json.load(file)
        return json_content

    def save_users_information(self):
        app_user_dic = {}

        for app_user in self.users:
            print(self.users[app_user])
            app_user_dic[app_user] = self.users[app_user]

        with open("./JSONS/app_users.json", "w", encoding="utf-8", newline="") as file:
            app_user = {"App_users": app_user_dic}
            json.dump(app_user, file, indent=2)
        return

    def save_external_account(self):
        app_user_dic = {}

        for app_user in self.users:
            print(self.users[app_user])
            app_user_dic[app_user] = self.users[app_user]

        with open("./JSONS/users_external_accounts.json", "w", encoding="utf-8", newline="") as file:
            app_user = {"App_users": app_user_dic}
            json.dump(app_user, file, indent=2)
        return



