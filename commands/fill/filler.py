from PyQt5.QtWidgets import QTableWidgetItem

from src.route.utils import ROUTE_POOL
from src.utils.singleton import Singleton


class Filler(Singleton):
    def fill_tables(self, menu):
        while menu.points.rowCount() != 0:
            menu.points.removeRow(0)
        while menu.info.rowCount() != 0:
            menu.info.removeRow(0)

        items = menu.routes.selectedItems()
        route = ROUTE_POOL[menu.routes.item(items[0].row(), 0).text()]

        for point in route.points:
            r = menu.points.rowCount()
            menu.points.insertRow(r)
            lat = QTableWidgetItem("{0:.5f}".format(point[0]))
            lon = QTableWidgetItem("{0:.5f}".format(point[1]))
            elev = QTableWidgetItem("{0:.5f}".format(point[2]))
            menu.points.setItem(r, 0, lat)
            menu.points.setItem(r, 1, lon)
            menu.points.setItem(r, 2, elev)

        menu.points.resizeColumnsToContents()

        menu.delete_point.setEnabled(True)

        for pr in route.__dict__:
            if pr != 'points':
                r = menu.info.rowCount()
                menu.info.insertRow(r)
                value = QTableWidgetItem("{0}".format(route.__dict__[pr]))
                pr = QTableWidgetItem("{0}".format(pr))
                menu.info.setItem(r, 0, pr)
                menu.info.setItem(r, 1, value)

        menu.info.resizeColumnsToContents()