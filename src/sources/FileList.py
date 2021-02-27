from .SourceInterface import SourceInterface
class FileList(SourceInterface):
    """
    allows to iterate through a list of files in a specified directory
    """
    def __init__(self, path, extensions=[]):
        self.path = path
        self.extensions = extensions

    def execute(self):
        for subdir, dirs, files in os.walk(self.path):
            for file in files:
                #print os.path.join(subdir, file)
                filepath = subdir + os.sep + file
                if len(self.extensions) > 0:
                    if file.endswith(self.extensions):
                        yield (filepath, file)
                else:
                    yield (filepath, file)
