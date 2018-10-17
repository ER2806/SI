from polyline import decode, encode
from lab1.commands import utils
from lab1.route.route import Route


class RoutePolyline(Route):
    def __init__(self, source):
        super().__init__()
        print(source)
        self.polyline = source
        self.length = 0

        print("_fill_polyline")
        self.points = decode(source)

        self.points = list(map(lambda x: dict(latitude=x[0], longitude=x[1]), self.points))
        self.recount_length()

    def recount_length(self):
        self.length = utils.count_length(self.points)

    def recount_polyline(self):
        self.polyline = encode(list(map(lambda x: [x.get('latitude'), x.get('longitude')], self.points)))




