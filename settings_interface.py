import config
from my_types import SettingsInterfaceReplyType, PositiveLimitedInt
import main_interface
from typing import Callable


def print_settings_interface() -> None:
    """Settings menu output"""
    print('''Настройки:
    1.Изменить длину пароля
    2.Изменить количество генерируемых паролей
    3.Добавить/убрать заглавные буквы
    4.Добавить/убрать прописные буквы
    5.Добавить/убрать цифры
    6.Добавить/убрать спецсимволы
    7.Выйти из настроек''')
    manage_config()


def get_reply_settings_interface() -> SettingsInterfaceReplyType:
    """Gets user input from the settings menu"""
    try:
        return SettingsInterfaceReplyType(int(input()))
    except ValueError:
        manage_config()


def manage_config() -> None:
    reply: SettingsInterfaceReplyType = get_reply_settings_interface()
    match reply:
        case SettingsInterfaceReplyType.CHANGE_LENGTH:
            change_length()
        case SettingsInterfaceReplyType.CHANGE_COUNT:
            pass
        case SettingsInterfaceReplyType.CHANGE_UPPER:
            pass
        case SettingsInterfaceReplyType.CHANGE_LOWER:
            pass
        case SettingsInterfaceReplyType.CHANGE_DIGITS:
            pass
        case SettingsInterfaceReplyType.CHANGE_SPECIALS:
            pass
        case SettingsInterfaceReplyType.EXIT:
            main_interface.print_main_interface()


def change_length() -> None:
    """Changes the password length in the config by user input"""
    print("Введите длину для паролей")
    try:
        config.PASSWORD_LENGTH = check_length(int(input()), change_length)
        print_settings_interface()
    except ValueError:
        change_length()


def check_length(num: int, func: Callable) -> PositiveLimitedInt:
    if 0 < num < 512:
        return PositiveLimitedInt(num)
    else:
        func()
