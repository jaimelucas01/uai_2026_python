def registrar_usuario():
    nombre = input("Ingrese su nombre: ")
    return nombre

def depositar(saldo, historial):
    print("Función de depósito simulada.")
    return saldo + 100, historial

def extraer(saldo, historial):
    print("Función de extracción simulada.")
    return saldo - 50, historial