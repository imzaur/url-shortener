from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validate_url(value):
    url_validator = URLValidator()
    value_1_invalid = True
    value_2_invalid = True
    try:
        url_validator(value)
    except:
        value_1_invalid = False
        value = 'http://' + value

    try:
        url_validator(value)
    except:
        value_2_invalid = False

    if not value_1_invalid and not value_2_invalid:
        raise ValidationError("Invalid URL")
    return value


def validate_dot_com(value):
    if value.count('.') >= 1:
        return value
    else:
        raise ValidationError("Type correct URL")