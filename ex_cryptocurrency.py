'''
Objetivo:

Desenvolver um algoritmo em Python para simular a compra, venda e troca de criptomoedas, sem automatizar o processo. O objetivo é auxiliar na tomada de decisões de investimento, fornecendo informações e cálculos relevantes.

Funcionalidades:

Simulação de Compra de Criptomoedas:

O programa deve permitir a escolha da criptomoeda a ser comprada.

O programa deve solicitar o valor a ser investido.

O programa deve calcular o número de criptomoedas que podem ser compradas com o valor informado, considerando o preço atual da moeda.

O programa deve simular a compra da criptomoeda, exibindo o valor total da compra, incluindo taxas.

O programa deve permitir a simulação de diferentes cenários, como a compra em diferentes datas ou com diferentes valores.
/////////////////////////////////////////

Simulação de Venda de Criptomoedas:

O programa deve permitir a escolha da criptomoeda a ser vendida.

O programa deve solicitar a quantidade de criptomoedas a ser vendida.

O programa deve calcular o valor total da venda, considerando o preço atual da moeda e as taxas.

O programa deve simular a venda da criptomoeda, exibindo o lucro ou prejuízo da operação.

O programa deve permitir a simulação de diferentes cenários, como a venda em diferentes datas ou com diferentes quantidades.
///////////////////////////////////////

Simulação de Troca de Criptomoedas:

O programa deve permitir a escolha das criptomoedas a serem trocadas.

O programa deve solicitar a quantidade de uma das criptomoedas a ser trocada.

O programa deve calcular a quantidade da outra criptomoeda que será recebida na troca, considerando a taxa de câmbio entre as moedas.

O programa deve simular a troca de criptomoedas, exibindo o valor total da operação e a taxa de câmbio utilizada.

O programa deve permitir a simulação de diferentes cenários, como a troca em diferentes datas ou com diferentes quantidades.
'''
COTACAO_DOLAR = 5.02
BITCOIN = 65000.00
ETHEREUM = 3400.00
SOLANA = 190.00
TIA = 13.88

TAXA_PLATAFORMA = 0.02
TAXA_TROCA = 0.03

saldoreais_previo_cliente = 1585.69
saldo_att_cliente = []
saldo_btc = []
saldo_eth = []
saldo_sol = []
saldo_tia = []


def crypto_exchange(): 
    mensagem = f'Olá, seja bem vindo(a) ao cryptofuture app'
    nome = input(f'Olá, por favor digite seu nome: ')
    boas_vindas = f'{mensagem}, {nome}! Aqui você encontra uma variedade de serviços em criptomoedas. O seu saldo atual é de R${saldoreais_previo_cliente}. Escolha abaixo a opção que você deseja realizar em nosso aplicativo.'
    print(boas_vindas)
    seleciona_acao = input(f'Para comprar uma crypto digite "c". Para vender digite "v" ou para trocar digite "t". E para adicionar crédito a plataforma digite "add": ').lower()
    print(seleciona_acao)

    if seleciona_acao == "c":
        buy_crypto()
    elif seleciona_acao == "v":
        sell_crypto()
    elif seleciona_acao == "t":
        swap_crypto()
    else:
        print('Algo deu errado na crypto_exchange.')


def buy_crypto():
    while True:
        buy_amount = float(input(f'Digite aqui qual valor deseja comprar: '))
        print(buy_amount)
        choose = input(f'Escolha a moeda que deseja comprar. Digite uma das opcoes: "BITCOIN", "ETHEREUM", "SOLANA", "TIA":  ').upper()
        print(choose)

        if buy_amount > saldoreais_previo_cliente:
            print('Saldo insuficiente para realizar a compra.')
            return

        if choose == "BITCOIN":
            fracao = buy_amount / BITCOIN
            informa_total_compra = (buy_amount * TAXA_PLATAFORMA) + buy_amount
            print(f' O total da compra + taxas é de R${informa_total_compra}')
            reduz_saldo = saldoreais_previo_cliente - informa_total_compra
            print(reduz_saldo)
            saldo_att_cliente.append(reduz_saldo)
            print(saldo_att_cliente)

            # Atualiza o saldo após a compra
            saldo_atual = saldo_att_cliente[-1]
            novo_saldo = saldo_atual - informa_total_compra
            saldo_att_cliente[-1] = novo_saldo
            print(saldo_att_cliente)

            saldo_btc.append(fracao)
            print(f'Você finalizou a compra de {fracao} BITCOIN. E o seu saldo é de R${reduz_saldo}.')
        elif choose == "ETHEREUM":
            fracao = buy_amount / ETHEREUM
            informa_total_compra = buy_amount * TAXA_PLATAFORMA + buy_amount
            print(f' O total da compra + taxas é de R${informa_total_compra}.')
            reduz_saldo = saldoreais_previo_cliente - informa_total_compra
            print(reduz_saldo)
            saldo_att_cliente.append(reduz_saldo)
            print(saldo_att_cliente)
            saldo_eth.append(fracao)
            print(f'Você finalizou a compra de {fracao} ETHEREUM. E o seu saldo é de R${reduz_saldo}.')
        elif choose == "SOLANA":
            fracao = buy_amount / SOLANA
            informa_total_compra = buy_amount * TAXA_PLATAFORMA + buy_amount
            print(f' O total da compra + taxas é de R${informa_total_compra}.')
            reduz_saldo = saldoreais_previo_cliente - informa_total_compra
            print(reduz_saldo)
            saldo_att_cliente.append(reduz_saldo)
            print(saldo_att_cliente)
            saldo_sol.append(fracao)
            print(f'Você finalizou a compra de {fracao} Solana. E o seu saldo é de R${reduz_saldo}.')
        elif choose == "TIA":
            fracao = buy_amount / TIA
            informa_total_compra = buy_amount * TAXA_PLATAFORMA + buy_amount
            print(f' O total da compra + taxas é de R${informa_total_compra}.')
            reduz_saldo = saldoreais_previo_cliente - informa_total_compra
            print(reduz_saldo)
            saldo_att_cliente.append(reduz_saldo)
            print(saldo_att_cliente)
            ultimo_saldo_compra = float(saldo_att_cliente[-1])
            saldo_outras_compras = ultimo_saldo_compra -informa_total_compra
            print(saldo_outras_compras)
            saldo_att_cliente.append(saldo_outras_compras)
            saldo_tia.append(fracao)
            print(saldo_tia)
            print(f'Você finalizou a compra de {fracao} Tia. E o seu saldo é de R${reduz_saldo}.')
        else:
            print('Opção de criptomoeda inválida.')

        repetir = input(f'Você gostaria de comprar mais criptomoedas? Se sim digite "c" ou digite "v" para vender, "t" para trocar ou "s" para sair: ').lower()
        if repetir == "c":
            buy_crypto()
        elif repetir == "v":
            sell_crypto()
        elif repetir == "t":
            swap_crypto()
        else:
            print('Você saiu do programa! Te esperamos de volta.')
        break

def sell_crypto():
    while True:
        choose = input(f'Escolha a moeda que deseja vender. Digite uma das opções: "BITCOIN", "ETHEREUM", "SOLANA", "TIA":  ').upper()
        print(choose)
        sell_amount = float(input(f'Digite aqui qual valor deseja vender: '))
        print(sell_amount)

        ultimo_saldo_reais_lista = float(saldo_att_cliente[-1])
        print(f'O seu últmo saldo é de R${ultimo_saldo_reais_lista}.')

        if sell_amount > ultimo_saldo_reais_lista:
            print('Você está tentando vender um valor maior que seu saldo.')
            return
        
        if choose == "BITCOIN":        
            ultimo_saldo_btc = float(saldo_btc[-1])
            print(ultimo_saldo_btc)

            fracao_venda_btc = sell_amount / BITCOIN
            print(fracao_venda_btc)

            if ultimo_saldo_btc < fracao_venda_btc:
                print(f'Você está tentando vender um saldo maior do que tem. Seu saldo é de {ultimo_saldo_btc} Bitcoin.')
                return
            att_saldo_btc = ultimo_saldo_btc - fracao_venda_btc
            saldo_sol.append(att_saldo_btc)

            saldo_apos_venda = sell_amount + ultimo_saldo_reais_lista - (sell_amount * TAXA_PLATAFORMA)
            print(f'Seu saldo descontado taxa de 0.002% é de: R${saldo_apos_venda}. E você ainda têm na sua carteira cripto {att_saldo_btc} Bitcoin.')

        elif choose == "ETHEREUM":
            
            ultimo_saldo_eth = float(saldo_eth[-1])
            print(f'O seu saldo de Ethereum é de: {ultimo_saldo_eth}')

            fracao_venda_eth = sell_amount / ETHEREUM
            print(f'Você está vendendo {fracao_venda_eth} Ethereum.')

            if ultimo_saldo_eth < fracao_venda_eth:
                print(f'Você está tentando vender um saldo maior do que tem. Seu saldo é de {ultimo_saldo_eth} Ethereum.')
                return
            
            att_saldo_eth = ultimo_saldo_eth - fracao_venda_eth
            saldo_sol.append(att_saldo_eth)

            saldo_apos_venda = sell_amount + ultimo_saldo_reais_lista - (sell_amount * TAXA_PLATAFORMA)
            print(f'Seu saldo descontado taxa de 0.002% é de: R${saldo_apos_venda}. E você ainda têm na sua carteira cripto {att_saldo_eth} Ethereum.')
            saldo_att_cliente.append(saldo_apos_venda)  
            
        elif choose == "SOLANA":
            
            ultimo_saldo_sol = float(saldo_sol[-1])
            print(f'O seu saldo de Ethereum é de: {ultimo_saldo_sol}')

            fracao_venda_sol = sell_amount / SOLANA
            print(f'Você está vendendo {fracao_venda_sol} Solana.')

            if ultimo_saldo_sol < fracao_venda_sol:
                print(f'Você está tentando vender um saldo maior do que tem. Seu saldo é de {ultimo_saldo_eth} Solana.')
                return
            
            att_saldo_sol = ultimo_saldo_sol - fracao_venda_sol
            saldo_sol.append(att_saldo_sol)

            saldo_apos_venda = sell_amount + ultimo_saldo_reais_lista - (sell_amount * TAXA_PLATAFORMA)
            print(f'Seu saldo descontado taxa de 0.002% é de: R${saldo_apos_venda}. E você ainda têm na sua carteira cripto {att_saldo_sol} solanas.')
            saldo_att_cliente.append(saldo_apos_venda)        

        elif choose == "TIA":
            
            ultimo_saldo_tia = float(saldo_tia[-1])
            print(f'O seu saldo de Ethereum é de: {ultimo_saldo_tia}')

            fracao_venda_tia = sell_amount / TIA
            print(f'Você está vendendo {fracao_venda_tia} TIA.')

            if ultimo_saldo_tia < fracao_venda_tia:
                print(f'Você está tentando vender um saldo maior do que tem. Seu saldo é de {ultimo_saldo_tia} TIA.')
                return
            
            att_saldo_tia = ultimo_saldo_tia - fracao_venda_tia
            saldo_sol.append(att_saldo_tia)
            
            saldo_apos_venda = sell_amount + ultimo_saldo_reais_lista - (sell_amount * TAXA_PLATAFORMA)
            print(f'Seu saldo descontado taxa de 0.002% é de: R${saldo_apos_venda}. E você ainda têm na sua carteira cripto {att_saldo_tia} TIA.')
            saldo_att_cliente.append(saldo_apos_venda) 
        else:
            print('Opção de criptomoeda inválida.')
        
        repetir = input(f'Você gostaria de vender mais criptomoedas? Se sim digite "v" ou digite "c" para comprar, "t" para trocar ou "s" para sair: ').lower()
        if repetir == "c":
            buy_crypto()
        elif repetir == "v":
            sell_crypto()
        elif repetir == "t":
            swap_crypto()
        else:
            print('Você saiu do programa! Te esperamos de  em breve.')
        break


def swap_crypto():
    choose = input(f'Selecione a moeda no qual deseja trocar: ').upper()
    choose_2 = input(f'Selecione a outra moeda no qual deseja adquirir: ').upper()
    amount_crypto = float(input(f'Digite a quantidade que deseja trocar: '))
    print(f'Você deseja trocar {choose} por {choose_2}.')

    if choose == "BITCOIN" and choose_2 == "ETHEREUM": 

        saldo_prev_btc = saldo_btc[-1]

        troca_btc_reais = float(saldo_prev_btc * BITCOIN) - (amount_crypto * TAXA_TROCA)
        taxa_paga = amount_crypto * TAXA_TROCA
        print(f'Seus Bitcoins valem R${troca_btc_reais:.2f}. Valor da taxa: R${taxa_paga:.4f}')

        troca_reais_eth = troca_btc_reais / ETHEREUM
        print(f'O total de Ethereum adquirido é de: {troca_reais_eth:.2f}.')

        saldo_prev_eth = saldo_eth

        if not saldo_prev_eth:
            print(f'Printa saldo_prev_eth {saldo_prev_eth:.4f}')
            print(f'Não têm ethereum em carteira')            
            saldo_eth.append(troca_reais_eth)
            print(f'Saldo em ethereum: {troca_reais_eth:.4f}')

            att_saldo_btc = float(saldo_prev_btc - amount_crypto)
            print(f'Seu saldo em Bitcoin é de: {att_saldo_btc:.4f}.')
            saldo_btc.append(att_saldo_btc)
        elif len(saldo_prev_eth) > 0: 
            att_saldo_eth = float(saldo_prev_eth[-1] + troca_reais_eth)
            print(f'Saldo atualizado de ethereum: {att_saldo_eth:.2f}')

            att_saldo_btc = float(saldo_prev_btc - amount_crypto)
            print(f'Seu saldo em Bitcoin é de: {att_saldo_btc:.2f}.')
            saldo_btc.append(att_saldo_btc)
        else:
            print(f'Swap btc p eth deu errado!')
    
    elif  choose == "BITCOIN" and choose_2 == "SOLANA": 

        saldo_prev_btc = saldo_btc[-1]

        troca_btc_reais = float(saldo_prev_btc * BITCOIN) - (amount_crypto * TAXA_TROCA)
        taxa_paga = amount_crypto * TAXA_TROCA
        print(f'Seus Bitcoins valem R${troca_btc_reais:.2f}. Valor da taxa: R${taxa_paga:.4f}')

        troca_reais_sol = troca_btc_reais / SOLANA
        print(f'O total de Ethereum adquirido é de: {troca_reais_sol:.2f}.')

        saldo_prev_sol = saldo_sol

        if not saldo_prev_sol:
            print(f'Printa saldo_prev_sol {saldo_prev_sol:.4f}')
            print(f'Não têm ethereum em carteira')            
            saldo_sol.append(troca_reais_sol)
            print(f'Saldo em Solana: {troca_reais_sol:.4f}')

            att_saldo_btc = float(saldo_prev_btc - amount_crypto)
            print(f'Seu saldo em Bitcoin é de: {att_saldo_btc:.4f}.')
            saldo_btc.append(att_saldo_btc)
        elif len(saldo_prev_sol) > 0: 
            att_saldo_sol = float(saldo_prev_sol[-1] + troca_reais_sol)
            print(f'Saldo atualizado de solana: {att_saldo_sol:.2f}')

            att_saldo_btc = float(saldo_prev_btc - amount_crypto)
            print(f'Seu saldo em Bitcoin é de: {att_saldo_btc:.2f}.')
            saldo_btc.append(att_saldo_btc)
        else:
            print(f'Swap btc p sol deu errado!')
    
    elif  choose == "BITCOIN" and choose_2 == "TIA": 

        saldo_prev_btc = saldo_btc[-1]

        troca_btc_reais = float(saldo_prev_btc * BITCOIN) - (amount_crypto * TAXA_TROCA)
        taxa_paga = amount_crypto * TAXA_TROCA
        print(f'Seus Bitcoins valem R${troca_btc_reais:.2f}. Valor da taxa: R${taxa_paga:.4f}')

        troca_reais_tia = troca_btc_reais / SOLANA
        print(f'O total de Ethereum adquirido é de: {troca_reais_tia:.2f}.')

        saldo_prev_tia = saldo_tia

        if not saldo_prev_tia:
            print(f'Printa saldo_prev_sol {saldo_prev_tia:.4f}')
            print(f'Não têm ethereum em carteira')            
            saldo_tia.append(troca_reais_tia)
            print(f'Saldo em Solana: {troca_reais_tia:.4f}')

            att_saldo_btc = float(saldo_prev_btc - amount_crypto)
            print(f'Seu saldo em Bitcoin é de: {att_saldo_btc:.4f}.')
            saldo_btc.append(att_saldo_btc)
        elif len(saldo_prev_tia) > 0: 
            att_saldo_tia = float(saldo_prev_tia[-1] + troca_reais_tia)
            print(f'Saldo atualizado de solana: {att_saldo_tia:.2f}')

            att_saldo_btc = float(saldo_prev_btc - amount_crypto)
            print(f'Seu saldo em Bitcoin é de: {att_saldo_btc:.2f}.')
            saldo_btc.append(att_saldo_btc)
        else:
            print(f'Swap btc p sol deu errado!')

    elif  choose == "ETHEREUM" and choose_2 == "BITCOIN": 

        saldo_prev_eth = saldo_eth[-1]

        troca_eth_reais = float(saldo_prev_eth * ETHEREUM) - (amount_crypto * TAXA_TROCA)
        taxa_paga = amount_crypto * TAXA_TROCA
        print(f'Seus Ethereums valem R${troca_eth_reais:.2f}. Valor da taxa: R${taxa_paga:.4f}')

        troca_reais_btc = troca_eth_reais / BITCOIN
        print(f'O total de Bitcoin adquirido é de: {troca_reais_btc:.4f}.')

        saldo_prev_btc = saldo_btc

        if not saldo_prev_btc:
            print(f'Printa saldo_prev_btc {saldo_prev_btc:.4f}')
            print(f'Não têm Bitcoin em carteira')            
            saldo_btc.append(troca_reais_btc)
            print(f'Saldo em Bitcoin: {troca_reais_btc:.4f}')

            att_saldo_eth = float(saldo_prev_eth - amount_crypto)
            print(f'Seu saldo em Ethereum é de: {att_saldo_eth:.4f}.')
            saldo_eth.append(att_saldo_eth)
        elif len(saldo_prev_btc) > 0: 
            att_saldo_btc = float(saldo_prev_btc[-1] + troca_reais_btc)
            print(f'Saldo atualizado de Bitcoins: {att_saldo_btc:.4f}')

            att_saldo_eth = float(saldo_prev_eth - amount_crypto)
            print(f'Seu saldo em Ethereum é de: {att_saldo_eth:.4f}.')
            saldo_eth.append(att_saldo_eth)
        else:
            print(f'Swap btc p sol deu errado!')
    
    elif  choose == "ETHEREUM" and choose_2 == "SOLANA": 

        saldo_prev_eth = saldo_eth[-1]

        troca_eth_reais = float(saldo_prev_eth * ETHEREUM) - (amount_crypto * TAXA_TROCA)
        taxa_paga = amount_crypto * TAXA_TROCA
        print(f'Seus Ethereums valem R${troca_eth_reais:.2f}. Valor da taxa: R${taxa_paga:.4f}')

        troca_reais_sol = troca_eth_reais / SOLANA
        print(f'O total de Solanas adquiridas é de: {troca_reais_sol:.4f}.')

        saldo_prev_sol = saldo_sol

        if not saldo_prev_sol:
            print(f'Printa saldo_prev_sol {saldo_prev_sol:.4f}')
            print(f'Não têm Solana em carteira')            
            saldo_sol.append(troca_reais_sol)
            print(f'Saldo em Solana: {troca_reais_sol:.4f}')

            att_saldo_eth = float(saldo_prev_eth - amount_crypto)
            print(f'Seu saldo em Ethereum é de: {att_saldo_eth:.4f}.')
            saldo_eth.append(att_saldo_eth)

        elif len(saldo_prev_sol) > 0: 
            att_saldo_sol = float(saldo_prev_sol[-1] + troca_reais_sol)
            print(f'Saldo atualizado de Bitcoins: {att_saldo_sol:.4f}')

            att_saldo_eth = float(saldo_prev_eth - amount_crypto)
            print(f'Seu saldo em Ethereum é de: {att_saldo_eth:.4f}.')
            saldo_eth.append(att_saldo_eth)
        else:
            print(f'Swap btc p sol deu errado!')

    elif  choose == "ETHEREUM" and choose_2 == "TIA": 

        saldo_prev_eth = saldo_eth[-1]

        troca_eth_reais = float(saldo_prev_eth * ETHEREUM) - (amount_crypto * TAXA_TROCA)
        taxa_paga = amount_crypto * TAXA_TROCA
        print(f'Seus Ethereums valem R${troca_eth_reais:.2f}. Valor da taxa: R${taxa_paga:.4f}')

        troca_reais_tia = troca_eth_reais / TIA
        print(f'O total de Solanas adquiridas é de: {troca_reais_tia:.4f}.')

        saldo_prev_tia = saldo_tia

        if not saldo_prev_tia:
            print(f'Printa saldo_prev_sol {saldo_prev_tia:.4f}')
            print(f'Não têm Solana em carteira')            
            saldo_tia.append(troca_reais_tia)
            print(f'Saldo em Tia: {troca_reais_tia:.4f}')

            att_saldo_eth = float(saldo_prev_eth - amount_crypto)
            print(f'Seu saldo em Ethereum é de: {att_saldo_eth:.4f}.')
            saldo_eth.append(att_saldo_eth)

        elif len(saldo_prev_tia) > 0: 
            att_saldo_tia = float(saldo_prev_tia[-1] + troca_reais_tia)
            print(f'Saldo atualizado de Bitcoins: {att_saldo_sol:.4f}')

            att_saldo_eth = float(saldo_prev_eth - amount_crypto)
            print(f'Seu saldo em Ethereum é de: {att_saldo_eth:.4f}.')
            saldo_eth.append(att_saldo_eth)
        else:
            print(f'Swap btc p sol deu errado!')

    elif  choose == "SOLANA" and choose_2 == "BITCOIN": 

        saldo_prev_sol = saldo_sol[-1]

        troca_sol_reais = float(saldo_prev_sol * SOLANA) - (amount_crypto * TAXA_TROCA)
        taxa_paga = amount_crypto * TAXA_TROCA
        print(f'Seus Ethereums valem R${troca_sol_reais:.2f}. Valor da taxa: R${taxa_paga:.4f}')

        troca_reais_btc = troca_sol_reais / BITCOIN
        print(f'O total de Bitcoins adquiridos é de: {troca_reais_btc:.4f}.')

        saldo_prev_btc = saldo_btc

        if not saldo_prev_btc:
            print(f'Printa saldo_prev_btc {saldo_prev_btc:.4f}')
            print(f'Não têm Bitcoin em carteira')            
            saldo_btc.append(troca_reais_btc)
            print(f'Saldo em Bitcoin: {troca_reais_btc:.4f}')

            att_saldo_sol = float(saldo_prev_sol - amount_crypto)
            print(f'Seu saldo em Solana é de: {att_saldo_sol:.4f}.')
            saldo_sol.append(att_saldo_sol)

        elif len(saldo_prev_btc) > 0: 
            att_saldo_btc = float(saldo_prev_btc[-1] + troca_reais_btc)
            print(f'Saldo atualizado de Bitcoins: {att_saldo_btc:.4f}')

            att_saldo_sol = float(saldo_prev_sol - amount_crypto)
            print(f'Seu saldo em Solana é de: {att_saldo_sol:.4f}.')
            saldo_sol.append(att_saldo_sol)
        else:
            print(f'Swap sol p btc deu errado!')

    elif  choose == "SOLANA" and choose_2 == "ETHEREUM": 

        saldo_prev_sol = saldo_sol[-1]

        troca_sol_reais = float(saldo_prev_sol * SOLANA) - (amount_crypto * TAXA_TROCA)
        taxa_paga = amount_crypto * TAXA_TROCA
        print(f'Seus Ethereums valem R${troca_sol_reais:.2f}. Valor da taxa: R${taxa_paga:.4f}')

        troca_reais_eth = troca_sol_reais / ETHEREUM
        print(f'O total de Ethereum adquiridos é de: {troca_reais_eth:.4f}.')

        saldo_prev_eth = saldo_eth

        if not saldo_prev_eth:
            print(f'Printa saldo_prev_eth {saldo_prev_eth:.4f}')
            print(f'Não têm Eth em carteira')            
            saldo_eth.append(troca_reais_eth)
            print(f'Saldo em Ethereum: {troca_reais_eth:.4f}')

            att_saldo_sol = float(saldo_prev_sol - amount_crypto)
            print(f'Seu saldo em Solana é de: {att_saldo_sol:.4f}.')
            saldo_sol.append(att_saldo_sol)

        elif len(saldo_prev_eth) > 0: 
            att_saldo_eth = float(saldo_prev_eth[-1] + troca_reais_eth)
            saldo_eth.append(att_saldo_eth)
            print(f'Saldo atualizado em Ethereum: {att_saldo_eth:.4f}')

            att_saldo_sol = float(saldo_prev_sol - amount_crypto)
            print(f'Seu saldo em Solana é de: {att_saldo_sol:.4f}.')
            saldo_sol.append(att_saldo_sol)
        else:
            print(f'Swap sol p btc deu errado!')

    elif  choose == "SOLANA" and choose_2 == "TIA": 

        saldo_prev_sol = saldo_sol[-1]

        troca_sol_reais = float(saldo_prev_sol * SOLANA) - (amount_crypto * TAXA_TROCA)
        taxa_paga = amount_crypto * TAXA_TROCA
        print(f'Seus Ethereums valem R${troca_sol_reais:.2f}. Valor da taxa: R${taxa_paga:.4f}')

        troca_reais_tia = troca_sol_reais / TIA
        print(f'O total de Tia adquiridas é de: {troca_reais_tia:.4f}.')

        saldo_prev_tia = saldo_tia

        if not saldo_prev_tia:
            print(f'Printa saldo_prev_tia {saldo_prev_tia:.4f}')
            print(f'Não têm Tia em carteira')            
            saldo_tia.append(troca_reais_tia)
            print(f'Saldo em Tia: {troca_reais_tia:.4f}')

            att_saldo_sol = float(saldo_prev_sol - amount_crypto)
            print(f'Seu saldo em Solana é de: {att_saldo_sol:.4f}.')
            saldo_sol.append(att_saldo_sol)

        elif len(saldo_prev_tia) > 0: 
            att_saldo_tia = float(saldo_prev_tia[-1] + troca_reais_tia)
            saldo_tia.append(att_saldo_tia)
            print(f'Saldo atualizado de Tia: {att_saldo_tia:.4f}')

            att_saldo_sol = float(saldo_prev_sol - amount_crypto)
            print(f'Seu saldo em Solana é de: {att_saldo_sol:.4f}.')
            saldo_sol.append(att_saldo_sol)
        else:
            print(f'Swap sol p btc deu errado!')

    
    elif  choose == "TIA" and choose_2 == "BITCOIN": 

        saldo_prev_tia = saldo_tia[-1]

        troca_tia_reais = float(saldo_prev_tia * TIA) - (amount_crypto * TAXA_TROCA)
        taxa_paga = amount_crypto * TAXA_TROCA
        print(f'Suas Tias valem R${troca_tia_reais:.2f}. Valor da taxa: R${taxa_paga:.4f}')

        troca_reais_btc = troca_tia_reais / BITCOIN
        print(f'O total de Tia adquiridas é de: {troca_reais_btc:.4f}.')

        saldo_prev_btc = saldo_btc

        if not saldo_prev_btc:
            print(f'Printa saldo_prev_tia {saldo_prev_btc:.4f}')
            print(f'Não têm Bitcoin em carteira')            
            saldo_btc.append(troca_reais_btc)
            print(f'Saldo em Bitcoin: {troca_reais_btc:.4f}')

            att_saldo_tia = float(saldo_prev_tia - amount_crypto)
            print(f'Seu saldo em Tia é de: {att_saldo_tia:.4f}.')
            saldo_tia.append(att_saldo_tia)

        elif len(saldo_prev_btc) > 0: 
            att_saldo_btc = float(saldo_prev_btc[-1] + troca_reais_btc)
            saldo_btc.append(att_saldo_btc)
            print(f'Saldo atualizado de Bitcoin: {att_saldo_btc:.4f}')

            att_saldo_tia = float(saldo_prev_tia - amount_crypto)
            print(f'Seu saldo em Tia é de: {att_saldo_tia:.4f}.')
            saldo_sol.append(att_saldo_tia)
        else:
            print(f'Swap tia p btc deu errado!')


    else:
        print('Deu errado o swap')

crypto_exchange()


'''
def add_crypto():
    add_amount = float(input(f'Digite o valor que deseja adicionar a sua carteira: '))
    saldo_att = saldoreais_previo_cliente + add_amount
    saldo_att_cliente = saldo_att
    print_saldo = input(f'O seu salto atual é de R${saldo_att_cliente}. Deseja adicionar mais saldo? Digite "add" ou Para comprar uma crypto digite "c". Para vender digite "v" ou para trocar digite "t".' )
    print(print_saldo)

    if print_saldo == "add":
        add_crypto()
    elif print_saldo == "c":
        buy_crypto()
    elif print_saldo == "v":
        sell_crypto()
    elif print_saldo == "t":
        swap_crypto()
    else:
        print('Add cripto deu errado.')
'''
