import pytest
import hypothesis.strategies as st
from hypothesis import given, settings, Verbosity
from triangulos import comprobarTriangulo
@settings(max_examples=100, verbosity=Verbosity.verbose)
@given(st.integers(), st.integers(), st.integers())
def test_comprobar_triangulo(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        assert comprobarTriangulo(a, b, c) == False
    elif a + b <= c or a + c <= b or b + c <= a:
        assert comprobarTriangulo(a, b, c) == False
    elif a == b and b == c:
        assert comprobarTriangulo(a, b, c) == "Equilátero"
    elif a == b or a == c or b == c:
        assert comprobarTriangulo(a, b, c) == "Isósceles"
    else:
        assert comprobarTriangulo(a, b, c) == "Escaleno"