import os

def remove_directory_files(directory):
    """Removes all files in given directory."""
    paths = (os.path.join(directory, item) for item in os.listdir(directory))
    files = (path for path in paths if os.path.isfile(path))
    for file in files: os.remove(file)
