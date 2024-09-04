from django.core.exceptions import ValidationError


def validate_username_string(name):
    if not all(c.isalnum() or c == '_' for c in name):
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


def validate_gt_zero(num):
    if num <= 0:
        raise ValidationError("Price must be positive number")