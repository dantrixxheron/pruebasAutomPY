def comprobarDescuento(cantCompra, isNewClient, isVIPClient):
    descuento = 0
    if(cantCompra<=0): return 0;
    if(cantCompra>=100): descuento+=15;
    if(isNewClient): descuento+=5;
    elif(isVIPClient): descuento+=10;
    return descuento;  