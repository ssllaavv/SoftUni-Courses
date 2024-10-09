from django.core.exceptions import ValidationError


def validate_first_letter_capital(value):
    if value and not value[0].isupper():
        raise ValidationError('Your name must start with a capital letter!')
