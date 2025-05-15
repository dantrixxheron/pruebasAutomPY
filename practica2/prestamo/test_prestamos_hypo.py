import pytest
import hypothesis.strategies as st
from hypothesis import given, settings, Verbosity
from prestamos import asigPrestamo

@settings(max_examples=100, verbosity=Verbosity.verbose)
@given(st.booleans(), st.booleans(), st.booleans(), st.booleans(), st.integers(min_value=0, max_value=10000))
def test_asig_prestamo(isCliente, deseaAbrirCuenta, isPrestamo, isPagos, ingresos):
    # Test for valid cases
    if not isCliente:
        if deseaAbrirCuenta:
            # cliente sin crédito vigente
            assert asigPrestamo(isCliente, deseaAbrirCuenta, isPrestamo, isPagos, ingresos) == ingresos * 6
        else:
            assert asigPrestamo(isCliente, deseaAbrirCuenta, isPrestamo, isPagos, ingresos) == "Crédito negado"
    else:
        # Si ya es cliente
        if isPrestamo:
            if isPagos:
                assert asigPrestamo(isCliente, deseaAbrirCuenta, isPrestamo, isPagos, ingresos) == ingresos * 3
            else:
                assert asigPrestamo(isCliente, deseaAbrirCuenta, isPrestamo, isPagos, ingresos) == "Crédito negado"
        else:
            assert asigPrestamo(isCliente, deseaAbrirCuenta, isPrestamo, isPagos, ingresos) == ingresos * 6