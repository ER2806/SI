from src.commands.utils import HISTORY
from src.utils.singleton import Singleton


class OperationStackO(Singleton):
    def __init__(self):
        self.menu = None
        self.pointer = None

    def push(self, elem):
        if not HISTORY:
            self.menu.undo.setEnabled(True)
            self.pointer = -1
        else:
            self.menu.redo.setEnabled(True)

        self.pointer += 1
        HISTORY.insert(self.pointer, elem)

    def pop(self):
        if HISTORY:
            self.menu.redo.setEnabled(True)

        self.pointer -= 1
        return HISTORY[self.pointer + 1]