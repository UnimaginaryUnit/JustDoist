import os
import sys

from django import setup
from django.apps.registry import apps


def load_django(app_settings: str="justdoist.settings", project_directory: str=None):
    """
    A function that loads django apps without starting the server.
    Usage:
    >>> # Firstly load django apps
    >>> from load_django import load_django; load_django()
    >>> # After you are able to import any model you want.
    >>> from my_app.models import MyModel
    
    :param app_settings: project settings file 
    :param project_directory: path to main project directory
    """
    project_directory = project_directory or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if not apps.ready:
        if app_settings is None:
            raise ValueError("Application settings must be provided when django isn't loaded!")
        sys.path.append(os.path.abspath(project_directory))
        os.environ["DJANGO_SETTINGS_MODULE"] = app_settings
        setup()
