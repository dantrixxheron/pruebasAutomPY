class Renta:
    def __init__(self):
        self.permitido = False
        self.tarifa_extra = False

renta = Renta()

def comprobar_renta(edad):
    if edad < 18 or edad > 80:
        renta.permitido = False
        renta.tarifa_extra = False
    elif 18 <= edad <= 24 or 65 < edad <= 80:
        renta.permitido = True
        renta.tarifa_extra = True
    else:
        renta.permitido = True
        renta.tarifa_extra = False
    return (renta.permitido, renta.tarifa_extra)
