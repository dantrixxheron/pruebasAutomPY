import pytest
from descuentos import comprobarDescuento

@pytest.mark.parametrize(("cantCompra", "isNewClient", "isVIPClient", "resultado"), [
    (100, True, False, 20),  # Compra mayor o igual a 100 (+15) y nuevo cliente (+5)
    (150, False, True, 25),  # Compra mayor a 100 (+15) y cliente VIP (+10)
    (50, False, False, 0),   # Compra menor a 100 y no es nuevo ni VIP (0)
    (0, False, False, 0),    # Compra de 0 (no se aplica descuento)
    (-50, True, False, 0),   # Compra negativa (no se aplica descuento)
])
def test_comprobar_descuento(cantCompra, isNewClient, isVIPClient, resultado):
    assert comprobarDescuento(cantCompra, isNewClient, isVIPClient) == resultado