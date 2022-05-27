import wikipedia as wiki

#Establecer Lenguaje
wiki.set_lang("es")

#Decorador
def decor(func):
    def wrap():
        print("=====================")
        func()
        print("=====================")
        print("\n")
    return wrap

#Bienvenida
@decor    
def bienvenida():
    print("|  Wikipedia Python  |")

#Variable de busqueda(lista vacia) y busqueda
bus= ""    
@decor
def buscar():
    global bus
    print("|  Que estas Buscando  |")
    bus= input(": ")

#Variable de resultado y muestra de resultados
res=[]     
@decor 
def mostrar():
    global bus, res
    res= wiki.search(bus)
    num= 0
    for i in res:
        print(num, i)
        num += 1

#Seleccion de la opcion elegida y muestra de el contenido
@decor
def opcion():
    global res
    print("| Que numero deseas leer?  |")
    opc= int(input(": "))
    print("\n")
    print("====" + res[opc] + "====")
    print(wiki.summary(res[opc]))

#Funcion para el break    
@decor
def adios():
    print("Hasta Luego :)")
    
bienvenida()

while True:
    print("=====================")
    print("[1]Realizar Busqueda")
    print("[0]Salir")
    print("=====================")
    op= int(input("Que deseas Hacer?: "))
    
    if op == 1:
        buscar()
        mostrar()
        opcion()
    
    elif op == 0:
        adios()
        break
