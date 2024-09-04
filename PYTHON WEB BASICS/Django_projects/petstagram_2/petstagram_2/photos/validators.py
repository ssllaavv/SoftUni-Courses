from django.core.exceptions import ValidationError


def file_size_validator(image_object):
    if image_object.size > 5242880:
        raise ValidationError('The maximum file size is 5MB')
