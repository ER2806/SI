from lab1.commands.utils import HISTORY
from lab1.utils.singleton import Singleton


class OperationStack(Singleton):
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

    def print(self):
        print([item for item in HISTORY])