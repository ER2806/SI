import gpxpy
import gpxpy.gpx

from lab1.route.routes_creator import RoutesCreator
from lab1.utils.singleton import Singleton


class ImporterGPX(Singleton):
    def make_import(self, filename):
        with open(filename, 'r') as gpx_file:
            try:
                gpx = gpxpy.parse(gpx_file)
                return RoutesCreator.create_route(gpx)
            except gpxpy.gpx.GPXXMLSyntaxException:
                raise IndexError

    def cancel(self):
        pass
