import Pagamento

def checkinPassageiro(numeroassento, vetdestino, numcadeira):
    nomecompleto=''
    listaPassageiros=[]
    contador=1
    qtdassento = 0

    while contador <= numeroassento:
        nome = input(f"Digite o {contador} nome do(a) passageiro(a): ")
        sobrenome = input(f"Digite o sobrenome do(a) {nome} : ")

        while True:
            try:
                idade =int(input(f"Digite a idade do(a) {nome} : "))
            except:
                print("Você não digitou um número.")
                continue
            else:
                contador += 1
                if(idade <18):
                    print("\n** OBS: Todo o embarque de passageiro menor de idade, deve ser acompanhado pelo responsável legal")
                    break
            #concatenação de nome e sobrenome
            nomecompleto=nome+" "+sobrenome

            listaPassageiros.append(nomecompleto)

            listaPassageiros.append(idade)
            if idade>0:
                break

        Pagamento.quitar(numeroassento, vetdestino, numcadeira, listaPassageiros)
        break
#-----------------------------------------------------------------
def checkinAssento(reservadestino):
    global poltronas, num_assentos_colhidos,cadeiras
    janela1 = ['1', '3', '5', '7', '9', '11']
    janela2 = ['13', '15', '17', '19', '21', '23']
    corredor1 = ['2', '4', '6', '8', '10', '12']
    corredor2 = ['14', '16', '18', '20', '22', '24']

    while True:
        try:
            num = input('Digite o número da poltrona que deseja viajar: ')
        except :
            print('Você não digitou um número.\n')
            continue
        else:
            if (num in janela1):
                print(f"\nA poltrona {num} da janela foi reservada com um X \n")
                a = int(janela1.index(num))
                poltronas[0][a] = 'X'
            elif (num in janela2):
                print(f"A poltrona {num} da janela foi reservada com X \n")
                a = int(janela2.index(num))
                poltronas[4][a] = 'X'
            elif (num in corredor1):
                print(f"A poltrona {num} do corredor foi reservada com X \n")
                a = int(corredor1.index(num))
                poltronas[1][a] = 'X'
            elif (num in corredor2):
                print(f"A poltrona {num} do corredor foi reservada com X \n")
                a = int(corredor2.index(num))
                poltronas[3][a] = 'X'
            elif (num=='X' or num=='x'):
                print("Poltrona indisponivel!\n")
                checkinAssento(reservadestino)
                num_assentos_colhidos-= 1 #decrementa a cadeira ja reservada
            else:
                print("Poltrona invalida! \n")
                checkinAssento(reservadestino)

        num_assentos_colhidos+=1 #incrementa
        cadeiras.append(num)
        assento_do_aviao(poltronas)  # imprime o assento com a reserva

        while True:
            try:        # tratamento de erro
                novoCheckin = int(input("Deseja reservar outro assento no voo:   1- SIM  2-NÃO  3-Cancelar Reserva\n"))
            except:
                print("Você não digitou um número.")
                continue
            else:
                if (novoCheckin == 1):
                    checkinAssento(reservadestino)
                    break
                elif (novoCheckin==2):
                    checkinPassageiro(num_assentos_colhidos, reservadestino, cadeiras)
                    break
                elif (novoCheckin==3):
                    num_assentos_colhidos=0
                    print('Reserva cancelada!')
                    opcaoinicio(poltronas)
                    break
                else:
                    print("Opção invalida!")
                break
            break
        break
#-----------------------------------------------------------------
def checkinDestino(poltronas):
    valor=[]

    while True:
        try:    # tratamento de erro
            regial = int(input("Digite a regional que deseja viajar:\n 1-SUL  2-CENTRO OESTE  3-NORDESTE  4-NORTE\n"))
        except:
            print("Você não digitou um número: ")
            continue
        else:
            if(regial==1):
                valor='SUL',1000.00
                checkinAssento(valor)
                break
            elif(regial == 2):
                valor='CENTRO OESTE',1100.0
                checkinAssento(valor)
                break
            elif(regial == 3):
                valor='NORDESTE',900.0
                checkinAssento(valor)
                break
            elif (regial == 4):
                valor='NORTE',850.0
                checkinAssento(valor)
                break
            else:
                print("Destino invalida!")
        break
#-----------------------------------------------------------------
def consultaTabela():
    mostralinhas(" TABELA: VOO REGIONAL")
    tabela = [['SUDESTE', '', 'und. R$'], ['-->', 'SUL', '1.000,00'], ['-->', 'CENTRO OESTE', '1.100,00'],
              ['-->', 'NORDESTE', '900,00'], ['-->', 'NORTE', '850,00']]

    for linhas in range(0, 5):
        for colunas in range(0, 3):
            print(f'[{tabela[linhas][colunas]:^12}]', end='')
        print()  # quebra de linha

    print("\n*** Para pagamento à vista, desconto de 5% *** \n")
    return tabela
#-----------------------------------------------------------------
def opcaoinicio(poltronas):
    while True:
        try:
            escolha = int(input("\nDigite a opção: \n1-Check-in  2-Sair do sistema\n"))
        except:
            print("Você não digitou um número: ")
            continue    #o sistema não encerra até que digite um número
        else:
            if (escolha == 1):
                checkinDestino(poltronas)
                break
            elif (escolha == 2):
                print("Volte Sempre!")
                break
            else:
                print("Opção invalida!")
        break

#-----------------------------------------------------------------
def assento_do_aviao(reserva):
    for linha in range(0, 5):
        for coluna in range(0, 6):
            # impressão de intervalo de 10 caracteres e centralizados
            print(f'[{reserva[linha][coluna]:^2}]', end='')
        print()  # quebra de linha
#-----------------------------------------------------------------
def mostralinhas(texto):
    print(texto)
    print('-' * 45)


cadeiras=[]
num_assentos_colhidos=0
poltronas=[[1,3,5,7,9,11],[2,4,6,8,10,12],['','','','','',''],[14,16,18,20,22,24],[13,15,17,19,21,23]]