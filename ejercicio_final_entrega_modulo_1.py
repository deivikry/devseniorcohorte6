



#recibimos parametros de notas y nombre de estudiante para calcular el promedio
def promedio(nota1,nota2,nota3,estudiantes_nombre):
    print("ahora vamos a calcular el promedio de las 3 notas: ")
    promedio= (nota1+nota2+nota3)/3
    print(f"el promedio de las notas del estudiante {estudiantes_nombre} es: {promedio:.2f}")
    return promedio#aprobado(estudiantes_nombre,promedio)
    
#funcion para determinar si el estudiante aprobo o no   
def aprobado(estudiantes_nombre,promedio):#parametros de nombre de estudiante y promedio para determinar si aprobo o no
    print("ahora vamos a determinar si el estudiante aprobo o no: ")

    if promedio >=4.0 and promedio <=5.0:
        print(f"el estudiante {estudiantes_nombre} aprobo con un promedio de {promedio:.2f}")
    elif promedio >=3.0 and promedio<=3.9:
        print(f"el estudiante {estudiantes_nombre} esta en recuperacion con un promedio de {promedio:.2f}")
    elif promedio <=2.9 and promedio >= 0:
        print(f"el estudiante {estudiantes_nombre} reprobo con un promedio de {promedio:.2f}")
    else:
        print("error al calcular revise las notas ingresadas,\n RECORDATORIO las notas van de 0.0 a 5.0")
    return """

            proceso de aprobacion terminado
"""
    


#registro usuario y valido edad
def registrar():
    estudiantes_nombre = input("ingrese el nombre del estudiante:")
    #esto es un "mienstras sea verdadero" ejecute todo lo que esta dentro del bucle
    while True:
        #solicito una edad para validar
        estudiante_edad = int(input("ingrese la edad del estudiante:"))
        #valido que la edad sea mayor a 0 o positiva
        if estudiante_edad <0:
            #imprimo un mensaje de error si la edad es negativa
            print ("error al ingresar la edad, ingresa una edad valida")
        else:
            #cuando la edad es valida osea mayor a 0 se ejecuta este bloque de codigo y se sale del bucle con el break
            print(f"""
                  
                  el estudiante {estudiantes_nombre} tiene una edad psitiva puedes continuar con el registro
                  
                  """)
            break
            
    print("""
          
          ahora necesito las 3 primeras notas del estudiante
          
          """)

    print("por favor escriba cada nota y luego presione enter")
    
    #validamos las notas ingresadas con un while para cada nota
    nota1= 0
    while True:
        nota1=float(input("ingrese la primera nota:"))
        if nota1 <0 or nota1 >5 :
            print("error al ingresar las notas, por favor ingrese notas validas entre 0.0 y 5.0")
        else:
            print("notas validas")
            break
    nota2= 0
    while True:
        nota2=float(input("ingrese la segunda nota:"))
        if nota2 <0 or nota2 >5 :
            print("error al ingresar las notas, por favor ingrese notas validas entre 0.0 y 5.0")
        else:
            print("notas validas")
            break
    nota3= 0
    while True:
        nota3=float(input("ingrese la tercera nota:"))
        if nota3 <0 or nota3 >5:
            print("error al ingresar las notas, por favor ingrese notas validas entre 0.0 y 5.0")
        else:
            print("notas validas")
            break
            #return de cada dato registrado para luego ser usado en el calculo del promedio y aprobacion
    return estudiante_edad,estudiantes_nombre,nota1,nota2,nota3


#menu de opciones

#contador de estudiantes registrados y acumulador para el promedio del grupo
estudiante_contador=0
clase=0
#bucle while para el menu
opcion=0
while opcion !=2:
    menu= print(""" 
            
          Bienvenido al menu de opciones para registrar estudiante y calcular s promedio
        
          
          1. REGISTRAR ESTUDIANTE Y CALCULAR PROMEDIO
          
          2. SALIR DEL PROGRAMA
          
          por favor elije alguna opcion
          
          =================================================
          """)
    opcion= int(input("escribe la opcion deseada:"))
    if opcion ==1:
        estudiante_registrado=registrar()
        print("""
              usuario registrado y notas tomadas
              """)
        estudiante_registrado_promedio=(promedio(estudiante_registrado[2],estudiante_registrado[3],estudiante_registrado[4],estudiante_registrado[1]))#poscion 2,3,4,1 del registro de estudiante
        estudiante_registrado_aprobado=(aprobado(estudiante_registrado[1],estudiante_registrado_promedio))
        clase=estudiante_registrado_promedio+clase
        estudiante_contador+=1
        #validacion de opcion cuando se va a salir del programa 
    elif opcion ==2:
        if estudiante_contador >0:
            print(f"el total de estudiantes registrados es de: {estudiante_contador}")
            print(f" el promedio del grupo es de: {clase/estudiante_contador:.2f}")
            print("gracias por usar el programa de registro y calculo de promedio")
        else:
            print("no se registraron estudiantes, gracias por usar el programa de registro y calculo de promedio")
     #cuando hay una opcion invalida diferente a 1 y 2   
    else:
        print("error al ingresar la opcion, por favor ingrese una opcion valida")
    
       
        