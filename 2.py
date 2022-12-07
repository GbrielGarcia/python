import os

km_de_recorrido = float(input('Ingresa el valor de km de recorrido: '))
monto_a_pagar = 0
monto_fijo = 200
if km_de_recorrido <= 100:
    monto_a_pagar = monto_fijo
if km_de_recorrido > 100 and km_de_recorrido <= 500:
    monto_a_pagar = monto_fijo+(km_de_recorrido-300)*14
if km_de_recorrido > 100:
    monto_a_pagar = monto_fijo+700*15+(km_de_recorrido-100)*14
monto_del_impuesto = monto_a_pagar*0.12
print('Valor de monto a pagar: ' + repr(monto_a_pagar))
print('Valor de monto del impuesto: ' + repr(monto_del_impuesto))
print('Valor de monto fijo: ' + repr(monto_fijo))
print()
os.system('pause')
