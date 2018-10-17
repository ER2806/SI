from math import atan, degrees
import gpxpy.geo
from lab1.route.route_gpx import RouteGPX
from lab1.route.route_polyline import RoutePolyline


class SlopesCounter():
    def __init__(self, route):
        self.route = route
        self.STEEP_SLOPE_BOARDER = 15
        pass

    def _count_distance(self, first_point, second_point):
        return gpxpy.geo.distance(first_point.get('latitude'), first_point.get('longitude'),
                                    first_point.get('elevation', None),
                                    second_point.get('latitude'), second_point.get('longitude'),
                                    second_point.get('elevation', None))

    def _check(self):
        emptyFlag = True
        for point in self.route.points:
            elev = point.get('elevation', None)
            if elev:
                return False
        return emptyFlag

    def _count_slopes(self):
        if self._check():
            return False

        counter = 0
        points = self.route.points
        for idx in range(len(points)):
            prev = points[idx - 1]
            curr = points[idx]
            distance = self._count_distance(prev, curr)
            if distance != 0:
                height = curr.get('elevation', 0) - prev.get('elevation', 0)
                print('atan', degrees(atan(height / distance)), 'otn', height / distance,
                      'hei', height, 'alt0', curr.get('elevation', 0),
                      'alt1', prev.get('elevation', 0), 'dist', distance)
                if abs(degrees(atan(height / distance))) % 90 > self.STEEP_SLOPE_BOARDER:
                    counter += 1
        return counter

    def call_counter(self):
        if isinstance(self.route, RouteGPX):
            return self._count_slopes()
        elif isinstance(self.route, RoutePolyline):
            return False

def call(route):
    counter = SlopesCounter(route)
    result = counter.call_counter()
    print('result', result)
    response = ''
    if result:
        response += 'Amount of steep slopes: {0}\n'.format(result)
    else:
        response += 'incorrect data\n'
    return response
