"""
6. Desarrollar una función que reciba como parámetros dos números enteros positivos 
y devuelva como valor de retorno el número que resulte de concatenar ambos 
parámetros. Por ejemplo, si recibe 1234 y 567 debe devolver 1234567. No se permite utilizar facilidades de Python no vistas en clase.
"""


def pedir_num(msj):
    while True:
        try:
            num = int(input(msj))
            if num > 0:
                return num
            print("Se debe ingresar un numero entero y mayor a cero.")
        except ValueError:
            print("Se debe ingresar un numero.")


def convertir_numero(a, b):
    return str(a) + str(b)


def main():
    a = pedir_num("Ingrese el primer numero: ")
    b = pedir_num("Ingrese el segundo numero: ")
    cn = convertir_numero(a, b)
    print(cn)


main()
