from PyQt5.QtCore import Qt

from lab1.commands.edit.edit import Edit
from lab1.commands.operation_stack import OperationStack
from lab1.commands.remove.remove import Remove
from lab1.commands.utils import HISTORY, count_length, field_idx_to_name
from lab1.controllers.fill_controller import FillController
from lab1.route.utils import ROUTE_POOL


class UndoRedoController():
    def __init__(self, view):
        self.view = view
        self.operation_stack = OperationStack()
        self.fill_controller = FillController(self.view)
        self._remove = Remove()
        self._edit = Edit()

    def undo(self):
        global_action = self.operation_stack.pop()
        key = list(global_action.keys())[0]
        action = global_action[key]
        print(self.operation_stack)
        print(global_action)
        print(key)
        print(action)

        if key == "ImportPolyline":
            item = self.view.routes.findItems(action['import'], Qt.MatchFixedString)[0]
            item.setSelected(True)
            self.view.delete_route.click()

        elif key == "ImportGPX":
            print("view routes", self.view.routes.itemAt(0, 0))
            print('action', action)
            item = self.view.routes.findItems(action['import'], Qt.MatchFixedString)[0]
            item.setSelected(True)
            self.view.delete_route.click()

        elif key == "Edit":
            self.operation_stack.print()
            self._edit.cancel(action)
            self.fill_controller.fill_points()

        elif key == "Remove":
            self._remove.cancel(action)
            if list(action.keys())[0] == 'Point':
                self.fill_controller.fill_points()
            else:
                self.fill_controller.fill_all_routes()

    def redo(self):
        print("redo starts")
        if len(HISTORY) <= self.view.stack.pointer + 1:
            return

        self.view.stack.pointer += 1
        act = HISTORY[self.view.stack.pointer]
        print('act', act)
        key = list(act.keys())[0]
        sub = act[key]

        if key == "ImportPolyline":
            pass

        elif key == "ImportGPX":
            pass

        elif key == "Edit":
            if list(sub.keys())[0] == "point":
                route = ROUTE_POOL[sub['point'][0]]
                new_val = route.points[sub['point'][1]]
                new_val.update({field_idx_to_name(sub['point'][2]): sub['point'][3]})
                route.points[sub['point'][1]] = new_val
                route.recount_length()
                route.recount_polyline()
                self.fill_controller.fill_points()
                self.fill_controller.fill_info(route.length, route.polyline)

        elif key == "Remove":
            if list(sub.keys())[0] == "Point":
                route = ROUTE_POOL[sub['Point'][0]]
                route.points.pop(sub['Point'][1])
                route.recount_length()
                route.recount_polyline()
                self.view.points.removeRow(sub['Point'][1])
                self.fill_controller.fill_info(route.length, route.polyline)

            elif list(sub.keys())[0] == "GPX":
                route = sub['GPX']
                items = self.view.routes.findItems(route.title, Qt.MatchFixedString)
                self.view.routes.removeRow(items[0].row())
                while self.view.info.rowCount() != 0:
                    self.view.info.removeRow(0)
                while self.view.points.rowCount() != 0:
                    self.view.points.removeRow(0)

                if len(ROUTE_POOL) == 0:
                    self.view.delete_route.setEnabled(False)
            elif list(sub.keys())[0] == "Polyline":
                route = sub['Polyline']
                items = self.view.routes.findItems(route.title, Qt.MatchFixedString)
                self.view.routes.removeRow(items[0].row())
                while self.view.info.rowCount() != 0:
                    self.view.info.removeRow(0)
                while self.view.points.rowCount() != 0:
                    self.view.points.removeRow(0)

                if len(ROUTE_POOL) == 0:
                    self.view.delete_route.setEnabled(False)




