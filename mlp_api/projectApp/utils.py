from os import path

def get_project_preview_path(instance, filename):
    """
    Takes an instance of Project model and name of preview's picture.
    Returns a path to project's picture relative to MEDIA_ROOT.
    """
    return path.join('projectApp', 'previews', instance.slug, filename)
