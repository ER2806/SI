from math import degrees, atan

from lab1.route.route_gpx import RouteGPX
from lab1.route.route_polyline import RoutePolyline
import gpxpy.geo


class CountDescAsc():
    def __init__(self, route):
        self.route = route
        self.LENGTH_CATHEGORIES_COUNT = 3
        self.STEEPNESS_CATHEGORIES_COUNT = 5

    def _count_distance(self, first_point, second_point):
        return gpxpy.geo.distance(first_point.get('latitude'), first_point.get('longitude'),
                                    first_point.get('elevation', None),
                                    second_point.get('latitude'), second_point.get('longitude'),
                                    second_point.get('elevation', None))

    def _count_desc_asc(self):
        if self._check():
            return False
        caths = [[0] * self.STEEPNESS_CATHEGORIES_COUNT] * self.LENGTH_CATHEGORIES_COUNT
        points = self.route.points
        for idx in range(1, len(points)):
            prev = points[idx - 1]
            curr = points[idx]
            length_cath = self._get_length_cathegory(prev, curr)
            steepness_cath = self._get_steepness_cathegory(prev, curr)
            caths[length_cath][steepness_cath] += 1
        return caths

    def _check(self):
        emptyFlag = True
        for point in self.route.points:
            elev = point.get('elevation', None)
            if elev:
                return False
        return emptyFlag

    def _get_length_cathegory(self, a, b):
        distance = self._count_distance(a, b) * 1000
        if distance > 500:
            return 0
        elif distance >= 50:
            return 1
        return 2

    def _get_steepness_cathegory(self, a, b):
        height = a.get('elevation', 0) - b.get('elevation', 0)
        distance = self._count_distance(a, b)
        if distance != 0:
            angle = abs(degrees(atan(height / distance))) % 90
            print(angle)
            if angle >= 35.0:
                return 0
            if angle >= 15.0:
                return 1
            if angle >= 8.0:
                return 2
            if angle >= 4.0:
                return 3
        return 4

    def call_counter(self):
        if isinstance(self.route, RouteGPX):
            return self._count_desc_asc()
        elif isinstance(self.route, RoutePolyline):
            return []


def call(route):
    counter = CountDescAsc(route)
    result = counter.call_counter()
    response = ''
    if result:
        for len_idx in range(len(result)):
            for steep_idx in range(len(result[len_idx])):
                response += 'len cath - {0}; steep - {1}: {2}\n'.format(len_idx, steep_idx,
                                                                        result[len_idx][steep_idx])
    else:
        response += 'incorrect data'
    return response
