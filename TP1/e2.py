"""
2. Desarrollar una función que reciba tres números enteros positivos correspondientes
al día, mes, año de una fecha y verifique si corresponden a una fecha válida. Debe
tenerse en cuenta la cantidad de días de cada mes, incluyendo los años bisiestos(bisiesto = febrero con 29 dias).
Devolver True o False según la fecha sea correcta o no. Realizar también un
programa para verificar el comportamiento de la función.
year % 4 == 0 and year % 100 != 0 or year % 400 == 0
"""


meses = {
    "enero": 31,
    "febrero": 28,
    "marzo": 31,
    "abril": 30,
    "mayo": 31,
    "junio": 30,
    "julio": 31,
    "agosto": 31,
    "septiembre": 30,
    "octubre": 31,
    "noviembre": 30,
    "dicembre": 31,
}

def pedir_fecha() -> list[int]:
    lista_fecha= []
    while len(lista_fecha) < 3:
        try:
            anio = int(input("ingrese un dia: "))
            mes = int(input("ingrese un dia: "))
            dia = int(input("ingrese un dia: "))
        except ValueError:
            print("se ingreso un valor erroneo, porfavor vuelva a intentar")
    return dia, mes, anio

def validar_bisiesto(anio: int)-> bool:
    valido = False
    if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
        valido= True
    return valido


#.update


def main():
    dia, mes, anio, lista_fecha = pedir_fecha()
    vb= validar_bisiesto(anio)

main()