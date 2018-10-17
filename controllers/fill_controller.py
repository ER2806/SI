from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtChart import QChart, QLineSeries

from lab1.commands.utils import count_length
from lab1.controllers.module_controller import ModuleController
from lab1.route.route_gpx import RouteGPX
from lab1.route.utils import ROUTE_POOL

class FillController():
    def __init__(self, view):
        self.view = view
        self.module_controller = ModuleController(self.view)

    def fill_route(self, route):
        self.view.delete_route.setEnabled(True)
        base_route = self.view.routes.rowCount()
        self.view.routes.insertRow(base_route)
        title = QTableWidgetItem("{0}".format(route.title))
        self.view.routes.setItem(base_route, 0, title)


    def fill_all_routes(self):
        for name, route in ROUTE_POOL.items():
            if route:
                self.fill_route(route)

    def fill_info(self, length, polyline):
        item_to_change = self.view.info.findItems("length", Qt.MatchFixedString)
        temp = self.view.info.item(item_to_change[0].row(), 1)
        temp.setText("{0}".format(length))

        item_to_change = self.view.info.findItems("polyline", Qt.MatchFixedString)
        temp = self.view.info.item(item_to_change[0].row(), 1)
        temp.setText("{0}".format(polyline))



    def _enable_additions(self):
        self.view.delete_point.setEnabled(True)
        self.module_controller.activate_buttons()

    def fill_points(self):
        while self.view.points.rowCount() != 0:
            self.view.points.removeRow(0)
        while self.view.info.rowCount() != 0:
            self.view.info.removeRow(0)

        items = self.view.routes.selectedItems()
        route = ROUTE_POOL[self.view.routes.item(items[0].row(), 0).text()]

        for point in route.points:
            r = self.view.points.rowCount()
            self.view.points.insertRow(r)
            lat = QTableWidgetItem("{0:.5f}".format(point.get('latitude')))
            lon = QTableWidgetItem("{0:.5f}".format(point.get('longitude')))
            elev = QTableWidgetItem("{0:.5f}".format(point.get('elevation')) if point.get('elevation', None) else 'None')
            self.view.points.setItem(r, 0, lat)
            self.view.points.setItem(r, 1, lon)
            self.view.points.setItem(r, 2, elev)

        for pr in route.__dict__:
            if pr != 'points':
                r = self.view.info.rowCount()
                self.view.info.insertRow(r)
                value = QTableWidgetItem("{0}".format(route.__dict__[pr]))
                pr = QTableWidgetItem("{0}".format(pr))
                self.view.info.setItem(r, 0, pr)
                self.view.info.setItem(r, 1, value)

        self.construct_plot(route)
        self._enable_additions()
        self.fill_info(route.length, route.polyline)

    @staticmethod
    def _get_series_for_plot(route):
        series_array = []
        series_array.append([0, route.points[0].get('elevation', 0)])
        length_sum = 0
        for idx in range(1, len(route.points)):
            length_sum += count_length(route.points[idx-1:idx+1])
            series_array.append([length_sum, route.points[idx].get('elevation', 0)])

        return series_array


    def construct_plot(self, route):
        if not isinstance(route, RouteGPX):
            return

        self.chart = QChart()
        self.series = QLineSeries()

        self.series_array = self._get_series_for_plot(route)
        #print(self.series_array)
        for series in self.series_array:
            self.series.append(*series)

        self.chart.addSeries(self.series)
        #print(self.chart)
        self.chart.setTitle(route.title)
        self.chart.createDefaultAxes()
        self.view.widgetA.setChart(self.chart)

        return self.series_array
