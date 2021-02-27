from .SourceInterface import SourceInterface
import gspread

class GoogleSheet(SourceInterface):
    """gets data from a google sheet
    """

    def __init__(self, name, tab):
        self.name = name
        self.tab = tab

    def execute(self):
        yield None
