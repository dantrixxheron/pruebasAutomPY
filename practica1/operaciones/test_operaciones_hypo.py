import pytest
import hypothesis.strategies as st
from hypothesis import given, settings, Verbosity
from operaciones import suma, resta, multiplicacion, division

@settings(max_examples=100, verbosity=Verbosity.verbose)
@given(st.integers(), st.integers())
def test_suma(a, b):
    assert suma(a, b) == a + b

@given(st.integers(), st.integers())
def test_resta(a, b):  # ← Agrega los parámetros aquí también
    assert resta(a, b) == a - b

@given(st.integers(), st.integers())
def test_multiplicacion(a, b):  # ← Igual aquí
    assert multiplicacion(a, b) == a * b

@given(st.integers(), st.integers())
def test_division(a, b):  # ← Y aquí
    if b == 0:
        with pytest.raises(ValueError):
            division(a, b)
    else:
        assert division(a, b) == a / b
