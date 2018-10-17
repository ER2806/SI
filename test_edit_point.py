import unittest

import gpxpy

from lab1.commands.edit.editor import Editor
from lab1.commands.imports.importer_polyline import ImporterPolyline
from lab1.route.routes_creator import RoutesCreator

class EditPoint(unittest.TestCase):
    def test_edit_point(self):
        def prepare_item(row, column, text):
            class Item():
                def __init__(self, row, column, text):
                    self.r = row
                    self.col = column
                    self.txt = text
                def row(self):
                    return self.r
                def column(self):
                    return self.col
                def text(self):
                    return self.txt
            return Item(row, column, text)

        self.test_polyline = '_mcbA~jiF~mme@oyo@~xyGn{|gV'
        self.editor = Editor()

        importer = ImporterPolyline()
        route0 = importer.make_import(self.test_polyline)
        self.editor.edit_points({'route': route0, 'points': [prepare_item(0, 0, 1)]})

        good_points = [{'latitude': 1.0, 'longitude': -1.2},
                       {'latitude': 4.7, 'longitude': -0.95},
                       {'latitude': 3.252, 'longitude': -123.0}]
        good_length = 13944.69

        self.assertEqual(route0.points, good_points)
        self.assertEqual(round(route0.length, 2), good_length)
