import unittest

import gpxpy

from lab1.route.routes_creator import RoutesCreator


class CreateRoute(unittest.TestCase):
    def test_create_from_polyline(self):
        test_polyline = '_mcbA~jiF~mme@oyo@~xyGn{|gV'
        route0 = RoutesCreator.create_route(test_polyline)
        print('point0', route0.points)

        good_points = [{'latitude': 11.0, 'longitude': -1.2},
                       {'latitude': 4.7, 'longitude': -0.95},
                       {'latitude': 3.252, 'longitude': -123.0}]
        good_length = 14233.73

        self.assertEqual(route0.points, good_points)
        self.assertEqual(round(route0.length, 2), good_length)
        self.assertEqual(route0.polyline, test_polyline)

    def test_create_from_gpx(self):
        gpx_source = ''
        with open('test_route.gpx', 'r') as gpx_file:
            gpx_source = gpxpy.parse(gpx_file)

        route0 = RoutesCreator.create_route(gpx_source)
        print('point0', route0.points)
        print(route0.length)
        print('polyline', route0.polyline)

        good_points = [{'latitude': 46.57608333, 'longitude': 8.89241667, 'elevation': 2376.0, 'course': 0},
         {'latitude': 46.57619444, 'longitude': 8.89252778, 'elevation': 2375.0, 'course': 0},
         {'latitude': 46.57641667, 'longitude': 8.89266667, 'elevation': 2372.0, 'course': 0},
         {'latitude': 46.5765, 'longitude': 8.89280556, 'elevation': 2373.0, 'course': 0},
         {'latitude': 46.57638889, 'longitude': 8.89302778, 'elevation': 2374.0, 'course': 0},
         {'latitude': 46.57652778, 'longitude': 8.89322222, 'elevation': 2375.0, 'course': 0},
         {'latitude': 46.57661111, 'longitude': 8.89344444, 'elevation': 2376.0, 'course': 0}]
        good_polyline = "o{g{Gsxgu@UUm@[O[Tk@[e@Ok@"
        good_length = 0.12

        self.assertEqual(route0.points, good_points)
        self.assertEqual(round(route0.length, 2), good_length)
        self.assertEqual(route0.polyline, good_polyline)
