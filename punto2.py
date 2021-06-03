def subTotal(precio,cantidad):
    return precio*cantidad

cesta ={}
totalProductos = 1

centinela ='si'
while centinela == 'si' and totalProductos <=2:
    clave=input('introduzca el producto: ')
    valor=int(input('Ingrese el valor de '+clave+ ': '))
    talla = input('Ingrese la talla: ')
    cesta[clave] = valor
    centinela = input('desea continuar? ')
    totalProductos = totalProductos +1
if len(cesta)>=2:
    print('No puede agregar mas de 10 productos a la cesta')
total = 0
totacant = 0
for producto,precio in cesta.items():
    cantidad = int(input('ingrese la cantidad de '+producto+': '))
    totacant = totacant+cantidad
    total +=subTotal(precio,cantidad)
if totacant<=10:
    print('El total es: ',total)
else:
    print('No se pudo calcular el valor a pagar debido que pasaste de 10 productos')  



      

    