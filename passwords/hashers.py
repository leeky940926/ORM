from django.contrib.auth.hashers import PBKDF2PasswordHasher

class MyPBKDF2Hahser(PBKDF2PasswordHasher):
    interations = PBKDF2PasswordHasher.iterations * 100