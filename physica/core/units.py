from sympy import Symbol

unit_systems = ['SI', 'CGS']

class dim_analysis:
    basic_dims = {
        'length': Symbol('L'), 
        'time': Symbol('T'), 
        'mass': Symbol('M'), 
        'temperatura': Symbol('T'),
        'electric_current': Symbol('I'),
        }
    
    
class Unit(object):
    def __init__(self, system, value) -> None:
        self.system = system
        self.value = value