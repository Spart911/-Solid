class Engine:
    def start(self):
        pass

class PetrolEngine(Engine):
    def start(self):
        pass

class DieselEngine(Engine):
    def start(self):
        pass

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()