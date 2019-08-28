import random
def es_primo(numero):
    if numero==2:
        return True
    elif numero < 2 or numero % 2 == 0:
        return False
    for i in range(3, numero, 2):
        if numero % i == 0:
            return False
    return True
def numero_primo_random(n):
    p = random.randrange(n,2*n)
    while not es_primo(p):
        p = p + 1
        if p == 2*n:
            p = n
    return p

def generacionpyq(n):
    p = numero_primo_random(n)
    q = numero_primo_random(n)
    while p==q:
        q = numero_primo_random(n)
    return p,q

def es_coprimo(n,m):
    global lista
    lista = []
    global lista2
    lista2=[]
    for i in range(2,n+1):
        if n%i==0:
            lista.append(i)
    for j in range(2,m+1):
        if m%j==0:
            lista2.append(j)
    for k in range(len(lista)):
        if lista[k] in lista2:
            return False

    return True

def generacion_clave():
    num = int(input("Digite numero mayor o igual a 2: "))
    while num < 2:
        print("Error, debe ser mayor o igual a 2")
        num = int(input("Digite numero mayor o igual a 2: "))
    p,q= generacionpyq(num)
    n = p*q
    phi = (p-1)*(q-1)
    e = random.randrange(1, phi)
    while not es_coprimo(e,phi):
        e = random.randrange(1,phi)
    print(str(e))
    print(str(phi))
