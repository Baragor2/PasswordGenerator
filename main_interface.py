from enum import Enum


def print_main_interface() -> None:
    print("""Выберите желаемое действие:
    1.Сгенерировать пароль
    2.Настройки""")


class MainInterfaceReplyType(Enum):
    GENERATE_PASSWORD = 1
    SETTINGS = 2


def reply_main_interface() -> MainInterfaceReplyType:
    try:
        reply: MainInterfaceReplyType = MainInterfaceReplyType(int(input()))
        return reply
    except ValueError:
        reply_main_interface()