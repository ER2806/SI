from PyQt5.QtCore import Qt

from lab1.commands.abstract_command import AbstractCommand
from lab1.commands.imports.importer_gpx import ImporterGPX


class ImportGPX(AbstractCommand):
    def __init__(self, exec=ImporterGPX()):
        self.importer = exec

    def execute(self, filename):
        return self.importer.make_import(filename=filename)

    def cancel(self):
        pass

