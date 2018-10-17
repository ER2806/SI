from PyQt5.QtCore import Qt

from src.commands.abstract_command import AbstractCommand
from src.commands.imports.importer_polyline import ImporterPolyline


class ImportPolyline(AbstractCommand):
    def __init__(self, exec=ImporterPolyline()):
        self.importer = exec

    def execute(self, source):
        return self.importer.make_import(source)

    def cancel(self):
        pass

