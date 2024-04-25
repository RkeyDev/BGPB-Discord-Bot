import sys
import os


class SetupDirPath:
    """
    Allow access to modules from parent files.
    """
    def __init__(self) -> None:        
        sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
