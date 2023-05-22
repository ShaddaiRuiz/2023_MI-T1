import math
def main():
    altura = float(input('Escribe la altura de la casa: '))
    angulo = int(input('Escribe el angulo en grados: '))
    a = altura / math.sin(math.radians(angulo))
    print ('Largo de la escalera: ', round(a))

if __name__ == '__main__':
    main()
