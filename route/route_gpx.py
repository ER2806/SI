from polyline import encode
from lab1.commands import utils
from lab1.route.route import Route


class RouteGPX(Route):
    def __init__(self, source):
        super().__init__()
        print(source)
        points = []
        self.length = 0
        self.polyline = ''

        for track in source.tracks:
            for segment in track.segments:
                points += segment.points

        self.points = []
        for point in points:
            info = dict(latitude=point.latitude, longitude=point.longitude,
                        elevation=point.elevation or 0, course=point.course or 0)
            self.points.append(info)

        self.recount_length()
        self.recount_polyline()

    def recount_length(self):
        self.length = utils.count_length(self.points)

    def recount_polyline(self):
        self.polyline = encode(list(map(lambda x: [x.get('latitude'), x.get('longitude')], self.points)))

