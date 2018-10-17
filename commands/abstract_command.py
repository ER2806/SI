import abc

class AbstractCommand:
    @abc.abstractmethod
    def execute(self, *args):
        pass

    @abc.abstractmethod
    def cancel(self, *args):
        pass

