from FUNCTIONALITIES.ELEMENTS import password_list
from FUNCTIONALITIES.ELEMENTS import password


class User:
    """Clase Usuario"""
    def __init__(self, user_name, user_password):
        self.user_name = user_name
        self.user_password = user_password
        self.external_passwords = password_list.PasswordList()
        self.user_shared_passwords = None

    def share_password(self, user_name_sender, user_name_receiver):
        """Copartie Contraseña con otro usuario"""
        return

    def add_new_ext_account(self, acc_site, acc_username, acc_password):
        new_pass = password.Password(acc_site, acc_username, acc_password)
        self.external_passwords.add_password(new_pass)

    def visual_user_accounts(self):
        self.external_passwords.view_all_passwords()

    def share_user_account(self):
        pass

    def modify_ext_account(self, site, new_site, new_user, new_pass, new_sec_ques, new_notes):
        self.external_passwords.modify_password(site, new_site, new_user, new_pass, new_sec_ques, new_notes)

    def delete_ext_account(self, site):
        self.external_passwords.delete_password(site)

