import unittest

from lab1.commands.imports.importer_polyline import ImporterPolyline
from lab1.route.route_polyline import RoutePolyline


class ImportPolyline(unittest.TestCase):
    def test_import(self):
        self.test_polyline = '_mcbA~jiF~mme@oyo@~xyGn{|gV'

        importer = ImporterPolyline()
        route0 = importer.make_import(self.test_polyline)
        route1 = RoutePolyline(self.test_polyline)
        assert(route0, route1)