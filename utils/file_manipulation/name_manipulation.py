import uuid


def set_unique_filename(_instance, filename):
    """Gets a filename and sets a randon filename so there is no overwriting in the system"""
    extension = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{extension}'
    return filename
