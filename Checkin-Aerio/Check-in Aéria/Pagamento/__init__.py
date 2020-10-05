import Checkin
from Recibo import comprovate

def quitar(qtdassento, tupladestino,numerocadeira, listapassageiro):
    totalcompra=qtdassento * int(tupladestino[1])
    Checkin.mostralinhas("Pagamento no débito 5% desconto \nPagamento no crédito, acrescimo de 2% ao mês")

    while True:
        try:
            formapagamento=int(input("Digite a forma de pagamento 1-Débito 2-Crédito \n"))
        except :
            print('Você não digitou um número. \n')
            continue
        else:
            if(formapagamento==1):
                valortotal=float(totalcompra*0.95)
                print("\nReserva efetuada com sucesso!")
                comprovate(qtdassento, listapassageiro, tupladestino, numerocadeira, valortotal) #passagem de parametro formal
                break
            elif(formapagamento==2):
                parcela=int(input("Digite o número de parcelas: \n"))
                valor_checkin= int(tupladestino[1])*((1+0.02)**parcela)
                comprovate(qtdassento, listapassageiro, tupladestino, numerocadeira, valor_checkin, parcela) #passagem de parametro formal
                break
            else:
                print("Opção inválida!")
        break