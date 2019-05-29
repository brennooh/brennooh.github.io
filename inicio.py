# Tipos básicos
a = 1 # inteiros
b = 1.2 # ponto flutuante
c = "c" # string
d = 'minha terra tem palmeiras' # string
e = d[3] # "caractere
print (a,b,c,d,e)

# Operadores aritméticos + - * / // % **
# A <op>=b =========== a = a <op> b
x = 1 + 2 # Soma
y = 4 - 3 # Subtração
z = 5/2 # Divisão com ponto flutuante
w = 5//2 # Divisão inteira
u = 5%2 # Módulo (resto da divisão)
v = 5**2 # Potência (elevado a)
t = 25**(1/2) # Raiz (elevado a 0.5) == 25**0.5
r = int(25**0.5)
print (x,y,z,w,u,v,t,r)

# conversão entre tipos
r = int(5.0)
s = float (5)
f = str(r)
g = int('23') + 2
print (r,s,f,g)

# Strings
msg = 'The quick brown fox jumps over the lazy dog'
print (msg[0], len(msg))
s0 = msg[4:9]
print ('0:', s0)
s1 = msg[40:]
print ('1:', s1)
s2 = msg [:3]
print ('2:', s2)
s3 = msg [-8:]
print ('3:', s3)
s4 = msg [-8:-4]
print ('4:', s4)
s5 = msg [-1]
print ('5:', s5)
s6 = msg.upper()
print ('6:', s6)
s7 = msg.lower ()
print ('7:', s7)
s8 = 'minha terra tem'.upper()
print ('8:', s8)
s9 = 'minha terra tem'[6:-4]
print ('s9:', s9)
msga = "\n         meu   texto        \t\t"
print (msga.strip()) # Retira caracteres não visiveis (espaço)
msgb = '\t\t 3;4.5;6;-7.6;cardio;xx\n' .strip()
print (msgb.split(';'))
print (s8 + '' , msga.strip())
caracteres = "\n\t\'\\"
print (caracteres)

# Lógica Booleana
q0 = True
q1 = False
q2 = q0 and q1
q3 = q0 or q1
q4 = not q3
# Decisão
if q4 and not q3:
    print ('Olá')
elif q1 and not q2:
    print ('EITA PORRA')
else:
    print ('Tchau')

# Comparações
print (3 > 4)
print (3 >= 4)
print (3 < 4)
print (3 <= 4)
print (3 == 4)
print (3 != 4, not ( 3 ==4))

# Arrays / Listas
li = [1,2,3,4]
print (li)
li = [1,'2', 3.5,"jimmy".upper]
print (li, len(li))
# referência na lista igual a da string
print (li[1:4])

# Laço
print ('Laço')
stri = ''
for i in range (5):
    stri += str (i) + ' '
print (stri)
stri = ''
for i in range(6,11):
    stri += str(i) + ' '
print (stri)
for i in range (10,101,5):
    stri += str (i) + ' '
    print (stri)
li = [1,2,3,4,5,6,7,8]
stri = ''
for el in li:
    stri += str(el) + " "
print (stri)
# for (i = 0; i < li.lenght; o++) {console log (i):}
for xaxaxaxaxaxaxaxa in li:
    print (xaxaxaxaxaxaxaxa)

li = [1,2,3,4,5,6,7,8]
for i, el in enumerate (li):
    print (i, ";", el)

# random
li0 = list(range(1,100,2))
print (li0)
li1 = list(i**2 for i in li0)
print (li1)
li2 =list(e for e in li0 if e%3 ==0)
print (li2)
Matriz = list(list((i,j) for j in range (4)) for i in range (4))
for linha in Matriz:
    print (linha)