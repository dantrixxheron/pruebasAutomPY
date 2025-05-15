def comprobarTriangulo(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a+b<=c or a+c<=b or b+c<=a:
        return False
    if a == b and b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"