import unittest

from src.commands.remove.remover import Remover
from src.route.routes_creator import RoutesCreator
from src.route.utils import ROUTE_POOL


class DeleteRoute(unittest.TestCase):
    def test_delete(self):
        route = RoutesCreator.create_route('_mcbA~jiF~mme@oyo@~xyGn{|gV')
        route_name = 'route0'
        remover = Remover()
        ROUTE_POOL.update({route_name: route})
        remover.delete_route(route_name)
        self.assertEqual(ROUTE_POOL, {})