from FUNCTIONALITIES import admin
import os
import time

admin = admin.Admin()
os.system('clear')

print("Welcome to PassSword!!!\n")
time.sleep(2)

while True:
    "Bucle que permite la ejecucion hasta que el usuario indique lo contrario"
    admin.recover_json_information("./JSONS/app_users.json")
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
        log_in_ck = admin.log_in_check_user(app_user, app_pass)
        flag = log_in_ck[0]
        user_acc = log_in_ck[1]

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
                    user_acc.visual_user_accounts()

                elif action == "2":
                    os.system("clear")
                    print("Add a new password - Introduce the account information")
                    acc_site = input("Introduce the site of the account: ")
                    acc_user = input("Introduce the user of the account: ")
                    acc_pass = input("Introduce the password of the account: ")
                    user_acc.add_new_ext_account(acc_site, acc_user, acc_pass)

                elif action == "3":
                    os.system("clear")
                    print("Modify password - Introduce the required data")
                    site = input("Introduce the site/application that you would like to change: ")
                    new_acc_site = input("Introduce the new site/application: ")
                    new_acc_user = input("Introduce the new user: ")
                    new_acc_pass = input("Introduce the new password: ")
                    new_acc_sec_ques = input("Introduce the new security question: ")
                    new_acc_notes = input("Introduce the new notes: ")
                    user_acc.modify_ext_account(site, new_acc_site, new_acc_user, new_acc_pass,
                                                new_acc_sec_ques, new_acc_notes)

                elif action == "4":
                    os.system("clear")
                    print("Share a password - Introduce the required data")
                    receiving_user = input("Introduce the user which you will like to share your account: ")
                    site_to_share = input("Introduce the site of the account you want to share: ")
                    user_acc.share_user_account(admin.users, receiving_user, site_to_share)

                elif action == "5":
                    os.system("clear")
                    print("Delete a password - Introduce the required data")
                    site = input("Introduce the site/application that you would like to delete: ")
                    user_acc.delete_ext_account(site)

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
        admin.save_users_information()
        os.system("clear")
        print("Thanks for using PassSword!!")
        break

    # ---------------------- Input error functionality -----------------------------
    else:
        print("Wrong answer, try again!")
        time.sleep(2)

