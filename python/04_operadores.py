#operadores
"""
operadores aritméticos
+ suma
- resta
* multiplicación
/ división
// división entera
% módulo
** potencia
"""
valor1 = 10
valor2 = 3
resultado = valor1 + valor2
resta = valor1 - valor2
multiplicacion = valor1 * valor2
division = valor1 / valor2
division_entera = valor1 // valor2
modulo = valor1 % valor2
potencia = valor1 ** valor2

print("Suma:", resultado)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("División entera:", division_entera)
print("Módulo:", modulo)
print("Potencia:", potencia)

print("tabla de multiplicar del 5")
print("5 x 1 =", 5 * 1)
print("5 x 2 =", 5 * 2)
print("5 x 3 =", 5 * 3) 
print("5 x 4 =", 5 * 4)
print("5 x 5 =", 5 * 5)
print("5 x 6 =", 5 * 6)
print("5 x 7 =", 5 * 7)
print("5 x 8 =", 5 * 8)
print("5 x 9 =", 5 * 9)
print("5 x 10 =", 5 * 10)

"""
operadores de comparación
== igual a
!= diferente de
> mayor que           
< menor que
>= mayor o igual que
<= menor o igual que
"""
print("area del tringulo con base 5 y altura 10", (5 * 10) / 2)
velocidad_anakin = 950
valocidad_luke = 1000
print("¿Anakin es más rápido que Luke?", velocidad_anakin > valocidad_luke)
print("¿Anakin es más lento que Luke?", velocidad_anakin < valocidad_luke)
print("¿Anakin es igual de rápido que Luke?", velocidad_anakin == valocidad_luke)
print("¿Anakin es diferente de Luke?", velocidad_anakin != valocidad_luke)
print("¿Anakin es más rápido o igual que Luke?", velocidad_anakin >= valocidad_luke)
print("¿Anakin es más lento o igual que Luke?", velocidad_anakin <= valocidad_luke)

resultado = velocidad_anakin > valocidad_luke
print("Resultado de la comparación:", resultado)
print("Tipo de resultado:", type(resultado))

#operadores lógicos
"""
and (y)
or (o)
not (no)
"""

motor_encendido = True
nave_en_movimiento = False

print("¿La nave puede despegar?", motor_encendido and nave_en_movimiento)
print("¿La nave puede despegar?", motor_encendido or nave_en_movimiento)
print("¿La nave puede despegar?", not motor_encendido)

cantidad_motores = 2
cantidad_alas = 4
combustible= 50

print("¿La nave puede despegar?")
print(cantidad_motores >= 2 and cantidad_alas >= 4 and combustible > 0)

#operadores de asignación
"""
= asignación
+= suma y asigna
-= resta y asigna
*= multiplica y asigna
/= divide y asigna
//= divide entera y asigna
%= módulo y asigna
**= potencia y asigna
"""
velocidad = 100
print("velocidad inicial", velocidad)
velocidad += 50
print("velocidad después de acelerar", velocidad)
velocidad -= 30
print("velocidad después de frenar", velocidad)
velocidad **= 2
print("velocidad después de potenciar", velocidad)
velocidad //= 3
print("velocidad después de dividir entera", velocidad)
velocidad %= 7
print("velocidad después de módulo", velocidad)
velocidad *= 2
print("velocidad después de multiplicar", velocidad)
velocidad /= 4
print("velocidad después de dividir", velocidad)
#precencia de operadores
"""
1. ()
2. ** (potencia)
3. * / // % (multiplicación, división, división entera, módulo)
4. + - suma, resta
"""
resultado = 10 + 5 * 2
print("Resultado de 10 + 5 * 2:", resultado)
resultado = (10 + 5) * 2
print("Resultado de (10 + 5) * 2:", resultado)
resultado = 10 + 5 ** 2
print("Resultado de 10 + 5 ** 2:", resultado)
