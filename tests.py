import unittest

from lab1 import test_convert_to_polyline, test_delete_route, test_import_polyline, test_create_point, test_create_route, \
    test_edit_point, test_plot

'''
отображение карты высот (проверять данные для отображения, либо
невозможность построить карту при отсутствии данных).
'''

if __name__ == '__main__':
    suite = unittest.TestSuite()

    modules = [test_convert_to_polyline,
               test_delete_route,
               test_import_polyline,
               test_create_point,
               test_create_route,
               test_edit_point,
               test_plot]

    for module in modules:
        suite.addTest(unittest.TestLoader().loadTestsFromModule(module))

    unittest.TextTestRunner(verbosity=2).run(suite)


