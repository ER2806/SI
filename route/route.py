from src.route.utils import ROUTE_POOL


class Route:
    def __init__(self):
        route_idx = 0
        while "route{0}".format(route_idx) in ROUTE_POOL.keys():
            route_idx += 1
        self.title = "route{0}".format(route_idx)





