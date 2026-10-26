monstros = ["monstro", "rei", "monstro", "monstro", "Rei"] # definindo uma lista com n valores

def atacar(x):
    return x

for n in monstros:
    if  n == "monstro":
        dano = atacar(8)
        print(f"ataquei dano tirado: {dano}")
    else:
        print("Vou proteger o rei")



# Agora usando o While Enquanto algo for true faça

loop = True
while loop == True: # Ou podemos só colocar while loop:
    print("jogando") # tome cuidade while pode ser infinito e travar sua maquina ou o vs code
    