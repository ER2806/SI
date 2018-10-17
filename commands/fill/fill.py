from src.commands.abstract_command import AbstractCommand
from src.commands.fill.filler import Filler


class Fill(AbstractCommand):
    def __init__(self, exec=Filler()):
        self.importer = exec

    def execute(self, menu):
        self.importer.fill_tables(menu=menu)

    def cancel(self, win):
        pass
