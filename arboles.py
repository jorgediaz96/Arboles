class Nodo:
    def __init__(self,valor,izq=None,der=None):
        self.valor=valor
        self.izq=izq
        self.der=der

def insertar (arbol,valor):
    if arbol==None:
        return  Nodo(valor)
    elif arbol.valor > valor:
            return Nodo(arbol.valor,insertar(arbol.izq,valor),arbol.der)
    elif arbol.valor < valor:
            return Nodo(arbol.valor,arbol.izq,insertar(arbol.der,valor))
def lista_a_arbol(lista,arbol=None):
    if len(lista)==0:
        return None
    return lista_a_arbol(lista[1:],insertar(arbol,lista[0]))


def buscar(arbol, valor):
    if arbol==None:
        return False
    if arbol.valor==valor:
        return True
    if arbol.valor > valor:
        return buscar(arbol.izq,valor)
    return buscar(arbol.der,valor)

def a_lista(arbol):
    if arbol == None:
        return []
    return a_lista(arbol.izq)+[arbol.valor]+a_lista(arbol.der)

def a_num(arbol):
    if arbol == None:
        return 0
    return a_num(arbol.izq)+arbol.valor+a_num(arbol.der)


       
    

    
a=Nodo(5,Nodo(3),Nodo(10,Nodo(8)))
#print(buscar(a,6))
print(a_lista(a))
print (a_lista(insertar(a,16)))
#print (a_num(a))
#insertar(a,7)
#print (a_lista(a))
print(a_lista(lista_a_arbol([2,1,5,9,10])))