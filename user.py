class User():
    """Clase Usuario"""
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        self.user_passwords = None
        self.user_shared_passwords = None

    def share_password(self, user_name_sender, user_name_receiver):
        """Compartir contraseña con otro usuario"""
        pass