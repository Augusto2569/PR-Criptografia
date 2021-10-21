"""Esta idea me parece más fácil de implementar (todo en una única clase que hereda del resto)"""
from ELEMENTS import user
from ELEMENTS import password
from ELEMENTS import password_list
import time


class Admin:
    def __init__(self):
        self.users = []
        self.passwords = password_list.PasswordList()

    def add_user(self, user_name:str, password:str):
        for i in range(len(self.users)):
            if self.users[i].user_name == user_name:
                print("User name already taken, choose another one.")
                time.sleep(2)
                return
        temp = user.User(user_name, password)
        self.users.append(temp)

    def log_in_check_user(self, user_name, user_password):
        for i in range(len(self.users)):
            if self.users[i].user_name == user_name and self.users[i].password == user_password:
                return True
        return False

    # -------- Hacer refactor y meterlo en user porque es de cada usuario
    def add_new_ext_account(self, acc_site, acc_username, acc_password):
        new_pass = password.Password(acc_site, acc_username, acc_password)
        self.passwords.add_password(new_pass)
        return

    def visual_user_accounts(self):
        self.passwords.view_all_passwords()

    def share_user_account(self):
        pass

    def delete_ext_account(self, site):
        self.passwords.delete_password(site)

    def modify_ext_account(self, site, new_site, new_user, new_pass, new_sec_ques, new_notes):
        self.passwords.modify_password(site, new_site, new_user, new_pass, new_sec_ques, new_notes)

    # --------------------------------------------------------------------------------------
    def save_user_information(self):
        return
