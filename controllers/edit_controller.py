from PyQt5.QtCore import Qt
from lab1.commands.edit.edit import Edit
from lab1.commands.operation_stack import OperationStack
from lab1.controllers.fill_controller import FillController
from lab1.route.utils import ROUTE_POOL


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
        if not points:
            return

        changed_points = self._edit.execute({"route": route, "points": points})

        if changed_points:
            for point in changed_points:
                self.operation_stack.push({
                    "Edit": {
                        "point": [point.get('title'),
                                point.get('row'),
                                point.get('col'),
                                point.get('value'),
                                point.get('point')]
                    }
                })
            self.fill_controller.fill_info(route.length, route.polyline)

        self.fill_controller.construct_plot(route)

