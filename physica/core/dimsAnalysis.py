from sympy import Symbol

unit_systems = ['SI', 'CGS']

dims = {
    'length': Symbol('L'), 
    'time': Symbol('T'), 
    'mass': Symbol('M'), 
    'temperatura': Symbol('T'),
    'electric_current': Symbol('I'),
}
comp_dims = {
    'speed': dims['length']/dims['time'],
    'force': dims['mass']*dims['length']/dims['time']**2,
}

def analysis(expr: Symbol):
    
    for i in dims:
        if dims[i] == expr:
            return i
    for i in comp_dims:
        if comp_dims[i] == expr:
            return i