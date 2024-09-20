"""
Desarrollar una función que reciba tres números enteros positivos y devuelva el
mayor de los tres, sólo si éste es único (es decir el mayor estricto). Devolver -1 en
caso de no haber ninguno. No utilizar operadores lógicos (and, or, not). Desarrollar
también un programa para ingresar los tres valores, invocar a la función y mostrar
el máximo hallado, o un mensaje informativo si éste no existe.
"""


def cargar_num():
    lista_numeros = []
    while len(lista_numeros) < 3:
        try:
            num = int(input("ingrese un valor: "))
            if num > 0:
                lista_numeros.append(num)
        except ValueError:
            print("se deben ingresar unicamente numeros enteros")
    return lista_numeros


def encontrar_mayor(cn):
    maxi = max(cn)
    return maxi


def validar_maximo(cn, en):
    valido = True
    contador = cn.count(en)
    if contador >= 2:
        valido = False
    return valido


def mostrar_numero(vm, en):
    if vm == False:
        print("-1")
    else:
        print(f"El mayor de los numeros ingresados es: {en}")


def main():
    cn = cargar_num()
    en = encontrar_mayor(cn)
    vm = validar_maximo(cn, en)
    mostrar_numero(vm, en)


main()
