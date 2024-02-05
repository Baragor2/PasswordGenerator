from enum import Enum


def print_main_interface() -> None:
    """Main menu output"""
    print("""Выберите желаемое действие:
    1.Сгенерировать пароль
    2.Настройки""")


class MainInterfaceReplyType(Enum):
    GENERATE_PASSWORD = 1
    SETTINGS = 2


def get_reply_main_interface() -> MainInterfaceReplyType:
    """Gets user input from the main menu"""
    try:
        return MainInterfaceReplyType(int(input()))
    except ValueError:
        get_reply_main_interface()
