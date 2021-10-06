class Password():
    """This class is used for creating a password that will be saved in our program"""

    def __init__(self, user_id, username, password,security_questions, notes):
        self.user_id = user_id #user_id tiene password de atributo, password tiene user_id de atributo? No sería mejor todo en uno? (user)
        self.username = username
        self.password = password
        self.security_question = security_questions
        self.notes = notes

    #Jorge: yo no pondría el atributo notes obligatorio, algunos usuarios puede que no  quieran añadir notas para recordar su contraseña