
nombre = "juan manuel"
apellido = "galeano pineda"

print(nombre)
print(apellido)
print(nombre, apellido)

print("ingresa tu nombre")

nombre = input("nombre:")

print("ingresa tu edad")

edad = int(input("edad:"))

suma = edad + 3

if  edad>18:
    print("mayor de edad")
else:
    print("menor de edad")

#######################################################
print("ingresa tu salario")
ingreso = int(input("ingreso:"))

if ingreso>4000000 and ingreso<10000000:
    
    print (nombre,"tiene que pagar", ingreso*0.15)
    
    print("tu impuesto es del 15%")
    
elif ingreso> 10000000 and ingreso< 15000000:
    
    print (nombre,"tiene que pagar", ingreso*0.20)
    
    print("tu impuesto es del 20%")
    

else:
    
    print (nombre,"tiene que pagar", ingreso*0.30)
    
    print("tu impuesto es del 30%")

#######################
    
miList = []

count = 0

while count <=100:
    
    miList.append(count)
    count=count+1

name = input("nombre:")

miList = []

countDos = 0
while countDos <= 99:
    
    miList.append(name)
    countDos=countDos+1


print("ingresa tu nombre")

nombre = input("nombre:")



mylist = []

count = 0
while count <= 2: 
    
    ingreso = int(input("ingreso:"))
    
    mylist.append(ingreso)
    
    count = count+1
    
    



    if ingreso>4000000 and ingreso<10000000:
        
        print (nombre,"tiene que pagar", ingreso*0.15)
        
        print("tu impuesto es del 15%")
        
    elif ingreso> 10000000 and ingreso< 15000000:
        
        print (nombre,"tiene que pagar", ingreso*0.20)
        
        print("tu impuesto es del 20%")
        
    
    else:
        
        print (nombre,"tiene que pagar", ingreso*0.30)
        
        print("tu impuesto es del 30%")

###############################################################

mylist = []

count = 0
while count <= 2: 
    
    x = int(input("x="))
    
    y = int(input("y="))
    
    print(suma(x+y))
    
    mylist.append(ingreso)
    
    count = count+1
    
    





















































    