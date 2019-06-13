# Tipos de dados
a = None
if a is None:
    print ("Nada")

b = list (i for i in range(5))
b = None
if not (b is None):
        print (b)

lista = [2,3,4,5]
tupla = tuple() # tupla vazia
tupla = (2,3,4,5)
print (lista, tupla)

dic = dict () # dicionário vazio
dic = {
    'zero' : 0,
    'um' : 1,
    'dois': 2,
    'tres' : 3,
}
print(dic['dois'])
msg = 'custa dois reais'
novamsg = []
for palavra in msg.split():
    if palavra in dic.keys():
        novamsg.append (str(dic[palavra]))
    else:
        novamsg.append(palavra)
novamsg= ' '.join(novamsg)
print (novamsg)

dic = {
    "I'm": "Eu sou",
    "green": "verde",
    "apple": "maçã",
    "eating": "comendo",
}
msg = "I'm eating a green apple"
traducao = []
for palavra in msg.split():
    if palavra in dic.keys():
        traducao.append(dic[palavra])
    else:
        traducao.append(palavra)
print (' '.join(traducao))
print (dic.items())
print(dic.values())               

# Funções
def imprime(x):
    """
    x: qualquer coisa para print
    """
    print(x)
imprime ('============================')
imprime (2)
imprime ('oLÁ mundO')
imprime (dic)
imprime (2,3)
imrpime (None)
imprime ([True, False])

def distancia(a,b):
    """
    a,b: são listas, tuples, etc com dois elementos no minimo
    retorna distancia euclidiana entre "pontos" a e b
    """
    return((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

imprime(distancia)
imprime(distancia((0,0),(3,4)))
imrpime(distancia([0,0], [3,4]))
imrpime(distancia([0,0], [3,4,5,6,7,8,9,0]))

def divisaoInteira(x,y):
    """
    x, y são numeros
    retorna quociente, resto, flag maior que 1, flag denominador 0
    """
    if y != 0:
        return x//y, x%y, x > y, False 
    else:
        return None, None, x>y, True

quociente, resto = divisaoInteira(15,8)
print('Quociente:', quociente, 'Resto:', resto)

def mapear(funcao, lista):
    """
    aplica funcao em cada elemento de lista:
    retorna lista com resultados
    """
    return list(funcao(elemento) for elemento in lista)
def quadrado(x):
    """
    retorna quadrado de x
    """
    return x**2
def raiz(x):
    """
    retorna raiz de x
    """
    return x**0.5

lista = list (i for i in range(11))
print (lista)
print(mapear(quadrado, lista))
print(mapear(raiz, lista))