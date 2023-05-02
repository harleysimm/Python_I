class Empleado:
    sueldo_base = 500000

    def __init__(self, _name):
        self.__name = _name

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, _name):
        self.__name = _name

    @classmethod
    def get_sueldo_base(cls):
        return cls.sueldo_base

    @classmethod
    def set_sueldo_base(cls, _sueldo):
        cls.sueldo_base = _sueldo