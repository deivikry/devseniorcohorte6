menu = """menu de restaurante, estan las siguientes opciones
1. hamburguesa     10000
2. salchipapa      12000
3. pizza           15000
4. helados         13000
5. perro caliente  12000
6. salir y pagar 
"""
print(menu)

total=0
amburguesa=0  
salchipapa =0
pizza =0
helados=0        
perro_caliente=0  
salir=0

cantidad_amburguer=0
cantidad_salchipapa=0
cantidad_pizza=0
cantidad_helados=0
cantidad_perro_caliente=0
opcion = 0

while opcion !=6:
    opcion = int(input("elige la opcion que desees"))
    if opcion ==1:
        print("has ordenado una hamburguesa")
        amburguesa+=10000
        cantidad_amburguer +=1
    elif opcion ==2:
        print("has ordenado una salchipapa")
        salchipapa+=12000
        cantidad_salchipapa +=1
    elif opcion ==3:
        print(" has ordenado una pizza")
        pizza+= 15000
        cantidad_pizza +=1
    elif opcion ==4:
        print("has elegido un helado ")
        helados+= 13000
        cantidad_helados +=1
    elif opcion ==5:
        print("has ordenado un perro caliente")
        perro_caliente+= 12000
        cantidad_perro_caliente += 1
    elif opcion == 6:
        print (f"""
               gracias por visitar el restaurante >:)
               
               total pagar en amburguesa {amburguesa} cantidad {cantidad_amburguer}
               total pagaren salchipapa {salchipapa} cantidad {cantidad_salchipapa}
               total pagar en pizza {pizza} cantidad {cantidad_pizza}
               total pagar en helados {helados} cantidad {cantidad_helados}
               toral pagar en perro calientes {perro_caliente} cantidad {cantidad_perro_caliente}
               """)
        break
    else:
        print("opcion invalidad por favor elija una opcion valida")
