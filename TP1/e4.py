"""
4. Un comercio de electrodomésticos necesita para su línea de cajas un programa que 
le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan 
dos números enteros, correspondientes al total de la compra y al dinero recibido. 
Informar cuántos billetes de cada denominación deben ser entregados como vuelto, 
de tal forma que se minimice la cantidad de billetes. Considerar que existen billetes 
de $5000, $1000, $500, $200, $100, $50 y $10. Emitir un mensaje de error si el 
dinero recibido fuera insuficiente o si el cambio no pudiera entregarse debido a falta 
de billetes con denominaciones adecuadas. Ejemplo: Si la compra es de $3170 y se 
abona con $5000, el vuelto debe contener 1 billete de $1000, 1 billete de $500, 1 
billete de $200, 1 billete de $100 y 3 billetes de $10.
"""

billetes = {
    "5000": 0,
    "1000": 0,
    "500": 0,
    "200": 0,
    "100": 0,
    "50": 0,
    "10": 0,
}


def pedir_num(msj):
    while True:
        try:
            valor = int(input(msj))
            if valor > 0:
                return valor
            print("Por favor, ingrese un numero valido.")
        except ValueError:
            print("Por favor, ingrese un numero.")


def validar_plata(pago, total):
    return pago >= total


def calcular_billetes(vuelto):
    billetes["5000"] = vuelto // 5000
    resto = vuelto % 5000
    billetes["1000"] = resto // 1000
    resto = vuelto % 1000
    billetes["500"] = resto // 500
    resto = vuelto % 500
    billetes["200"] = resto // 200
    resto = vuelto % 200
    billetes["100"] = resto // 100
    resto = vuelto % 100
    billetes["50"] = resto // 50
    resto = vuelto % 50
    billetes["10"] = resto // 10
    resto = vuelto % 10
    return resto


def mostrar_billetes(cb):
    if cb > 0:
        print("faltan billetes con denominacion adecuada")
    for bille, cantidad in billetes.items():
        if cantidad > 0:
            print(f"Se usaron {cantidad} billetes de {bille}.")
        else:
            print(f"No se usaron billetes de {bille}.")


def main():
    total = pedir_num("Ingrese el total: ")
    pago = pedir_num("Ingrese la cantidad de dinero abonado: ")
    if validar_plata(pago, total):
        vuelto = pago - total
        cb = calcular_billetes(vuelto)
        mostrar_billetes(cb)
    else:
        print("Error, el monto del pago es menor al precio del producto.")


main()
