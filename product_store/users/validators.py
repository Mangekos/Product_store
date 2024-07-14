import re

from django.core.exceptions import ValidationError

REGEX_FOR_USERNAME: re.Pattern[str] = re.compile(r'^[\w.@+-]+\Z')


def validate_name(name) -> None:
    """Функция проверки корректности имени пользователя."""
    if name == 'me':
        raise ValidationError('Имя пользователя "me" использовать нельзя!')
    if not REGEX_FOR_USERNAME.fullmatch(name):
        raise ValidationError(
            'Можно использовать только буквы, цифры и "@.+-_".')
