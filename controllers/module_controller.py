from PyQt5 import QtWidgets

from lab1.commands.operation_stack import OperationStack
from lab1.module_disp.module_manager import ModuleManager
from lab1.route.utils import ROUTE_POOL


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
            return self.module_manager.call_default_module(module_name, route)
        else:
            return False

    def _manage_count_module(self, module_name):
        result = self._call_count_module(module_name)
        if result:
            QtWidgets.QMessageBox.information(None, module_name + " module",
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
        if self.module_manager.check_module('turn_counter'):
            print('turn_counter check successfull')
            self.view.count_turns.setEnabled(True)
        if self.module_manager.check_module('slopes_counter'):
            self.view.count_slopes.setEnabled(True)
        if self.module_manager.check_module('desc_asc_counter'):
            self.view.count_desc_asc.setEnabled(True)
        self.view.call_module.setEnabled(True)

    def call_runtime_module(self):
        self.view.statusbar.showMessage("choose file")
        file = QtWidgets.QFileDialog.getOpenFileName(parent=self.view, caption="Open file...", filter="*.py")
        if file == ('', ''):
            QtWidgets.QMessageBox.warning(None, "Warning", "File was not selected!",
                                          buttons=QtWidgets.QMessageBox.Ok)
        else:
            file_path = '.'.join([i for i in list(file[0][:-3].split('/'))[-4:]])
            print(file_path)
            route = ROUTE_POOL[self.view.routes.item(
                self.view.routes.selectedItems()[0].row(),
                0).text()]
            result = self.module_manager.call_runtime_module(file_path, route)
            if result:
                QtWidgets.QMessageBox.information(None, file_path + " module",
                                        "module ended work with result:\n{0}".format(result))
                print("COUNTER", result)
            else:
                print("unknown module")




