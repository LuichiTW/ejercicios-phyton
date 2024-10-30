def funcion_ejemplo():
    print("funcion de ejemplo")

print("Hola, mundo!")

nombre = "Esteban"
print("Hola %s como estas" % (nombre))

print nombre.index("e")


name = "John"
age = 23
if name == "John" and age == 23:
    print "tu nombre es John, y tu tienes 23 años."

if name == "John" or name == "Rick":
    print "Tu nombre es John o puede ser Rick."


primos = [2,3,5,7]
for prime in primos:
    print primos


count = 0
while count < 5:
    print count
    count += 1  # Esto es lo mismo que escribir:  count = count + 1

 class MyClass:
      variable = "blah"
      def function(self):
           print "Este mensaje está dentro de una clase."

 myobjectx = MyClass()




 librotelefonico = {
    "Juan" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

print librotelefonico["juan"]

for name, number in librotelefonico.iteritems():
    print "Número telefónico de %s esta en %d" % (name, number)

del librotelefonico["Juan"]
