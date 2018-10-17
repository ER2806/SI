import unittest

import gpxpy
from lab1.controllers.fill_controller import FillController
from lab1.route.routes_creator import RoutesCreator


class Plot(unittest.TestCase):
    def test_plot(self):
        gpx_source = ''
        with open('test_route.gpx', 'r') as gpx_file:
            gpx_source = gpxpy.parse(gpx_file)

        route0 = RoutesCreator.create_route(gpx_source)

        result = FillController._get_series_for_plot(route0)
        for idx in range(len(result)):
            result[idx][0] = round(result[idx][0], 2)
            result[idx][1] = round(result[idx][1], 2)
        print("test_plot_result", result)

        good_points = [[0, 2376.0],
                       [0.02, 2375.0],
                       [0.04, 2372.0],
                       [0.06, 2373.0],
                       [0.08, 2374.0],
                       [0.10, 2375.0],
                       [0.12, 2376.0]]

        self.assertEqual(result, good_points)
