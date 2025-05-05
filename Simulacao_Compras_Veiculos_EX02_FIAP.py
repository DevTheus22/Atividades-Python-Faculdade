#A compra de um veículo pode ser realizada parcelada. Crie um programa que receba o valor de um carro e mostre uma tabela com os seguintes dados: preço final, quantidade de parcelas e valor da parcela. Considere o seguinte:
#a) O preço final para compra à vista tem um desconto de 20%.
#b) A quantidade de parcelas pode ser 6, 12, 18, 24, 30, 36, 42, 48, 54 e 60.

print("=== Simulação de compra de veículo ===")


valor_carro = float(input("Digite o valor do carro: R$ "))


valor_avista = valor_carro * 0.8
print("\nCompra à vista:")
print("Desconto de 20% aplicado.")
print("Preço final: R$ {:.2f}".format(valor_avista))


parcelas = 6

print("\nCompra parcelada:")
print("Parcelas | Acréscimo | Preço final | Valor da parcela")

while parcelas <= 60:
    if parcelas == 6:
        acrescimo = 0.03
    elif parcelas == 12:
        acrescimo = 0.06
    elif parcelas == 18:
        acrescimo = 0.09
    elif parcelas == 24:
        acrescimo = 0.12
    elif parcelas == 30:
        acrescimo = 0.15
    elif parcelas == 36:
        acrescimo = 0.18
    elif parcelas == 42:
        acrescimo = 0.21
    elif parcelas == 48:
        acrescimo = 0.24
    elif parcelas == 54:
        acrescimo = 0.27
    elif parcelas == 60:
        acrescimo = 0.30

    preco_final = valor_carro * (1 + acrescimo)
    valor_parcela = preco_final / parcelas

    print("{:>8} | {:>9}% | R$ {:>10.2f} | R$ {:>10.2f}".format(
        parcelas, int(acrescimo * 100), preco_final, valor_parcela
    ))

    parcelas += 6
