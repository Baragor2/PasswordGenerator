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
            change_upper()
        case SettingsInterfaceReplyType.CHANGE_LOWER:
            change_lower()
        case SettingsInterfaceReplyType.CHANGE_DIGITS:
            change_digits()
        case SettingsInterfaceReplyType.CHANGE_SPECIALS:
            change_special()
        case SettingsInterfaceReplyType.EXIT:
            main_interface.print_main_interface()


def change_config(message: str, check_func: Callable, config_parameter: str) -> None:
    """Changes the config parameter by user input"""
    print(message + " или введите \"exit\" для выхода")
    reply = input()
    if reply == 'exit':
        print_settings_interface()
    try:
        param = check_func(int(reply), change_config)
        refresh_the_config(param, config_parameter)
        print_settings_interface()
    except ValueError:
        change_config(message, check_func, config_parameter)


def change_length() -> None:
    """Changes the password length in the config by user input"""
    change_config("Введите длину для паролей", check_positive_limited_int, "PASSWORD_LENGTH")


def change_count() -> None:
    """Changes the password count in the config by user input"""
    change_config("Введите количество одновременно генерируемых паролей", check_positive_limited_int, "PASSWORD_COUNT")


def change_upper() -> None:
    """Enables/disables the use of uppercase letters"""
    change_config_bool("Заглавные буквы", "USE_UPPERCASE")


def change_lower() -> None:
    """Enables/disables the use of lowercase letters"""
    change_config_bool("Строчные буквы", "USE_LOWERCASE")


def change_digits() -> None:
    """Enables/disables the use of digits"""
    change_config_bool("Цифры", "USE_DIGITS")


def change_special() -> None:
    """Enables/disables the use of special symbols"""
    change_config_bool("Спецсимволы", "USE_SPECIAL")


def change_config_bool(message: str, config_parameter: str) -> None:
    """Enables/disables the config parameters"""
    if getattr(MyConfig, config_parameter):
        print(f'{message} отключены')
        refresh_the_config(False, config_parameter)
        print_settings_interface()
    else:
        print(f'{message} включены')
        refresh_the_config(True, config_parameter)
        print_settings_interface()


def check_positive_limited_int(num: int, func: Callable) -> PositiveLimitedInt:
    """Checking the validity of password length"""
    if 0 < num < 513:
        return PositiveLimitedInt(num)
    else:
        func()


def refresh_the_config(value: (PositiveLimitedInt, bool), config_parameter: str):
    """Config parameter update"""
    with open('config.json', 'r') as json_config:
        config_data = json.load(json_config)

    config_data[config_parameter] = value

    with open('config.json', 'w') as json_config:
        json.dump(config_data, json_config, indent=2)

    setattr(MyConfig, config_parameter, value)
