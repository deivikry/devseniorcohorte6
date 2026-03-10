print("==============================================================")


print ("aqui podras saber cuanto pagarle a tus empleados por sus horas de trabajo")
print("")
print ("primero necesitamos saber las horas trabajadas y cuanto es que pagas por hora")
sueldoHora= int(input("digita cuanto pagas la hora a tu empleado:"))



print("=========================================================================")

#primer empleado 
print("para el primer empleado: ")
horasTrabajadas= int(input("digite las horas trabajadas por su empleado: "))
pagoTotal_empleado1= horasTrabajadas*sueldoHora

print (f"el pago total para su empleado que trabajo {horasTrabajadas} horas, es de {pagoTotal_empleado1} pesos")


print("=========================================================================")


#segundo empleado 
print("para el segundo empleado: ")
horasTrabajadas2= int(input("digite las horas trabajadas por su empleado: "))
pagoTotal_empleado2= horasTrabajadas2*sueldoHora

print (f"el pago total para su segundo empleado que trabajo {horasTrabajadas} horas, es de {pagoTotal_empleado2} pesos")


print("=========================================================================")

#tercer  empleado 
print("para el tercer empleado: ")
horasTrabajadas3= int(input("digite las horas trabajadas por su empleado: "))
pagoTotal_empleado3= horasTrabajadas3*sueldoHora


print (f"el pago total para su tercer empleado que trabajo {horasTrabajadas} horas, es de {pagoTotal_empleado3} pesos")

pago_total_empleados= pagoTotal_empleado3+pagoTotal_empleado1+pagoTotal_empleado2

print(f"el pago total para sus 3 empleados es de {pago_total_empleados}")
