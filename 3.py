import sys

embarque_en_kilos = float(input('ingrese los Kilogramos de uva entregada: '))
precio_inicial = float(input('Ingresa el valor de precio inicial: '))
tamano = float(input('Ingresa el valor de tamano: '))
precio_por_kilo = precio_inicial
print('Selecciona el valor de tipo de uva.')
print('\t1.- A')
print('\t2.- B')
sys.stdout.write('\t')
tipo_de_uva = 0
while tipo_de_uva < 1 or tipo_de_uva > 2:
    tipo_de_uva = int(input(': '))
    if tipo_de_uva < 1 or tipo_de_uva > 2:
        sys.stdout.write('Valor incorrecto. Ingr\u00E9salo nuevamente.')
if tipo_de_uva == 1 and tamano == 1:
    precio_por_kilo = precio_por_kilo + 0.2
if tipo_de_uva == 1 and tamano == 2:
    precio_por_kilo = precio_por_kilo + 0.3
if tipo_de_uva == 2 and tamano == 1:
    precio_por_kilo = precio_por_kilo - 0.3
if tipo_de_uva == 2 and tamano == 2:
    precio_por_kilo = precio_por_kilo - 0.5
pago_al_productor = embarque_en_kilos*precio_por_kilo
print('Valor de pago al productor: ' + repr(pago_al_productor))
print('Valor de precio por kilo: ' + repr(precio_por_kilo))
print()