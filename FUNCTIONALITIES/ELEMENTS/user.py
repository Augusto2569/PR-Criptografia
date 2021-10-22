import time
from FUNCTIONALITIES.ELEMENTS import password_list
from FUNCTIONALITIES.ELEMENTS import password


class User:
    """Clase Usuario"""
    def __init__(self, user_name, user_password):
        self.user_name = user_name
        self.user_password = user_password
        self.external_passwords = password_list.PasswordList()
        self.user_shared_passwords = None

    def add_new_ext_account(self, acc_site, acc_username, acc_password):
        new_pass = password.Password(acc_site, acc_username, acc_password)
        self.external_passwords.add_password(new_pass)

    def visual_user_accounts(self):
        self.external_passwords.view_all_passwords()

    def modify_ext_account(self, site, new_site, new_user, new_pass, new_sec_ques, new_notes):
        self.external_passwords.modify_password(site, new_site, new_user, new_pass, new_sec_ques, new_notes)

    def delete_ext_account(self, site):
        self.external_passwords.delete_password(site)

    def share_user_account(self, platform_users, receiving_user, site):
        for user in platform_users:
            if user.user_name == receiving_user:
                external_account = self.look_for_external_account(site)
                shared_password = password.SharedPassword(self.user_name, external_account.site,
                                                          external_account.username, external_account.password)
                user.external_passwords.add_password(shared_password)
                print("Your %s account have been successfully shared with %s" % (site, receiving_user))
                time.sleep(2.5)
                return
        print("Error - The requested user doesn't exist!")
        time.sleep(1.5)

    def look_for_external_account(self, site):
        external_account_existence = False
        for external_password in self.external_passwords.passwords:
            if external_password.site == site:
                return external_password
        return external_account_existence
