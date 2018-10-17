from lab1.route.route_gpx import RouteGPX
from lab1.route.route_polyline import RoutePolyline
import gpxpy.gpx


class RoutesCreator:  # фабричный метод
    @staticmethod
    def create_route(source):
        print("create_route", source)
        if type(source) == gpxpy.gpx.GPX:
            return RouteGPX(source)
        elif type(source) == str:
            return RoutePolyline(source)

