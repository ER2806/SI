from polyline import decode
from src.commands import utils
from src.route.route import Route


class RoutePolyline(Route):
    def __init__(self, source):
        super().__init__()
        print(source)
        self.polyline = source

        print("_fill_polyline")
        try:
            self.points = decode(source)
        except IndexError:
            raise PolylineInputError

        self.points = list(map(lambda x: dict(latitude=x[0], longitude=x[1]), self.points))
        self.length = utils.count_length(self.points)
        print("points", self.points)

