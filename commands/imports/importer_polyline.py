from src.route.routes_creator import RoutesCreator
from src.utils.singleton import Singleton


class ImporterPolyline(Singleton):
    def make_import(self, polyline):
        route = RoutesCreator.create_route(polyline)
        print("importer", route)
        return route

    def cancel(self):
        pass
