from django.core.exceptions import ValidationError


def validate_fruit_name_contains_only_letters(name):
    if not name.isalpha():
        raise ValidationError("Fruit name should contain only letters!")