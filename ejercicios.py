print("======================================================")
edad1= 20
edad2= 30

nombre1= "Juan"
nombre2= "Maria"

print("la edad de ", nombre1, "es:", edad1, "y la edad de ", nombre2, "es:", edad2+edad1)
print(f"La edad de {nombre1} es: {edad1} y la edad de {nombre2} es: {edad2}")


"""escriba un programa que calcule el area de un circulo"""

print("======================================================")


print("Calculo del area de un circulo")
print("para calcular este area necesito el radio del circulo")
radio = float(input("ingrese el valor del radio:"))
PI= 3.1416
areaCirculo= PI * radio **2
print(f"si el radio es: {radio}")
print(f"el area del circulo es : {areaCirculo:.2f}") #:.2f es para mostrar solo 2 decimales

print("...___..")
print("../...\..")
print("..(....)..")
print("..\___/..")
print("")



print("======================================================")

print("Calculo del area de un triangulo")

print( "para calacular este area necesitamos la base y la altura")
base= float(input("ingrese el valor de la base:"))
altura= float(input ("ingrese el valor de la altura:"))
areaTriangulo= (base * altura)/2
print(f"el area del triangulo es: {areaTriangulo:.2f}")

print("==============================================================")


print ("aqui podras saber cuanto pagarle a tus empleados por sus horas de trabajo")
print ("primero necesitamos saber las horas trabajadas y cuanto es que pagas por hora")

horasTrabajadas= int(input("digite las horas trabajadas por su empleado: "))
sueldoHora= float(input("digita cuanto pagas la hora a tu empleado:"))

pagoTotal= horasTrabajadas*sueldoHora

print (f"el pago total para su empleado que trabajo {horasTrabajadas} horas, es de {pagoTotal} pesos")

