def asigPrestamo(isCliente, deseaAbrirCuenta, isPrestamo, isPagos, ingresos):
    if not isCliente:
        if deseaAbrirCuenta:
            # nuevo cliente sin crédito vigente
            return ingresos * 6
        else:
            return "Crédito negado"

    # Si ya es cliente
    if isPrestamo:
        if isPagos:
            return ingresos * 3
        else:
            return "Crédito negado"
    else:
        return ingresos * 6
