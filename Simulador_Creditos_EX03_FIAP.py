#Na oferta de um produto de crédito aos clientes, três informações são muito importantes apresentar ao cliente: valor da dívida, a taxa de juros e o número de parcelas para pagamento do empréstimo contraído junto à Fintech. Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados:
#Valor da dívida, valor do juros, quantidade de parcelas e valor da parcela.
#Observação: Na saída do programa, utilize estrutura de repetição para apresentar a listagem, conforme o modelo acima.


print("=== Simulador de Crédito - Fintech ===")


valor_divida = float(input("Digite o valor da dívida: R$ "))


parcelas = 1

print("\nTabela de pagamento:")
print("Parcelas | Juros (%) | Valor Juros | Valor Total | Valor da Parcela")

while parcelas <= 12:
    if parcelas == 1:
        juros = 0
    elif parcelas == 3:
        juros = 10
    elif parcelas == 6:
        juros = 15
    elif parcelas == 9:
        juros = 20
    elif parcelas == 12:
        juros = 25
    else:
        parcelas += 1
        continue  

    valor_juros = valor_divida * (juros / 100)
    valor_total = valor_divida + valor_juros
    valor_parcela = valor_total / parcelas

    print("{:^9} | {:^10} | R$ {:>10.2f} | R$ {:>10.2f} | R$ {:>10.2f}".format(
        parcelas, juros, valor_juros, valor_total, valor_parcela
    ))

    parcelas += 1
