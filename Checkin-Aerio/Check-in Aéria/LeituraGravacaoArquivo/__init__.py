import csv

def lerArquivo():
    try:
        with open("texto.csv","r") as arq1:
            dados = csv.reader(arq1)   #abrir o arquivo e salva o conteúdo no objeto dados
            linhas= dados.split('\n') #divide o arquivo sempre que encontrar uma linha
            print(linhas) #imprime o arquivo separado por linha
    except IOError:
        print("Erro: arquivo não encontrado ou não pode ser salvo.")
    else:
        print("Contéudo gravado com sucesso!")
    finally:
        arq1.close()

def gravarArquivo():
    # sobrescrever o conteúdo do arquivo
    arquivo= open("texto.csv", 'w')
    try:
        arq2 = csv.writer(arquivo)
        arq2.writerow(('primeira','segunda','terceira'))
        arq2.write("\n")
        print(arq2)
    except IOError:
        print("Erro: arquivo não encontrado ou não pode ser salvo.")
    else:
        print("Contéudo gravado com sucesso!")
    finally:
        arq2.close()


def acrescAarquivo(tuplaPassageiros, tupladestino, strnumCadeira, totalcheckin, strdata_em_texto):
    arq3 = open('texto.csv','a')
    arq3.write(f"\nReserva para: {tuplaPassageiros} \n")
    arq3.write("Reserva de vôos:\n")
    arq3.write(f"Trecho :\nOrigem: SULDESTE \nDestino: {tupladestino} \nnúmero de assento {strnumCadeira}\n")
    arq3.write(f"Valor total das passagens R$: {totalcheckin:.2f}\n")
    arq3.write(f"Data da compra: {strdata_em_texto}")
    print('Operação concluída! '+arq3.name+' usando o modo acrescentar')
    arq3.close()