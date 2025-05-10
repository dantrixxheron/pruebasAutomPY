import pytest
from rentaAuto import comprobar_renta


def test_comprobar_renta_rango18():
    assert comprobar_renta(16) == (False, False)  # No permitido, sin tarifa extra    
    assert comprobar_renta(17) == (False, False)  # No permitido, sin tarifa extra
    assert comprobar_renta(18) == (True, True)  # Permitido, con tarifa extra
    assert comprobar_renta(19) == (True, True)  # Permitido, con tarifa extra
    assert comprobar_renta(20) == (True, True)  # Permitido, con tarifa extra
    
def test_comprobar_renta_rango25():
    assert comprobar_renta(23) == (True, True)  # Permitido, con tarifa extra
    assert comprobar_renta(24) == (True, True)  # Permitido, con tarifa extra
    assert comprobar_renta(25) == (True, False)  # Permitido, sin tarifa extra
    assert comprobar_renta(26) == (True, False)  # Permitido, sin tarifa extra
    assert comprobar_renta(27) == (True, False)  # Permitido, sin tarifa extra
    
def test_comprobar_renta_rango65():
    assert comprobar_renta(63) == (True, False)  # Permitido, sin tarifa extra
    assert comprobar_renta(64) == (True, False)  # Permitido, sin tarifa extra
    assert comprobar_renta(65) == (True, False)  # Permitido, sin tarifa extra
    assert comprobar_renta(66) == (True, True)  # Permitido, con tarifa extra
    assert comprobar_renta(67) == (True, True)  # Permitido, con tarifa extra
    
def test_comprobar_renta_rango80():
    assert comprobar_renta(78) == (True, True)  # Permitido, con tarifa extra
    assert comprobar_renta(79) == (True, True)  # Permitido, con tarifa extra
    assert comprobar_renta(80) == (True, True)  # Permitido, con tarifa extra
    assert comprobar_renta(81) == (False, False)  # No permitido, sin tarifa extra
    assert comprobar_renta(82) == (False, False)  # No permitido, sin tarifa extra