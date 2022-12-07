import sys

numero_alumnos = float(input('Ingrese numero de alumnos: '))
sys.stdout.write('\t')

if numero_alumnos >= 70:
    total = numero_alumnos * 55
    coste = total / 3000
if numero_alumnos > 50 and numero_alumnos <= 69:
    total = numero_alumnos * 65
    coste = total / 3000
if numero_alumnos > 30 and numero_alumnos <= 49:
    total = numero_alumnos * 85
    coste = total / 3000

if numero_alumnos <= 30:
    print('Precio del autobús es de 3000')
    sys.exit()

print('El pago de la agencia es de: ' + repr(total))
