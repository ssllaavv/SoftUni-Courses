from django.core.exceptions import ValidationError


def validate_name_contains_only_letters(value):
    if value and not value.isalpha():
        raise ValidationError("Plant name should contain only letters!")
