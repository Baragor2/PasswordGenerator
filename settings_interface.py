# import config
from config import MyConfig
from my_types import SettingsInterfaceReplyType, PositiveLimitedInt
import main_interface
from typing import Callable
import json


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
    """User input processing"""
    reply: SettingsInterfaceReplyType = get_reply_settings_interface()
    match reply:
        case SettingsInterfaceReplyType.CHANGE_LENGTH:
            change_length()
        case SettingsInterfaceReplyType.CHANGE_COUNT:
            change_count()
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
    print("Введите длину для паролей или введите \"exit\" для выхода")
    reply = input()
    if reply == 'exit':
        print_settings_interface()
    try:
        length = check_positive_limited_int(int(reply), change_length)
        refresh_the_config(length, "PASSWORD_LENGTH")
        print_settings_interface()
    except ValueError:
        change_length()


def change_count() -> None:
    """Changes the password count in the config by user input"""
    print("Введите количество одновременно генерируемых паролей или введите \"exit\" для выхода")
    reply = input()
    if reply == 'exit':
        print_settings_interface()
    try:
        count = check_positive_limited_int(int(reply), change_length)
        refresh_the_config(count, "PASSWORD_COUNT")
        print_settings_interface()
    except ValueError:
        change_count()


def check_positive_limited_int(num: int, func: Callable) -> PositiveLimitedInt:
    """Checking the validity of password length"""
    if 0 < num < 513:
        return PositiveLimitedInt(num)
    else:
        func()


def refresh_the_config(param: (PositiveLimitedInt, bool), config_parameter: str):
    """Config parameter update"""
    with open('config.json', 'r') as json_config:
        config_data = json.load(json_config)

    config_data[config_parameter] = param

    with open('config.json', 'w') as json_config:
        json.dump(config_data, json_config)

    setattr(MyConfig, config_parameter, param)
