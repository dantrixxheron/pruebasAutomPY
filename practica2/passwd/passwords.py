def validarPwd(pwd):
    #validar largo de la contraseña entre 8 y 16 caracteres
    if len(pwd) < 8 or len(pwd) > 16:
        return False
    #validar que contenga al menos un número, una letra y un símbolo
    if not any(char.isdigit() for char in pwd):
        return False
    #validar que contenga al menos una letra mayúscula
    if not any(char.isupper() for char in pwd):
        return False
    #validar que contenga al menos un símbolo
    if not any(char in "@#$%&*" for char in pwd):
        return False
    return True
