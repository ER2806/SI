from lab1.commands.abstract_command import AbstractCommand
from lab1.commands.edit.editor import Editor


class Edit(AbstractCommand):
    def __init__(self, exec=Editor()):
        self.editor = exec

    def execute(self, items):
        return self.editor.edit_points(items)

    def cancel(self, act):
            self.editor.cancel_edit(act)
