import os
import random
from string import ascii_letters, digits

def generate_random_string(min_len, max_len, chars=ascii_letters + digits):
    """
    Takes minimum and maximum length of output string and one optional argument
    - sequence of characters, on which a new random string will be based.
    """
    randrange = range(random.randrange(min_len, max_len))
    return ''.join(random.choice(chars) for _ in randrange)

def remove_directory_files(directory):
    """Removes all files in given directory."""
    paths = (os.path.join(directory, item) for item in os.listdir(directory))
    files = (path for path in paths if os.path.isfile(path))
    for file in files: os.remove(file)
