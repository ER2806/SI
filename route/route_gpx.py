from polyline import encode
from src.commands import utils
from src.route.route import Route


class RouteGPX(Route):
    def __init__(self, source):
        super().__init__()
        print(source)
        points = []
        #self.type = type(source)
        for track in source.tracks:
            for segment in track.segments:
                points += segment.points

        self.polyline = encode(list(map(lambda x: [x.latitude, x.longitude], points)))

        self.points = []
        for point in points:
            info = dict(latitude=point.latitude, longitude=point.longitude,
                        elevation=point.elevation or 0, course=point.course or 0)
            self.points.append(info)

        self.length = utils.count_length(self.points)

