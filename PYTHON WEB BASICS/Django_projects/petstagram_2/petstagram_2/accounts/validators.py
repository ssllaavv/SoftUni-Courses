from django.core.exceptions import ValidationError


def validate_name_isalpha(value):
    if not value.isalpha():
        raise ValidationError('The name must contains only letters!')


def validate_name_is_longer_then_two_cars(value):
    if len(value) < 2:
        raise ValidationError('Name must be at least two characters long!')
