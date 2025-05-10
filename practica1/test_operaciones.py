import pytest
from operaciones import suma, resta, multiplicacion, division

def test_suma():
    assert suma(2, 3) == 5 # la suma de 2 y 3 es 5
    assert suma(-1, 1) == 0 # la suma de -1 y 1 es 0
    assert suma(0, 0) == 0 # la suma de 0 y 0 es 0
    assert suma(-1, -1) == -2 # la suma de -1 y -1 es -2
    
def test_resta():
    assert resta(5, 3) == 2 # la resta de 5 y 3 es 2
    assert resta(0, 0) == 0 # la resta de 0 y 0 es 0
    assert resta(-1, -1) == 0 # la resta de -1 y -1 es 0
    assert resta(-1, 1) == -2 # la resta de -1 y 1 es -2

def test_multiplicacion():
    assert multiplicacion(2, 3) == 6 # la multiplicacion de 2 y 3 es 6
    assert multiplicacion(-1, 1) == -1 # la multiplicacion de -1 y 1 es -1
    assert multiplicacion(0, 5) == 0 # la multiplicacion de 0 y 5 es 0
    assert multiplicacion(-1, -1) == 1 # la multiplicacion de -1 y -1 es 1

def test_division():
    assert division(6, 3) == 2 # la division de 6 y 3 es 2
    assert division(-1, 1) == -1 # la division de -1 y 1 es -1
    assert division(0, 5) == 0 # la division de 0 y 5 es 0
    with pytest.raises(ValueError): # se espera un ValueError al dividir entre cero
        division(1, 0)
    with pytest.raises(ValueError): # se espera un ValueError al dividir entre cero
        division(-1, 0)
    with pytest.raises(ValueError): # se espera un ValueError al dividir entre cero
        division(0, 0)