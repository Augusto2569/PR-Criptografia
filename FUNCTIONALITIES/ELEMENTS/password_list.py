import time
import os


class PasswordList:
    """Lista de todas las contraseñas """

    def __init__(self):
        #self.passwords = []
        self.password = {}

    def add_password_v2(self, password: object):
        """Añadir contraseña a la lista de contraseñas"""
        existing = self.check_existing_password(password.site) #buscamos si la contraseña existe por el sitio
        if existing:
            self.passwords.append(password)
            os.system("clear")
            print("Your account information have been stored correctly, either way you can modify it!")
            time.sleep(1.5)
        else:
            os.system("clear")
            print("Error - Duplicated account")
            time.sleep(2)
        return

    def add_password(self, user, password: object):
        """Añadir contraseña a la lista de contraseñas"""
        #Accedemos al diccionario del usuario
        #Verificamos que no este la contraseña que estamos intentando crear
        #Si no esta, lo agregamos al diccionario del usuario

    def delete_password_v2(self, site):
        """Eliminar una contraseña de la lista"""
        existing = self.check_existing_password(site)
        if existing > 0:
            self.passwords.pop(existing)
            return
        os.system('clear')
        print("Error - Invalid searching value")
        time.sleep(1)
        return

    def delete_password(self, site):
        """Eliminar una contraseña de la lista"""
        #Accedemos al diccionario del usuario
        #Verificamos que este la contraseña que estamos intentando crear
        #Si esta, lo eliminamos

    def modify_password_v2(self, site, new_site, new_user, new_pass, new_sec_ques, new_notes):
        """Modificar una contraseña de la lista"""
        if len(self.passwords) == 0:
            print("Is impossible to modify any external account. \n"
                  "You don't have any external account registered in PassSword!!")
            existing = self.check_existing_password(site)
            if existing > 0:
                self.passwords[existing].site = new_site
                self.passwords[existing].username = new_user
                self.passwords[existing].password = new_pass
                self.passwords[existing].security_questions = new_sec_ques
                self.passwords[existing].notes = new_notes
                os.system("clear")
                print("Your account information have been modified correctly!")
                time.sleep(2)
                return
        os.system('clear')
        print("Error - Invalid searching value")
        time.sleep(1)
        return

    def modify_password(self, site, new_site, new_user, new_pass, new_sec_ques, new_notes):
        """Modificar una contraseña de la lista"""
        if len(self.passwords) == 0:
            print("Is impossible to modify any external account. \n"
                  "You don't have any external account registered in PassSword!!")
            existing = self.check_existing_password(site)
            if existing > 0:
                self.passwords[existing].site = new_site
                self.passwords[existing].username = new_user
                self.passwords[existing].password = new_pass
                self.passwords[existing].security_questions = new_sec_ques
                self.passwords[existing].notes = new_notes
                os.system("clear")
                print("Your account information have been modified correctly!")
                time.sleep(2)
                return
        os.system('clear')
        print("Error - Invalid searching value")
        time.sleep(1)
        return

    def view_all_passwords_v2(self):
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

    def view_all_passwords(self, user):
        # Accedemos al diccionario del usuario
        # Recorremos todas los sites

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

    def check_existing_password(self, site):

        try:
            a = self.passwords[user][site]

        except  KeyError:
            return None


        if len(self.passwords) == 0:
            return 0
        index = -1
        for i in range(len(self.passwords)):
            if self.passwords == site:
                index = i
                return index
        return index
