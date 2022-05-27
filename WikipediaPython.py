import wikipedia as wiki
wiki.set_lang("es")

def decor(func):
    def wrap():
        print("=====================")
        func()
        print("=====================")
        print("\n")
    return wrap

@decor    
def bienvenida():
    print("|  Wikipedia Python  |")

bus= ""    
@decor
def buscar():
    global bus
    print("|  Que estas Buscando  |")
    bus= input(": ")

res=[]     
@decor 
def mostrar():
    global bus, res
    res= wiki.search(bus)
    num= 0
    for i in res:
        print(num, i)
        num += 1

@decor
def opcion():
    global res
    print("| Que numero deseas leer?  |")
    opc= int(input(": "))
    print("\n")
    print("====" + res[opc] + "====")
    print(wiki.summary(res[opc]))
    
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
