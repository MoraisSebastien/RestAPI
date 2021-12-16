import re
from pydantic import BaseModel, ValidationError, validator


class SSN:
    def __init__(self, num_ssn: str):
        self.__num = num_ssn

    def is_format_valid(self):
        return bool(re.match("^[123478][0-9]{2}[0-1][0-9](2[AB]|[0-9]{2})[0-9]{3}[0-9]{3}[0-9]{2}$", self.__num))

    def is_length_valid(self):
        if len(self.__num) == 15:
            return True
        else:
            return False

    def is_key_valid(self):
        real_key: str = str(self.__num[13]) + str(self.__num[14])
        return bool(real_key == str((97 - (int(self.__num[0:13]) % 97))))

    def is_valid(self):
        if self.is_format_valid() is True and self.is_key_valid() is True and self.is_length_valid() is True:
            return True
        else:
            return False
