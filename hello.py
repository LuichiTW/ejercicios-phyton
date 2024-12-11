#ejemplos

#ejemplo de comentario

#definicion de una funcion
def funcion_ejemplo():
    print("funcion de ejemplo")

#llamada a la funcion
print("Hola, mundo!")

#llamada a la funcion
nombre = "Esteban"
print("Hola %s como estas" % (nombre))

#uso de una funcion de variable
print(nombre.index("e"))


#uso de if
name = "John"
age = 23
if name == "John" and age == 23:
    print ("tu nombre es John, y tu tienes 23 años.")

if name == "John" or name == "Rick":
    print("Tu nombre es John o puede ser Rick.")


#uso de bucle for
primos = [2,3,5,7]
for prime in primos:
    print(primos) 


#uso de bucle while
count = 0
while count < 5:
    print(count) 
    count += 1  # Esto es lo mismo que escribir:  count = count + 1

#uso de clase (object oriented programming)
class MyClass:
     variable = "blah"
     def function(self):
          print() 

myobjectx = MyClass()


#uso de clase con constructor
class MyClass:
    variable = "blah"
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad



#uso de diccionarios
librotelefonico = {
   "Juan" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}

print (librotelefonico["juan"])

#imprimir todos los numeros telefonicos
for name, number in librotelefonico.iteritems():
    print("Número telefónico de %s esta en %d" % (name, number))

del librotelefonico["Juan"]
