"""Esta idea me parece más fácil de implementar (todo en una única clase que hereda del resto)"""
from ELEMENTS import user
from ELEMENTS import password_list
import time


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

    def save_user_information(self):
        return


