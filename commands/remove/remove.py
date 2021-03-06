from lab1.commands.abstract_command import AbstractCommand
from lab1.commands.remove.remover import Remover
from lab1.commands.utils import count_length
from lab1.route.utils import ROUTE_POOL


class Remove(AbstractCommand):
    def __init__(self, exec=Remover()):
        self.remover = exec

    def execute(self, obj, type):
        if type == "route":
            return self.remover.delete_route(route=obj)
        elif type == "point":
            self.remover.delete_point(point_dict=obj)

    def cancel(self, name):
        key = list(name.keys())[0]
        if key == 'Polyline' or key == 'GPX':
            route = name[key]
            ROUTE_POOL.update({route.title: route})
        if key == 'Point':
            sub = name['Point']
            route = ROUTE_POOL[sub[0]]
            route.points.insert(sub[1], sub[2])
            route.recount_length()
            route.recount_polyline()
