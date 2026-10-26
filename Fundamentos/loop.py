# Criando uma variavel str
nome = "hero"

# Criando uma variavel int

vida = 10

# Criando uma variaveis booleana True or False

vivo = True

# Criando funções

def atacar(x):  # X é um parametro quando eu chamar essa função temos que passar esse valor de ataque
         #Def diz que é uma função pulo é o nome da função
    print("Dano", x)

3 # Criando função de pulo
def pulo():
    print("Pulou")

# Criando função de defesa

def defesa():
    print("defesa")


    # Para usar a função temos que chamar e assim aparece na tela

atacar(12)

pulo()

atacar(23)   # Assim vai imprimir o ataque o pulo e o ataque na tela


def criar_plataformar():
    print("Criou uma plataforma")

# Criando uma quantidade de vezes com for

for n in range(10):
    criar_plataformar()   # Assim criamos uma plataforma 10 vezes 
