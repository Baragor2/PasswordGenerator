from enum import Enum
from typing import List
from generation import gen_password


def print_main_interface() -> None:
    """Main menu output"""
    print("""Выберите желаемое действие:
    1.Сгенерировать пароль
    2.Настройки""")
    gen_password_or_show_settings()


class MainInterfaceReplyType(Enum):
    GENERATE_PASSWORD = 1
    SETTINGS = 2


def get_reply_main_interface() -> MainInterfaceReplyType:
    """Gets user input from the main menu"""
    try:
        return MainInterfaceReplyType(int(input()))
    except ValueError:
        get_reply_main_interface()


def gen_password_or_show_settings() -> None:
    """Redirects to password generation or to settings"""
    reply: MainInterfaceReplyType = get_reply_main_interface()
    if reply == MainInterfaceReplyType.GENERATE_PASSWORD:
        passwords = gen_password()
        print_passwords(passwords)
    elif reply == MainInterfaceReplyType.SETTINGS:
        pass


def print_passwords(passwords: List[str]) -> None:
    """Prints generated passwords"""
    for password in passwords:
        print(password)
    print()
    print_main_interface()