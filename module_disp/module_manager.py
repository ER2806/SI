from src.utils.singleton import Singleton


class ModuleManager(Singleton):
    def __init__(self):
        self.modules_dict = dict(turn_counter=None)

        self._register_modules()
        print('init')

    def _register_module(self, module_name):
        try:
            if module_name == "turn_counter":
                import src.module_disp.modules.turn_counter as turn_counter
                self.modules_dict.update(dict(turn_counter=turn_counter))
            elif module_name == "slopes_counter":
                import src.module_disp.modules.slopes_counter as slopes_counter
                self.modules_dict.update(dict(slopes_counter=slopes_counter))
            elif module_name == "desc_asc_counter":
                import src.module_disp.modules.desc_asc_counter as desc_asc_counter
                self.modules_dict.update(dict(desc_asc_counter=desc_asc_counter))
        except ModuleNotFoundError as e:
            print("not found")

    def _register_modules(self):
        self._register_module('turn_counter')
        self._register_module('slopes_counter')
        self._register_module('desc_asc_counter')

    def get_modules(self):
        return list(self.modules_dict.keys())

    def check_module(self, module_name):
        print("check_module", self.modules_dict)
        if self.modules_dict.get(module_name, None):
            return True
        return False

    def call_module(self, module_name, args):
        module = self.modules_dict.get(module_name, None)
        if module:
            return module.call(args)

