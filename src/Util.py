import os
class Util:
    """Utility class for getting information about global stuff"""
    @staticmethod
    def app_dir():
        return os.path.dirname(os.path.dirname(__file__))+os.sep

    def input_dir():
        return Util.app_dir()+'input'+os.sep
