from os import path
import re
from mlp_api.settings import MEDIA_ROOT

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
