from os import path
import re
import random
from string import ascii_letters, digits

def get_userpic_path(instance, filename):
    """
    Takes an instance of UserPersonalData model and name of profile's picture.
    Returns a path to profile's picture relative to MEDIA_ROOT.
    """
    userpic_dirname = 'user_%s' % instance.auth_data.id
    return path.join('userApp', 'avatar', userpic_dirname, filename)

def get_thumbnail_name(avatar_name):
    """
    Takes name of user's avatar file.
    Return name of related thumbnail file.
    """
    return re.sub(r'\.jpe?g$', lambda fnd: "_150x150"+fnd.group(0), avatar_name)

def generate_random_string(min_len, max_len, chars=ascii_letters + digits):
    """
    Takes minimum and maximum length of output string and one optional argument
    - sequence of characters, on which a new random string will be based.
    """
    randrange = range(random.randrange(min_len, max_len))
    return ''.join(random.choice(chars) for _ in randrange)
