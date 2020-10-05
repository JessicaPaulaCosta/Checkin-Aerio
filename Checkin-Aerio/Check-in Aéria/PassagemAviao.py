from Checkin import opcaoinicio, consultaTabela, assento_do_aviao, mostralinhas

#PROGRAMA PRINCIPAL COMPRA DE PASSAGEM AÉRIAS
poltronas=[[1,3,5,7,9,11],[2,4,6,8,10,12],['','','','','',''],[14,16,18,20,22,24],[13,15,17,19,21,23]]

mostralinhas(' BEM VINDO! ')
print("VOE SEGURO - PASSAGENS AÉREAS NACIONAL \nPOLTRONAS RESERVADAS ESTÃO MARCADAS COM O SINAL DE 'X' ")
print("POLTRONAS COM NÚMERAÇÃO IMPAR - LADO DA JANELA\n")

assento_do_aviao(poltronas)
consultaTabela()
opcaoinicio(poltronas)