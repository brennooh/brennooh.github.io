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