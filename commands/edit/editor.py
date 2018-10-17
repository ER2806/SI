import src.commands.utils as command_utils
from src.route.utils import ROUTE_POOL
from src.utils.singleton import Singleton


class Editor(Singleton):
    def edit_points(self, items):
        print("edit_points", items)
        route = items.get("route")
        points = items.get("points")
        edited_points = []

        if not points:
            return {}

        for point in points:
            print('point_column', point)
            field = command_utils.field_idx_to_name(point.column())
            row = point.row()
            col = point.column()
            print("point", point.row(), point.column(), point.text(), route.points[row], route.points[row].get(field))
            if route.points[row].get(field) != float(point.text()):
                edited_points.append(dict(title=route.title,
                                          row=row,
                                          col=col,
                                          value=float(point.text()),
                                          point=route.points[row].get(field)))
                route.points[row].update({field: float(point.text())})

        length = command_utils.count_length(route.points)
        route.length = length

        return edited_points

    def cancel_edit(self, act):
        print('0', act['point'])
        route = ROUTE_POOL.get(act['point'][0])
        print('2', act['point'][2])
        new_val = route.points[act['point'][1]]
        print({command_utils.field_idx_to_name(act['point'][2]): act['point'][4]})
        new_val.update({command_utils.field_idx_to_name(act['point'][2]): act['point'][4]})
        route.points[act['point'][1]] = new_val
        print('new points', route.points)
        route.length = command_utils.count_length(route.points)

