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


def euclides_extendido(a,b):
    s = 1
    t = 0
    sp =0
    tp = 1
    finala = a
    finalb = b
    while b!= 0:
        q = a//b
        r = a % b
        a,s,t,b,sp,tp = b,sp,tp,r,(s - (sp * q)), (t - (tp * q))
    if s < 0:
        s += finala
    return s


def generacion_clave():
    clave_publica = []
    clave_privada = []
    d = 1
    num = int(input("Digite numero mayor o igual a 2: "))
    while num < 2:
        print("Error, debe ser mayor o igual a 2")
        num = int(input("Digite numero mayor o igual a 2: "))
    p,q= generacionpyq(num)
    n = p*q
    clave_privada.append(n)
    clave_publica.append(n)
    phi = (p-1)*(q-1)
    e = random.randrange(1, phi)
    while not es_coprimo(e,phi):
        e = random.randrange(1,phi)
    d = euclides_extendido(e,phi)
    clave_privada.append(d)
    clave_publica.append(e)
    return clave_publica, clave_privada

def mypow(x,n):
    if n==1:
        x=x
    elif n%2==0:
        x= pow(mypow(x,n/2),2)
    elif n%2==1:
        x= x*mypow(x,n-1)
    return x

def cifrado(mensaje_letra, clave):
    mensaje_num= []
    for i in range(len(mensaje_letra)):
        caracter = ord(mensaje_letra[i])
        mensaje_num.append(caracter)
    for j in range(len(mensaje_num)):
        mensaje_num[j] = mypow(mensaje_num[j],clave[1])%clave[0]
    return mensaje_num

def descifrado(mensaje_num,clave):
    mensaje_letra= ""
    for i in range(len(mensaje_num)):
        mensaje_num[i] = mypow(mensaje_num[i], clave[1]) % clave[0]
    for j in range(len(mensaje_num)):
        mensaje_letra = mensaje_letra + chr(mensaje_num[j])
    return mensaje_letra

clavepriv=[]
clavepubli=[]
clavepubli,clavepriv = generacion_clave()
cifrado("Ho la",clavepubli)
print(descifrado(cifrado("Hola",clavepubli),clavepriv))
