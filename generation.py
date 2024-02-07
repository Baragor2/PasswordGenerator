from config import MyConfig
from random import choice
from typing import List
from string import ascii_lowercase, ascii_uppercase, digits, punctuation as special_symbols


def gen_password() -> List[str]:
    """Generates a list of passwords"""
    allowed_chars: str = get_allowed_chars()
    passwords: List[str] = []
    password: str = ''
    for i in range(MyConfig.PASSWORD_COUNT):
        for j in range(MyConfig.PASSWORD_LENGTH):
            password += choice(allowed_chars)
        passwords.append(password)
        password = ''
    return passwords


def get_allowed_chars() -> str:
    """Generates a string of allowed characters"""
    allowed_chars: str = ''
    if MyConfig.USE_LOWERCASE:
        allowed_chars += ascii_lowercase
    if MyConfig.USE_UPPERCASE:
        allowed_chars += ascii_uppercase
    if MyConfig.USE_DIGITS:
        allowed_chars += digits
    if MyConfig.USE_SPECIAL:
        allowed_chars += special_symbols
    return allowed_chars
