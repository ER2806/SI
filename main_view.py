from PyQt5 import QtWidgets, uic

from lab1.commands.operation_stack import OperationStack
from lab1.controllers.edit_controller import EditController
from lab1.controllers.fill_controller import FillController
from lab1.controllers.import_controller import ImportController
from lab1.controllers.module_controller import ModuleController
from lab1.controllers.remove_controller import RemoveController
from lab1.controllers.undo_redu_controller import UndoRedoController



class MainView(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi("editor.ui", self)

        self.import_controller = ImportController(self)
        self.remove_controller = RemoveController(self)
        self.edit_controller = EditController(self)
        self.fill_controller = FillController(self)
        self.undo_redo_controller = UndoRedoController(self)
        self.module_controller = ModuleController(self)

        self.stack = OperationStack()
        self.stack.menu = self

        self.delete_route.setEnabled(False)
        self.delete_point.setEnabled(False)
        self.redo.setEnabled(False)
        self.undo.setEnabled(False)
        self.count_turns.setEnabled(False)
        self.count_slopes.setEnabled(False)
        self.count_desc_asc.setEnabled(False)
        self.call_module.setEnabled(False)

        self.info.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.routes.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.redo.clicked.connect(lambda: self.undo_redo_controller.redo())
        self.undo.clicked.connect(lambda: self.undo_redo_controller.undo())

        self.import_gpx.clicked.connect(lambda: self.import_controller.import_gpx())
        self.import_polyline.clicked.connect(lambda: self.import_controller.import_polyline())
        self.delete_route.clicked.connect(lambda: self.remove_controller.remove_route())
        self.delete_point.clicked.connect(lambda: self.remove_controller.remove_point())
        self.count_turns.clicked.connect(lambda: self.module_controller.count_turns())
        self.count_slopes.clicked.connect(lambda: self.module_controller.count_slopes())
        self.count_desc_asc.clicked.connect(lambda: self.module_controller.count_desc_asc())
        self.call_module.clicked.connect(lambda: self.module_controller.call_runtime_module())

        self.routes.cellClicked.connect(lambda: self.fill_controller.fill_points())
        self.points.cellChanged.connect(lambda: self.edit_controller.edit_points())
