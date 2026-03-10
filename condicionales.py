#CASE una nueva condicional de flujode control, es una nueva forma de escribir condicionales, es mas facil de leer y entender,
# ademas de que es mas eficiente que el if-elif-else

"""
print("punto CASE animal")
animal = input("seleccione entre terian, perro, gato o pez: ")
match  animal:
    #aqui se pueden agregar mas casos, es decir, mas animales y sus respectivos sonidos
    case "gato":
        print("el gato hace miau \n")
    case "pez":
        print("el pez hace blub \n")
    case "perro":
        print("el perro hace gwau\n")
    case "terian":
        print("el terian es raro\n")
    case _:
        print("ingrese una opcion valida\n")
"""

print ("aqui vamos a calcular la tabla de multiplica que elijas")

#proponemos una variable para la tabla de multiplicar, y un ciclo while para imprimir la tabla de multiplicar,
# el ciclo se repetira hasta que i sea mayor a 10, y en cada iteracion se imprimira la tabla de multiplicar
# correspondiente a la variable tabla, y se incrementara i en 1

tabla= int(input("escirbe la tabla que desees: "))
i = 1
while i <=10:
    print (f"{tabla}x {i} = {i*tabla}")
    #el valor de "tabla" se multiplica por "i" que inicialmente vale 1, y se incrementa en 1 en cada iteracion (hasta que i sea mayor a 10)
    i+=1
print("ya termino el ciclo")