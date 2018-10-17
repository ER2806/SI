import gpxpy.gpx
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from src.commands.operation_stack import OperationStack
from src.commands.remove.remove import Remove
from src.route.utils import ROUTE_POOL


class RemoveController():
    def __init__(self, view):
        self.view = view
        self._remove = Remove()
        self.operation_stack = OperationStack()

    def remove_route(self):
        items = self.view.routes.selectedItems()

        if len(items) == 0:
            QtWidgets.QMessageBox.warning(None, "Warning", "Routes was not selected!",
                                          buttons=QtWidgets.QMessageBox.Ok)
            return
        route = self.view.routes.item(items[0].row(), 0).text()

        deleted_route = self._remove.execute(route, "route")

        if deleted_route.type == gpxpy.gpx.GPX:
            self.operation_stack.push({
                "Remove": {
                    "GPX": route
                }
            })
        elif deleted_route.type == str:
            self.operation_stack.push({
                "Remove": {
                    "Polyline": route
                }
            })

        self.view.routes.removeRow(items[0].row())
        while self.view.info.rowCount() != 0:
            self.view.info.removeRow(0)
        while self.view.points.rowCount() != 0:
            self.view.points.removeRow(0)

        if not ROUTE_POOL:
            self.view.delete_route.setEnabled(False)
            self.view.delete_point.setEnabled(False)

    def remove_point(self):
        items = self.view.routes.selectedItems()
        route = ROUTE_POOL[self.view.routes.item(items[0].row(), 0).text()]
        print("remove_point", items)
        items = self.view.points.selectedItems()

        for i in items:
            self.view.stack.push({
                "Remove": {
                    "Point": [route.title, i.row(), route.points[i.row()]]
                }
            })

        self._remove.execute({"route": route, "items": items}, "point")

        length_on_view = self.view.info.findItems("length", Qt.MatchFixedString)
        temp = self.view.info.item(length_on_view[0].row(), 1)
        temp.setText("{0}".format(route.length))

        for i in items:
            self.view.points.removeRow(i.row())

        if len(route.points) == 0:
            self.view.delete_point.setEnabled(False)






