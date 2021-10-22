"""Esta idea me parece más fácil de implementar (todo en una única clase que hereda del resto)"""
from ELEMENTS import user
import time
import json


class Admin:
    def __init__(self):
        self.users = []

    def add_user(self, user_name: str, password: str):
        for i in range(len(self.users)):
            if self.users[i].user_name == user_name:
                print("User name already taken, choose another one.")
                time.sleep(2)
                return
        temp = user.User(user_name, password)
        self.users.append(temp)

    def log_in_check_user(self, user_name, user_password):
        answer = [False, None]
        for i in range(len(self.users)):
            if self.users[i].user_name == user_name and self.users[i].user_password == user_password:
                answer[0] = True
                answer[1] = self.users[i]
                return answer
        return answer

    # -------- Esta funcion seria parte del guardar los datos de los usuarios

    def recover_users_information(self):
        with open("./JSONS/app_users.json", "r", encoding="utf-8", newline="") as file:
            app_user_dic = json.load(file)
            #self.users = app_user_dic["App_users"]
            #print(app_user_dic["App_users"])
            #time.sleep(5)
        return

    def save_users_information(self):
        app_user_dic = {}

        for app_user in self.users:
            app_user_dic[app_user.user_name] = app_user.user_password

        with open("./JSONS/app_users.json", "w", encoding="utf-8", newline="") as file:
            app_user = {"App_users": app_user_dic}
            json.dump(app_user, file, indent=2)
        return



