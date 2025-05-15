import pytest
from triangulos import comprobarTriangulo

def test_comprobarTriangulo():
    # Casos de prueba para triángulos equiláteros
    assert comprobarTriangulo(3, 3, 3) == "Equilátero"
    assert comprobarTriangulo(5, 5, 5) == "Equilátero"
    
    # Casos de prueba para triángulos isósceles
    assert comprobarTriangulo(3, 3, 4) == "Isósceles"
    assert comprobarTriangulo(4, 4, 5) == "Isósceles"
    
    # Casos de prueba para triángulos escalenos
    assert comprobarTriangulo(3, 4, 5) == "Escaleno"
    assert comprobarTriangulo(5, 6, 7) == "Escaleno"
    
    # Casos de prueba para triángulos no válidos
    assert comprobarTriangulo(1, 2, 3) == False
    assert comprobarTriangulo(0, 2, 2) == False
    assert comprobarTriangulo(-1, -1, -1) == False
