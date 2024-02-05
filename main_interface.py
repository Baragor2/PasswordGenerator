from my_types import MainInterfaceReplyType
from typing import List
from generation import gen_password
from settings_interface import print_settings_interface


def print_main_interface() -> None:
    """Main menu output"""
    print("""Выберите желаемое действие:
    1.Сгенерировать пароль
    2.Настройки""")
    gen_password_or_show_settings()


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
        print_settings_interface()


def print_passwords(passwords: List[str]) -> None:
    """Prints generated passwords"""
    for password in passwords:
        print(password)
    print()
    print_main_interface()
