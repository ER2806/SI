from PyQt5.QtCore import Qt

from src.commands.abstract_command import AbstractCommand
from src.commands.imports.importer_gpx import ImporterGPX


class ImportGPX(AbstractCommand):
    def __init__(self, exec=ImporterGPX()):
        self.importer = exec

    def execute(self, filename):
        return self.importer.make_import(filename=filename)

    def cancel(self):
        pass

