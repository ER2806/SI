from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtWidgets

from lab1.commands.imports.import_gpx import ImportGPX
from lab1.commands.imports.import_polyline import ImportPolyline
from lab1.commands.operation_stack import OperationStack
from lab1.controllers.fill_controller import FillController
from lab1.route.utils import ROUTE_POOL


class ImportController():
    def __init__(self, view):
        self.fill_controller = FillController(view)
        self.view = view
        self.operation_stack = OperationStack()
        self._import_gpx = ImportGPX()
        self._import_polyline = ImportPolyline()

    def import_gpx(self):
        self.view.statusbar.showMessage("choose file")
        file = QtWidgets.QFileDialog.getOpenFileName(parent=self.view, caption="Open file...", filter="*.gpx")
        if file == ('', ''):
            QtWidgets.QMessageBox.warning(None, "Warning", "File was not selected!",
                                          buttons=QtWidgets.QMessageBox.Ok)
        else:
            route = self._import_gpx.execute(file[0])
            ROUTE_POOL.update({route.title: route})
            if route:
                self.operation_stack.push({
                        "ImportGPX": {
                            "import": route.title
                        }
                    })
                self.view.statusbar.showMessage("The route from {0} was loaded.".format(file[0]))
                self.fill_controller.fill_route(route)
            else:
                QtWidgets.QMessageBox.critical(None, "Error!", "Error!",
                                                   defaultButton=QtWidgets.QMessageBox.Ok)
        #print('import_gpx_controller', ROUTE_POOL)

    def import_polyline(self):
        self.view.statusbar.showMessage("Enter polyline.")
        polyline, status = QtWidgets.QInputDialog.getText(self.view, "Input polyline.", "",
                                                          text="soe~Hovqu@dCrk@xZpR~VpOfwBmtG")
        if status:
            route = self._import_polyline.execute(polyline)
            print("polyline_route", route.title)
            ROUTE_POOL.update({route.title: route})
            self.view.stack.push({
                "ImportPolyline": {
                    "import": route.title
                }
            })
            self.view.statusbar.showMessage("The polyline {0} with title {1} was loaded.".format(polyline, route.title))
            self.fill_controller.fill_route(route)

        else:
            QtWidgets.QMessageBox.warning(None, "Warning", "Polyline enter error!",
                                          buttons=QtWidgets.QMessageBox.Ok)

        print('import_polyline_controller', ROUTE_POOL)
