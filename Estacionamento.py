import numpy as np
import random

SetorA = np.array([1, 2, 3, 4, 5])
SetorB = np.array([6, 7, 8, 9, 10])
SetorC = np.array([11, 12, 13, 14, 15])
Vagas_ocupadas = np.empty(16,dtype=object)
Placas = np.empty(16,dtype=object)
vaga = [] 
cont = -1
cont_vga = 0
while True:
    # print (f"estão disponiveis as vagas{SetorA - Vagas_ocupadas}no setor A")
    print (f"Existem {cont_vga} vagas ocupadas neste estacionamento") # mudar
    if len(Vagas_ocupadas)== 17:
        print ("Todas as vagas estão ocupadas...")
        break     
    vaga = random.randint(1, 15)
    print(f"Vaga sorteada: {vaga}")

    if vaga in Vagas_ocupadas:
        print("Vaga já ocupada, sorteando outra...")
        continue  
    # Vagas_ocupadas = np.append(Vagas_ocupadas,vaga)
    Vagas_ocupadas[vaga] = vaga
    cont += 1 
    cont_vga +=1
    print(Vagas_ocupadas)
    while True:
        placa_carro = input('Digite a placa do seu carro: ')
        if placa_carro in Placas:
            print ("Este carro ja está em outra vaga") #funciona mas ele sorteia outra vaga para o carro, deixar de um jeito que apenas peça para digitar outra placa
            Vagas_ocupadas[cont] = None
            continue
        elif placa_carro == "":
            print("Está não é uma placa valida")
            continue
        else:
            Placas[vaga] = placa_carro
            cont -= 1
            break    
    print (Placas)
    while True:
        saida = input("Você deseja sair do estacionamento(S/N)")
        if "S" in saida.upper():
            while True:
                vaga_estacionada = int(input("Em qual vaga você estava?"))
                if Vagas_ocupadas[vaga_estacionada] == None:
                    print('esta vaga não esta ocupada')
                    continue
                else:
                    Vagas_ocupadas[vaga_estacionada] = None 
                    Placas [vaga_estacionada] = None
                    cont -=1
                    cont_vga -=1
                    print (Vagas_ocupadas)
                    break
        else:
            break