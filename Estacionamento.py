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
    print (f"Existem {cont_vga} vagas ocupadas neste estacionamento")
    qt = np.count_nonzero(Vagas_ocupadas == None)
    if qt == 1:
        print ("Todas as vagas estão ocupadas...")
        break     
    vaga = random.randint(1, 15)
    print(f"Vaga sorteada: {vaga}")

    if vaga in Vagas_ocupadas:
        print("Vaga já ocupada, sorteando outra...")
        continue  
    Vagas_ocupadas[vaga] = vaga
    cont += 1 
    cont_vga +=1
    print(Vagas_ocupadas)
    while True:
        placa_carro = input('Digite a placa do seu carro: ')
        if placa_carro in Placas:
            print ("Este carro ja está em outra vaga") 
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
    consulta = input ("Você quer consultar algum veiculo? (S/N)")
    if "S" in consulta.upper():
        while True:
            placa_consulta = input("digite a placa do carro que você quer consultar")
            if placa_consulta in Placas:
                indice_placa = np.where(Placas == placa_consulta)
                vaga_correspondente = indice_placa[0]
                print (f"O seu carro com a placa {placa_consulta} está na vaga {vaga_correspondente} no setor ")
            else:
                print ("Não existe nenhum veiculo com esta placa no estacionamento, verifique se digitou corretamente")
                continue
