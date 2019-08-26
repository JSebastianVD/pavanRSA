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

def generacion_clave():
    num = int(input("Digite numero mayor o igual a 2: "))
    while num < 2:
        print("Error, debe ser mayor o igual a 2")
        num = int(input("Digite numero mayor o igual a 2: "))
    p,q= generacionpyq(num)
    n =

