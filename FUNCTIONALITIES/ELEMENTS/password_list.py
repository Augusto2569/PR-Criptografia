import time
import os


class PasswordList:
    """Lista de todas las contraseñas """

    def __init__(self):
        self.passwords = []

    def add_password(self, password: object):
        """Añadir contraseña a la lista de contraseñas"""
        self.passwords.append(password)
        return

    def delete_password(self, site):
        """Eliminar una contraseña de la lista"""
        for i in range(len(self.passwords)):
            if self.passwords[i].site == site:
                self.passwords.pop(i)
                return
        os.system('clear')
        print("Invalid searching value")
        time.sleep(1)
        return

    def modify_password(self, site, new_site, new_user, new_pass, new_sec_ques, new_notes):
        """Modificar una contraseña de la lista"""
        if len(self.passwords) == 0:
            print("Is impossible to modify any external account. \n"
                  "You don't have any external account registered in PassSword!!")
        for i in range(len(self.passwords)):
            if self.passwords[i].site == site:
                self.passwords[i].site = new_site
                self.passwords[i].username = new_user
                self.passwords[i].password = new_pass
                self.passwords[i].security_questions = new_sec_ques
                self.passwords[i].notes = new_notes
                return
        os.system('clear')
        print("Invalid searching value")
        time.sleep(1)
        return

    def view_all_passwords(self):
        os.system("clear")
        if len(self.passwords) == 0:
            print("You don't have any external account registered in PassSword!")

        """Visualizar todas las contraseñas de la lista"""
        for i in range(len(self.passwords)):

            if self.passwords[i].owner is not None:
                print("Shared password by: %s" % self.passwords[i].owner)

            print("Site/Application: %s\n"
                  "User: %s \n"
                  "Password: %s \n"
                  "Security questions: %s \n"
                  "Notes: %s \n" % (self.passwords[i].site, self.passwords[i].username,
                                    self.passwords[i].password, self.passwords[i].security_question,
                                    self.passwords[i].notes))

        input("Press enter to stop viewing your external accounts information ")
