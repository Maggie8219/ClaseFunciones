import os, time
opcion = ''
opcion_lista = []
while opcion != '3':
    os.system("clear")
    print('Menú de opciones')
    print('1. Cálculo de área de triángulo')
    print('2. Cálculo de área de círculo')
    print('3. Salir')

    opcion = input('Seleccione una opción: ')

    def area_triangulo():
        os.system("clear")
        base = input('Ingrese la base: ')
        altura = input('Ingrese la altura: ')
        resultado = (float(base) * float(altura)) / 2
        print(resultado)
        opcion_lista.append(resultado)
        time.sleep(2)
        return resultado

    def area_circulo():
        os.system("clear")
        radio = input("Ingrese el radio: ")
        PI = 3.141592
        resultado = PI * (float(radio)**2)
        print(resultado)
        opcion_lista.append(resultado)
        time.sleep(2)
        return resultado

    if opcion == '1':
        area_triangulo()
    elif opcion == '2':
        area_circulo()
    elif opcion == '3':
        print('--------------------------')
        print('El resultado de triangulo: ', opcion_lista[0])
        print('El resultado de circulo: ', opcion_lista[1])
        print('--------------------------')
        print('Gracias por tu visita')
    else:
        print('No existe la opción seleccionada')
        time.sleep(2)