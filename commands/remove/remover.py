from PyQt5 import QtWidgets
import gpxpy.gpx

from lab1.commands.utils import count_length
from lab1.route.utils import ROUTE_POOL
from lab1.utils.singleton import Singleton


class Remover(Singleton):
    def delete_route(self, route):
        return ROUTE_POOL.pop(route)

    def delete_point(self, point_dict):
        route = point_dict.get("route")
        items = point_dict.get("items")
        print("point_dict", [i.row() for i in items])
        for item in items:
            route.points.pop(item.row())
        route.recount_length()
        route.recount_polyline()
