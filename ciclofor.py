
tabla = int(input("Ingrese la tabla de multiplicar que desea: "))
for x in range (1,11):
    print (f"{tabla}x {x} = {x*tabla}")

print ("esta es tu tabla de multiplicar")

print("====================================")

print ("vamos a imprimir todas las tablas del 1 al 10")


for t in range (1,11):
    for x in range (1,11):
        print(f"{t} x {x} = {x*t}")
    print (f"tabla del {t}")
    
print("========================================================")

print ("ahora vamos a intentar a usar el siclo while")


tablaMultiplicar=1
valorMultiplicar=1
while tablaMultiplicar <=10:
    while valorMultiplicar <=10:
        print(f"{tablaMultiplicar} x {valorMultiplicar} = {tablaMultiplicar*valorMultiplicar}")
        valorMultiplicar +=1

    print (f" tabla de multiplicar {tablaMultiplicar}")
    tablaMultiplicar +=1
    valorMultiplicar=1
    