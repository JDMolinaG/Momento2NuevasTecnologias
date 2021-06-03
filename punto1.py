
numeroPersonas = 1
lista = []


def mostrarLista(lista):
    print('------Informacion de la lista------')
    print(f'Identificacion: {lista[0]}')
    print(f'Nombre: {lista[1]}')
    print(f'Salario: {lista[2]}')
    print(f'Comision: {lista[3]}')
    print(f'Bonificaion: {lista[4]}')

def buscarDato(dato):
    print(lista[dato])

while numeroPersonas <= 5:
    print('Persona numero ' + str(numeroPersonas))
    indentificacion = input('Ingrese su numero de identificacion: ')
    lista.append(indentificacion)
    nombre = input('Ingrese su nombre: ')
    lista.append(nombre)
    salario = int(input('Ingrese su salario: '))
    while salario < 900000:
        print('El salario debe ser mayor a 900000')
        salario = int(input('Ingrese su salario: '))
    lista.append(salario)
    comision = int(input('Ingrese su comision: '))
    while comision <= 0:
        print('La comision debe de ser mayor de 0')
        comision = int(input('Ingrese su comision: '))
    lista.append(comision)
    bonificaciones = int(input('Ingrese las bonificaciones: '))
    while bonificaciones <= 0:
        print('La bonificacion debe de ser mayor de 0')
        bonificaciones = int(input('Ingrese las bonificaciones: '))
    lista.append(bonificaciones)
    mostrarLista(lista)
    buscar = input('Quiere buscar un dato en la lista? si/no ')
    while buscar == 'si':
        print('Ingresa el numero que quiera buscar: ')
        datoBuscar = int(input('0-Identificacion 1-Nombre 2-salario 3-comision 4-bonificacion '))
        buscarDato(datoBuscar)
        buscar = input('Quiere buscar un dato en la lista? si/no ')
    lista.clear()
    numeroPersonas = numeroPersonas + 1

