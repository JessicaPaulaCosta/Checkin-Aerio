import Checkin
from LeituraGravacaoArquivo import acrescAarquivo
from datetime import date, datetime
                                                                                #passagem de parametro opcional
def comprovate(qtcadeirasEscolhida, nomePassageiros, destinoPassageiro, numDasCadeiras, valorcheckin, numParcela=1):
    data_atual = date.today()
    data_em_texto = '{}/{}/{}'.format(data_atual.day, data_atual.month, data_atual.year)

    print('-' * 45)
    Checkin.mostralinhas("Segue abaixo a confirmação da reserva:")

    i=0
    while i < qtcadeirasEscolhida:
        resultado = i%2
        if resultado==0:
            print(f"Reserva para: {nomePassageiros[i].upper()}\nidade: {nomePassageiros[i+1]}")
            Checkin.mostralinhas("Reserva de vôos:")
            print(f"Trechos :\nOrigem: SULDESTE \nDestino: {destinoPassageiro[0]} \nnúmero de assento reservado no avião: {numDasCadeiras[i]}")
            #break
        else:
            print(f"Reserva para: {nomePassageiros[i+1].upper()}\nidade: {nomePassageiros[i+2]}")
            Checkin.mostralinhas("Reserva de vôos:")
            print(f"Trecho :\nOrigem: SULDESTE \nDestino: {destinoPassageiro[0]} \nnúmero de assento reservado no avião:{numDasCadeiras[i]}")
            break
        valorPorPassagem=valorcheckin/qtcadeirasEscolhida
        print("Valor total das passagens: R$ %.2f com %d parcelas iguais de R$ %.2f" % (
        valorPorPassagem, numParcela, valorPorPassagem/numParcela))
        print(f"\tCompra efetuada em: {data_em_texto}")
        print('@*'*40,'\n\n')
        i+=1

    acrescAarquivo(nomePassageiros, destinoPassageiro, numDasCadeiras, valorcheckin, data_em_texto)
