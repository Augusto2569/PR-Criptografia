#from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

class Password:
    #This class is used for creating a password that will be saved in our program

    def __init__(self, site, username, password, security_questions=None, notes=None, owner=None):
        self.owner = owner
        self.site = site
        self.username = username
        self.password = password
        self.security_question = security_questions
        self.notes = notes

    '''
    def encrypt(self):
        key = os.urandom(32)
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        ct = encryptor.update(b"a secret message") + encryptor.finalize()
        decryptor = cipher.decryptor()
        decryptor.update(ct) + decryptor.finalize()'''


class SharedPassword(Password):
    def __init__(self, owner, site, username, password, security_questions=None, notes=None):
        self.owner = owner
        self.site = site
        self.username = username
        self.password = password
        self.security_question = security_questions
        self.notes = notes
