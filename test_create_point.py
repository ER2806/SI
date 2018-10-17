import unittest

from src.commands.imports.importer_polyline import ImporterPolyline


class CreatePoint(unittest.TestCase):
    def test_create(self):
        self.test_polyline = '_mcbA~jiF~mme@oyo@~xyGn{|gV'
        self.test_polyline = ['_mcbA~jiF~mme@oyo@~xyGn{|gV', 'gooaI_ddw~@gztnC_t~pt@~hiaCndstsBw{dwBobvA',
                              'nlxY~dkN~y{~EoasDox}~Efo~A~un[deO']
        importer = ImporterPolyline()
        route0 = importer.make_import(self.test_polyline[0])
        print('point0', route0.points[0])

        self.assertEqual(route0.points[0].get('latitude'), 11)
        self.assertEqual(route0.points[0].get('longitude'), -1.2)
