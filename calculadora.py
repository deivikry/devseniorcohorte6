def suma(a,b):
    sumar =a+b
    return sumar
    
def resta(a,b):
    restar = a-b
    return restar
    
def division(a,b):
    dividir= a/b
    return dividir
    
def multiplicacion(a,b):
    multiplicar = a*b
    return multiplicar
    
def potencia (a,b):
    potenciar = a**b
    return potenciar
    
def divicion_entera(a,b):
    divEntera= a//b
    return divEntera

def modulo(a,b):
    modular = a%b
    return modular
    
print("")
print("=================================================================================")

print('bienvenido a la calculador de python')
print("")
print("=================================================================================")
print("")
print("")

print('lo primero que necesito son 2 valores \n con los cuales quieras hacer alguna operacion')

print("")
print("")

n1=int(input('igrese el primer numero: '))
n2=int(input('ingrese el segundo numero: '))
print("")
print("")
print("================================================================================")
print("")


print("ahora elije una opcion del menu ")

lista = ("""
1. Suma
2. Resta
3. Multiplicacion
4. Division
5. Division entera
6. Potencia
7. Modulo
8. Salir      
      """)



opcion=0
while opcion !=8:
        print("==========================================================================================")
        print("")
        print(lista)
        opcion = int(input('que opcion eliges?: '))
        match opcion:
            case 1:
                print('el resultado de la suma entre los 2 numero que digitaste es de ',suma(n1,n2))
            case 2:
                print('el resultado de la resta entre los 2 numero que digitaste es de ',resta(n1,n2))
            case 3:
                print('el resultado de la multiplicacion entre los 2 numero que digitaste es de ',multiplicacion(n1,n2))
            case 4:
                print('el resultado de la division entre los 2 numero que digitaste es de ',division(n1,n2))
                if n2 ==0:
                    print('no se puede hacer diviciones entre 0')
            case 5:
                print('el resultado de la division entera entre los 2 numero que digitaste es de ',divicion_entera(n1,n2))
                if n2 ==0:
                    print('no se puede hacer diviciones entre 0')
            case 6:
                print('el resultado de la potencia entre los 2 numero que digitaste es de ',potencia(n1,n2))
            case 7:
                print('el resultado del modulo entre los 2 numero que digitaste es de ',modulo(n1,n2))
            case 8:
                print('GRACIAS POR USAR LA CALCULADORA')
            case _:
                print('ingrese una opcion valida')
        