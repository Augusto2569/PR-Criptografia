from ELEMENTS import user
from FUNCTIONALITIES import admin
from ELEMENTS import users_list
# from ELEMENTS import password
from ELEMENTS import password_list
import os
import time

"""TENEMOS QUE CAMBIAR LA CONTRASEÑA PORQUE NO ES DE CADA USUARIO SINO DEL SITEMA. RELAMENTE TEINE QUE SER DE CADA
USUARIO EN PARTICULAR."""


admin = admin.Admin()
os.system('clear')

print("Welcome to PassSword!!!\n")
time.sleep(2)

while True:
    "Bucle que permite la ejecucion hasta que el usuario indique lo contrario"

    os.system('clear')
    print("Welcome menu - Choose between actions: \n "
          "1) Login \n "
          "2) Sing up\n "
          "3) Close program")
    action = input("Write down 1, 2 or 3: ")

    # ---------------------- Login functionality -----------------------------
    if action == "1":
        os.system('clear')
        #Una vez chekeado que es un usuario registrado
        #pasamos a la interaccion de en el menu principal
        print("Login Menu - Introduce your user information:")
        app_user = input("Username: ")
        app_pass = input("Password: ")
        input("Please press enter to confirm")
        flag = admin.log_in_check_user(app_user, app_pass)

        if flag:
            while True:
                os.system('clear')
                print("Main menu - Choose between actions:\n"
                      "1) See your passwords\n"
                      "2) Add a new password\n"
                      "3) Modify a password\n"
                      "4) Share a password\n"
                      "5) Delete a password\n"
                      "6) Close current session")

                action = input("Write down 1, 2, 3, 4, 5 or 6: ")

                if action == "1":
                    admin.visual_user_accounts()

                elif action == "2":
                    print("Add a new password - Introduce the account information")
                    acc_site = input("Introduce the site of the account: ")
                    acc_user = input("Introduce the user of the account: ")
                    acc_pass = input("Introduce the password of the account: ")
                    admin.add_new_ext_account(acc_site, acc_user, acc_pass)
                    print("Your account information have been stored correctly, either way you can modify it!")

                elif action == "3":
                    print("Modify password - Introduce the required data")
                    site = input("Introduce the site/application that you would like to change: ")
                    new_acc_site = input("Introduce the new site/application: ")
                    new_acc_user = input("Introduce the new user: ")
                    new_acc_pass = input("Introduce the new password: ")
                    new_acc_sec_ques = input("Introduce the new security question: ")
                    new_acc_notes = input("Introduce the new notes: ")
                    admin.modify_ext_account(site, new_acc_site, new_acc_user, new_acc_pass, new_acc_sec_ques,
                                             new_acc_notes)
                    pass

                elif action == "4":
                    pass

                elif action == "5":
                    print("Delete a password - Introduce the required data")
                    site = input("Introduce the site/application that you would like to delete: ")
                    admin.delete_ext_account(site)
                    pass

                elif action == "6":
                    # Cuandp queramos cerrar la app, deberiamos guardar toda los datos modificados en un JSON
                    break
                else:
                    print("Wrong answer, try again!")
                    time.sleep(2)
        else:
            os.system("clear")
            print("Invalid credentials, please try again")
            time.sleep(1)

    # ---------------------- Sing up functionality -----------------------------
    elif action == "2":
        os.system('clear')
        print("Sing up - New User")
        app_user = input("Username: ")
        app_pass = input("Password: ")
        admin.add_user(app_user, app_pass)

    # ---------------------- Close functionality -----------------------------
    elif action == "3":
        os.system("clear")
        print("Thanks for using PassSword!!")
        break

    # ---------------------- Input error functionality -----------------------------
    else:
        print("Wrong answer, try again!")
        time.sleep(2)

