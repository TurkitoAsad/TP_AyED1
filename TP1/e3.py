"""
3. Una persona desea llevar el control de los gastos realizados al viajar en el subterráneo dentro de un mes. Sabiendo que dicho medio de transporte utiliza un
esquema de tarifas decrecientes (detalladas en la tabla de abajo) se solicita desarrollar una función que reciba como parámetro la cantidad de viajes realizados en un 
determinado mes y devuelva el total gastado en viajes. Realizar también un programa para verificar el comportamiento de la función.

"""


def pedir_num(msj: str) -> int:
    while True:
        try:
            viajes = int(input(msj))
            if viajes > 0:
                return viajes
            print("Por favor, ingresar un numero positivo y mayor a cero.")
        except ValueError:
            print("Solo se aceptan valores numericos.")


def descuentos(c_viajes: int, total: int) -> float:
    if c_viajes <= 20:
        return -1
    elif c_viajes >= 21 and c_viajes <= 30:
        return (total * 20) / 100
    elif c_viajes >= 31 and c_viajes <= 40:
        return (total * 30) / 100
    else:
        return (total * 40) / 100


def imprimir_descuentos(descuen: float, total: int) -> None:
    if descuen == -1:
        print("Averiguar en internet el valor actualizado.")
    else:
        print(f"El gasto total del mes es de ${total - descuen}.")


def main() -> None:
    c_viajes = pedir_num("Ingrese la cantidad de viajes del mes: ")
    p_viajes = pedir_num("Ingrese el precio de un viaje: ")
    total = c_viajes * p_viajes
    descuen = descuentos(c_viajes, total)
    imprimir_descuentos(descuen, total)


main()
