import pytest
from hypothesis import given, strategies as st
from rentaAuto import comprobar_renta

@given(st.integers(min_value=0, max_value=120))
def test_comprobar_renta(edad):
    permitido, tarifa_extra = comprobar_renta(edad)

    if edad < 18 or edad > 80:
        assert permitido is False
        assert tarifa_extra is False
    elif 18 <= edad <= 24 or 66 <= edad <= 80:
        assert permitido is True
        assert tarifa_extra is True
    else:  # edades entre 25 y 65
        assert permitido is True
        assert tarifa_extra is False
