from PyQt5 import QtWidgets

from src.commands.operation_stack import OperationStack
from src.module_disp.module_manager import ModuleManager
from src.route.utils import ROUTE_POOL


class ModuleController():
    def __init__(self, view):
        self.view = view
        self.module_manager = ModuleManager()
        self.operation_stack = OperationStack()

    def _call_count_module(self, module_name):
        route = ROUTE_POOL[self.view.routes.item(
                                self.view.routes.selectedItems()[0].row(),
                           0).text()]
        if self.module_manager.check_module(module_name):
            return self.module_manager.call_module(module_name, route)
        else:
            return False

    def _manage_count_module(self, module_name):
        result = self._call_count_module(module_name)
        if result:
            QtWidgets.QMessageBox.critical(None, module_name + " module",
                                        "module ended work with result:\n{0}".format(result))
            print("COUNTER", result)
        else:
            print("unknown module")

    def count_turns(self):
        self._manage_count_module("turn_counter")

    def count_slopes(self):
        self._manage_count_module("slopes_counter")

    def count_desc_asc(self):
        self._manage_count_module("desc_asc_counter")

    def activate_buttons(self):
        modules = self.module_manager.get_modules()
        print('activate_buttons', modules)
        if 'turn_counter' in modules:
            self.view.count_turns.setEnabled(True)
        if 'slopes_counter' in modules:
            self.view.count_slopes.setEnabled(True)
        if 'desc_asc_counter' in modules:
            self.view.count_desc_asc.setEnabled(True)



