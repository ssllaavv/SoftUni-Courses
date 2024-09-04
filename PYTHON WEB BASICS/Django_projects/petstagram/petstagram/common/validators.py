from django.core.exceptions import ValidationError


def validate_file_size(file_object):
    if file_object.size > 5242880:
        raise ValidationError('The maximum file size to be uploaded is 5MB')
