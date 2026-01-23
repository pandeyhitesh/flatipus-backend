import random
import string


class HouseKey:
    def __init__(self, value: str | None = None):
        if value is None:
            value = self._generate()

        if not self._is_valid(value):
            raise ValueError("Invalid house key")

        self._value = value

    @staticmethod
    def _generate() -> str:
        return ''.join(
            random.choices(
                string.ascii_uppercase + string.digits, k=6))

    @staticmethod
    def _is_valid(value: str) -> bool:
        return len(value) == 6 and value.isalnum()

    @property
    def value(self) -> str:
        return self._value

    def __str__(self):
        return self._value
