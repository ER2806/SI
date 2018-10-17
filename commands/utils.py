import gpxpy.geo

HISTORY = []

def count_length(dots_array):
    def count_distance(first_point, second_point):
        return gpxpy.geo.distance(first_point.get('latitude'), first_point.get('longitude'),
                                  first_point.get('elevation', None),
                                  second_point.get('latitude'), second_point.get('longitude'),
                                  second_point.get('elevation', None))

    length = 0
    for idx in range(0, len(dots_array) - 1):
        length += count_distance(dots_array[idx], dots_array[idx + 1])
    return length / 1000

def field_idx_to_name(idx):
    if idx == 0:
        return "latitude"
    if idx == 1:
        return "longitude"
    if idx == 2:
        return "elevation"
