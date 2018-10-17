from src.route.route_gpx import RouteGPX
from src.route.route_polyline import RoutePolyline


class CountTurns():
    def __init__(self, route):
        self.route = route
        pass

    def _get_cathegory(self, angle):
        angle = angle % 180
        if angle <= 5.5:
            return 0
        if angle <= 11:
            return 1
        if angle <= 33.5:
            return 2
        if angle <= 56.0:
            return 3
        if angle <= 78.5:
            return 4
        if angle <= 90.0:
            return 5
        if angle <= 135:
            return 6
        return 7

    def _count_turns(self):
        points = self.route.points
        turn_ar = [0] * 8
        print("_count_turns", points)
        for point in points:
            print("angle", point.get('course'))
            print("cat", self._get_cathegory(point.get('course')))
            turn_ar[self._get_cathegory(point.get('course'))] += 1
        return turn_ar

    def call_counter(self):
        if isinstance(self.route, RouteGPX):
            return self._count_turns()
        elif isinstance(self.route, RoutePolyline):
            return False

def call(route):
    counter = CountTurns(route)
    result = counter.call_counter()
    response = ''
    if result:
        for idx in range(len(result)):
            response += 'cathegory {0}: {1}\n'.format(idx, result[idx])
    else:
        response += 'incorrect data'
    return response
