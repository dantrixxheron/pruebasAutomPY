import pytest
from rentaAuto import comprobar_renta,renta

#Siguen siendo basados en ejemplos pero ahora son más sinteticos y claros
@pytest.mark.parametrize(("edad","permitido","tarifa_extra"),[
    (16, False, False),  # No permitido, sin tarifa extra
    (17, False, False),  # No permitido, sin tarifa extra
    (18, True, True),    # Permitido, con tarifa extra
    (19, True, True),    # Permitido, con tarifa extra
    (20, True, True),    # Permitido, con tarifa extra
    (23, True, True),    # Permitido, con tarifa extra
    (24, True, True),    # Permitido, con tarifa extra
    (25, True, False),   # Permitido, sin tarifa extra
    (26, True, False),   # Permitido, sin tarifa extra
    (27, True, False),   # Permitido, sin tarifa extra
    (63, True, False),   # Permitido, sin tarifa extra
    (64, True, False),   # Permitido, sin tarifa extra
    (65, True, False),   # Permitido, sin tarifa extra
    (66, True, True),    # Permitido, con tarifa extra
    (67, True, True),    # Permitido, con tarifa extra
    (78, True, True),    # Permitido, con tarifa extra
    (79, True, True),    # Permitido, con tarifa extra
    (80, True ,True),     # Permitido ,con tarifa extra 
])

def test_valores_limite(edad, permitido, tarifa_extra):
    comprobar_renta(edad)
    assert renta.permitido == permitido
    assert renta.tarifa_extra == tarifa_extra