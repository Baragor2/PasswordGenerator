from enum import Enum
from typing import NewType


class SettingsInterfaceReplyType(Enum):
    CHANGE_LENGTH = 1
    CHANGE_COUNT = 2
    CHANGE_UPPER = 3
    CHANGE_LOWER = 4
    CHANGE_DIGITS = 5
    CHANGE_SPECIALS = 6
    EXIT = 7


class MainInterfaceReplyType(Enum):
    GENERATE_PASSWORD = 1
    SETTINGS = 2


PositiveLimitedInt = NewType('PositiveLimitedInt', int)