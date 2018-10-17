from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtChart import QChart, QLineSeries

from src.commands.utils import count_length
from src.controllers.module_controller import ModuleController
from src.route.utils import ROUTE_POOL

class FillController():
    def __init__(self, view):
        self.view = view
        self.module_controller = ModuleController(self.view)
        self.COUNTER = 0

    def fill_routes(self):
        print(ROUTE_POOL)
        for name, route in ROUTE_POOL.items():
            if route:
                print('route', route)
                self.view.delete_route.setEnabled(True)
                base_route = self.view.routes.rowCount()
                self.view.routes.insertRow(base_route)
                title = QTableWidgetItem("{0}".format(route.title))
                self.view.routes.setItem(base_route, 0, title)
                self.view.routes.resizeColumnsToContents()

    def _enable_additions(self):
        self.view.delete_point.setEnabled(True)
        self.module_controller.activate_buttons()

    def fill_points(self):
        self.COUNTER += 1
        print('counter', self.COUNTER)
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

        self.view.points.resizeColumnsToContents()

        for pr in route.__dict__:
            if pr != 'points':
                r = self.view.info.rowCount()
                self.view.info.insertRow(r)
                value = QTableWidgetItem("{0}".format(route.__dict__[pr]))
                pr = QTableWidgetItem("{0}".format(pr))
                self.view.info.setItem(r, 0, pr)
                self.view.info.setItem(r, 1, value)

        self.view.info.resizeColumnsToContents()
        self._construct_plot(route)
        self._enable_additions()

    @staticmethod
    def _get_series_for_plot(route):
        series_array = []
        series_array.append([0, route.points[0].get('elevation', 0)])
        length_sum = 0
        for idx in range(1, len(route.points)):
            length_sum += count_length(route.points[idx-1:idx+1])
            series_array.append([length_sum, route.points[idx].get('elevation', 0)])

        return series_array


    def _construct_plot(self, route):
        self.chart = QChart()
        self.series = QLineSeries()

        self.series_array = self._get_series_for_plot(route)
        print(self.series_array)
        for series in self.series_array:
            self.series.append(*series)

        self.chart.addSeries(self.series)
        print(self.chart)
        self.chart.setTitle('Example')
        self.chart.createDefaultAxes()
        self.view.widgetA.setChart(self.chart)

        return self.series_array
