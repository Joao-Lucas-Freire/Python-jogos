nome = "hero"
vida = 10
ataque = 3
defesa = 2
vivo = True     # Definindo atributos do usuario

# Criando os metodos de atacar coletar e resgatar

def atacar():
    print("Atacando")

def coletar():
    print("Coletando")

def resgatar():
    print("resgatando")


def main():
    nome=(input("Digite seu nome "))

    print(f"SEJA BEM VINDO {nome.upper()} \n")

    print("VOCÊ TEM 3 MISSÕES ESCOLHA UMA DELAS")
    escolha=int(input("1 - Matar Goblins \n 2 - Conseguir materiais \n 3 - Resgatar inocentes"))
    if escolha == 1:
        print("Escolha 1 - Matar goblins")
        atacar()
    elif escolha == 2:
        print("Escolha 2 - Conseguir materiais")
        coletar()
    elif escolha == 3:
        print("Escolha 3 - Resgatar inocentes")
        resgatar()
    else:
        print("Escolha um numero válido 1 - 2 - 3")

main()

loop = True
while loop:
    main()