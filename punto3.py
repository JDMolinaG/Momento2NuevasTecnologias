from datetime import datetime


valorDiaParqueadero = 10000
calcularValor = 0
celdaDisponible = [1, 2]
celdasOcupadas =[]


def calcularFecha(fechaInicial, fechaFinal):
    fecha_inicial = datetime.strptime(fechaInicial, '%d/%m/%Y')
    fecha_final = datetime.strptime(fechaFinal, '%d/%m/%Y')
    return (fecha_final-fecha_inicial).days

centinela = 'si'
while centinela == 'si'  :
    
    accionVehiculo = input('1-si desea ingresar un vehiculo ingrese (entrar), si desea salir ingrese (salir): ')
    # if len(celdaDisponible)==0:
    #     print('Lo lamento no hay mas celdas disponibles')
    while accionVehiculo == 'entrar'  and len(celdaDisponible)>0 :
        print('---PROCESO PARA ENTRAR---')
        print(f'Celdas disponibles {celdaDisponible}')
        placa = input('Ingrese la placa del vehiculo: ')
        celda = int(input('Ingrese la celda del 1 al 5: '))
        disponible = celda in celdaDisponible
        if disponible == True:
            celdaDisponible.remove(celda)
            celdasOcupadas.append(celda)
            print(f'¡EXITO! Su vehiculo ya se ingreso a la celda {celda}')
            
        else:
            print('¡FALLO! La celda no esta disponible')
        accionVehiculo = input('2-si desea ingresar un vehiculo ingrese (entrar), si desea salir ingrese (salir): ')
    print('¡FALLO! Lo siento todas las celdas estan llenas')
    print('---PROCESO PARA SALIR---')
    print(f'Celdas donde puede estar su vehiculo {celdasOcupadas}')
    celda = int(input('Ingrese la celda donde guardo su vehiculo 1 al 5: '))
    disponible = celda in celdasOcupadas
    if disponible == True:
        celdaDisponible.append(celda)
        celdasOcupadas.remove(celda)
        fechaInicial = input('Ingrese fecha inicial dia/mes/año: ')
        fechaFinal = input('Ingrese fecha final dia/mes/año: ')
        calcularValor = (calcularFecha(fechaInicial, fechaFinal) * valorDiaParqueadero)
        print(f'El vehiculo duro {calcularFecha(fechaInicial,fechaFinal)} dias en el parquedero')
        print(f'El total a pagar es {calcularValor}')
        print(f'Ya puede retirar su vehiculo de la celda {celda}')
    else:
        print('Su vehiculo no esta en esta celda')
    
    centinela = input('Desea seguir? si/no: ')

