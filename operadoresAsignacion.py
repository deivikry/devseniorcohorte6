# operadores de asignación
a = 5
a += 3
print("a += 3:", a)
a -= 3
print("a -= 3:", a)
a *= 3
print("a *= 3:", a)
a /= 3
print("a /= 3:", a)
#la división entera y el módulo solo funcionan con números enteros, si intentamos usarlos con números decimales, obtendremos un error.
a //= 3
print("a //= 3:", a)
#el operador de módulo asigna el resto de la división de a entre 3 a a, es decir, a = a % 3
a %= 3
print("a %= 3:", a)
#el operador de exponente asigna a a el resultado de elevar a a la potencia de 3, es decir, a = a ** 3
a **= 3
print("a **= 3:", a)