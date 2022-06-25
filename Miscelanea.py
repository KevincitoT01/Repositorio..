# OPERADORES

# Operador 1
print("Ejerecicio 1: calcular el area del triangulo")
base = float(input("ingrese la base: \n"))
altura = float (input("ingrese la altura: \n"))
area = base * altura / 2
print("resultado: "+ str(area))
  
# Operador 2 
print("Ejercicio 2: sumar dos digitos")
n1 = float(input("agregar un número : \n"))
n2 = float(input("agregar un número : \n"))
suma = n1 +n2 
print("resultado: " + str(suma))

# Operador 3

print("Ejercicio 3 : número al cuadrado")
n1 = float(input("ingresa numero: \n"))
nac = n1 * n1
print ("resultado: " +str(nac))
  
# Operador 4
print("Ejercicio 4:convertir moneda de Euro a Dolar")
Euro = float(input("valor de Euro: \n"))
convertir = Euro / 1.05
print("Cantidad de Dolar: " +str(convertir))
  
 # Operador 5

print("Lado de un cuadrado y valor del area:")
Lado = float(input("ingrese el valor del lado: \n "))
area = Lado * Lado 
perimetro = Lado + Lado + Lado + Lado
print("resultado: " + str(area))
print("resultado del perimetro: "+ str(perimetro))
  
 # Operador 6

print("ejercicio 6: Area y volumen de un cilindro")
print("poner el radio y altura:")
radio = float(input("valor del radio: \n"))
altura = float(input("valor de la altura: \n"))
    
# Operador 7

print("area y longitud de un circulo")
print("radio del circulo:")
n1 = int(input())
print("longitud del circulo")
longitud = (2 * n1) * (3.1416)
print(longitud)
print("el area es")
n2 = (3.1416 * n1) *2
print(n2)
    
 # Operador 8

print("Promedio de 3 números")
print("ingresar los números:")
n1 = int(input())
n2 = int(input())
n3 = int(input())
promedio = (n1 + n2 +n3) /3
print("El promedio es:")
print(promedio)

# CONDICIONALES 
  
 #Condicional 1
print("Pedir un número para ver si es positivo o negativo:")
n = int(input())
if (n > 0):
 print("el número es positivo ")
elif (n < 0):
  print("el número es negativo")
else:
  print("solo es el 0 NMMS")


 #Condicional 2
print("Cuál es el mayor y cuál el menor:")
n1 = int(input("Numero 1:"))
n2 = int(input("Numero 2:"))
if n1 == n2:
  print("Los 2 numeros son iguales")
elif n1 > n2:
  print(f"El numero {n1} es mayor que {n2}")
else:
  print(f"El numero {n2} es mayor que {n1}")


# Condicional 3
print("El mayor de 3 números:\n")

n1 = float(input("\nPrimer número: "))

n2 = float(input("\nSegundo número: "))

n3 = float(input("\nTercer número: "))

if n2 < n1 > n3:
  print("\nEl número mayor es el primero", n1)
elif n1 < n2 > n3:
  print("\nEl número mayor es el segundo", n2)
elif n1 < n3 > n2:
  print("\nEl número mayor es el tercero", n3)


# Condicional 4
print("Sumar o Restar")
n1 = int(input("ingrese el primer numero:"))
n2 = int(input("ingrese el segundo numero:"))
if n1 < n2:
  print(f"el numero mayor es: {n2}")
  result = n1 + n2
  print("Resultado de la suma")
  print(result)
  if n2 < n1:
    print(f"el numero menor es:{n1}")
    result = n1 - n2
    print("Resultado de la resta:")
    print(result)

# Condicional 5
print("cosiente a o b:")
A = float(input("ingrese el dividendo:"))
B = float(input("ingrese el divisor:"))
if A == 0 or B == 0:
  print("No se puede dividir")
else:
  Cociente = A / B
  print(Cociente)


# Condicional 6
print("Sumar o mutiplicar:")
a = float(input("Ingrese numero a: "))
b = float(input("Ingrese numero b: "))
if 0 > a or a:
  c = a + a
  print(c)
else:
  c = b * b
  print(c)

      
 # Condicional 7
print("Año bisiesto o no\n ")
año = int(input("Año:"))
if (año % 4 == 0 
and (año % 100 !=0)) or (año % 400 == 0):
  print("El año", str(año) + " es bisiesto")
else:
  print(" el año", str(año) + " no es bisiesto")


# CICLOS
  
# Ciclo 1
print("Multiplos del 3 asta el 100 \n ")
num = 100
odd_number = [i for i in range(num)if i % 2!= 0]
print("Los multiplos son: \n")
print(odd_number)

# Ciclo 2
print("Números impares del 0 al 100 \n")
num = int(input())
odd_numbers = [i for i in range(num) if i % 2 != 0]
{num}
print(odd_numbers)

# Ciclo 3
print("Numeros pares asta el 100: \n")
num = int(input())
odd_numbers = [i for i in range(num) if i % 2 != 1]
{num}
print(odd_numbers)

# Ciclo 4
print("numeros cuadrados de 1 al 30")
for n1 in range(1, 30):
  print(n1**2, end=",")

# Ciclo 5
print("numeros de los cuadrados sumados")
for i in range(0, 100):
  cuadrado = (i+1)*(i+1)
  suma = 0
  suma = suma + cuadrado
  print(i+1,"=",cuadrado)
print(suma)

# Ciclo 6
print("Numeros comprendidos")
n1 = int(input("numero 1: \n"))
n2 = int(input("numeromayor al anterior: \n"))
print("los valores que se encuentran entre los numeros digitados son: \n")
for i in range(n1,n2):
  i = i
  print(i)
  
# Ciclo 7
print("sumar los numeros digitados: \n")
valor = 1
total = 0
while valor != 0 :
  valor = int(input("Escribe los numeros que desea sumar:"))
  if valor == 0 :
    valor = 0
  else :
    total = total + valor
  print(total)

