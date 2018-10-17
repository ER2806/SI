from PyQt5.QtCore import Qt
from src.commands.edit.edit import Edit
from src.commands.operation_stack import OperationStack
from src.controllers.fill_controller import FillController
from src.route.utils import ROUTE_POOL


class EditController():
    def __init__(self, view):
        self.view = view
        self.operation_stack = OperationStack()
        self._edit = Edit()
        self.fill_controller = FillController(self.view)
        self.counter = 0

    def edit_points(self):
        items = self.view.routes.selectedItems()
        route = ROUTE_POOL[self.view.routes.item(items[0].row(), 0).text()]
        points = self.view.points.selectedItems()
        changed_points = self._edit.execute({"route": route, "points": points})

        if changed_points:
            for point in changed_points:
                print("edit point", point)
                self.operation_stack.push({
                    "Edit": {
                        "point": [point.get('title'),
                                point.get('row'),
                                point.get('col'),
                                point.get('value'),
                                point.get('point')]
                    }
                })

            item_to_change = self.view.info.findItems("length", Qt.MatchFixedString)
            temp = self.view.info.item(item_to_change[0].row(), 1)
            temp.setText("{0}".format(route.length))


