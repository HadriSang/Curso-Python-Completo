def decuentos():
    mini=100
    valdesc=0
    desc=0
    consumo = float(input('Ingrese el total del consumo: '))
    if consumo <= mini:
        valdesc +=10
        desc= consumo * valdesc / 100
    elif consumo >100 and consumo < 200:
        valdesc += 20
        desc= consumo * valdesc / 100
    elif consumo >200:
        valdesc += 30
        desc= consumo * valdesc / 100
       
    impuesto= consumo * 19 / 100
    totaldesc= consumo - desc
    total = impuesto + totaldesc
    print('-'*50)
    print('='*15 ,'FACTURA VENTA', '='*15)
    print('-'*50)
    print(f'El descuento es del {valdesc}% para un total de: {desc}')
    print('-'*50)
    print(f'El Valor con descuento es {totaldesc}')
    print('-'*50)
    print(f'El valor del impuesto es: {impuesto}')
    print('-'*50)
    print(f'El total a pagar es: {total}')

decuentos()