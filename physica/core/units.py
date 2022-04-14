from sympy import Symbol, symbols

unit_systems = ['SI', 'CGS']

dimensional_analysis = {'length': Symbol('L'), 'time': 'T', 'mass': 'M', 'temperatura': 'T', }

class Unit(object):
    def __init__(self, system, value) -> None:
        self.system = system
        self.value = value