class Password:
    """This class is used for creating a password that will be saved in our program"""

    def __init__(self, user_id, username, password,security_questions, notes):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.security_question = security_questions
        self.notes = notes