from my_types import PositiveLimitedInt
import json


with open('config.json', 'r') as json_config:
    config_data = json.load(json_config)

PASSWORD_LENGTH = PositiveLimitedInt(config_data['PASSWORD_LENGTH'])
USE_UPPERCASE = config_data['USE_UPPERCASE']
USE_LOWERCASE = config_data['USE_LOWERCASE']
USE_DIGITS = config_data['USE_DIGITS']
USE_SPECIAL = config_data['USE_SPECIAL']
PASSWORD_COUNT = PositiveLimitedInt(config_data['PASSWORD_COUNT'])