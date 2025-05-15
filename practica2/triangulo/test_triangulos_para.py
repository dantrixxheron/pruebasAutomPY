import pytest
from triangulos import comprobarTriangulo

@pytest.mark.parametrize(("a", "b", "c", "resultado"), [
    (3, 4, 5, "Escaleno"),  # Triángulo escaleno
    (5, 5, 8, "Isósceles"),  # Triángulo isósceles
    (7, 7, 7, "Equilátero"),  # Triángulo equilátero
    (0, 4, 5, False),  # Lado no válido
    (-1, -1, -1, False),  # Lados negativos
    (1, 2, 3, False),  # No forma un triángulo
])
def test_comprobar_triangulo(a, b, c, resultado):
    assert comprobarTriangulo(a, b, c) == resultado