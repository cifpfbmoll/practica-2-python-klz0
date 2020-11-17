#Práctica 2 - Introducción a Python
#P2E4_sgonzalez
#Diagrama para calcular el mayor de dos números  

print ("Vamos a calcular el mayor de dos números")
a=int(input("Introduce el primer número "))
b=int(input("Introduce el segundo número ")) 
if (a>b):
    print (a, "es el número mayor")
elif(a==b):
    print (a, "y", b, "son iguales.")
else:
    print (b, "es mayor que ", a)    



