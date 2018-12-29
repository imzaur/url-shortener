from django.conf import settings
import random
import string

SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 6)

def code_generator(size=SHORTCODE_MIN):
    chars = string.ascii_lowercase + string.digits
    code = map(lambda x: random.choice(chars), range(size))
    return ''.join(list(code))


def create_shortcode(instance, size=SHORTCODE_MIN):
    new_code = code_generator(size=size)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shortcode(size=size)
    return new_code
