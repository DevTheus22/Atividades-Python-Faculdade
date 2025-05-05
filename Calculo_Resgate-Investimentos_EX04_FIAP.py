#Toda vez que um cliente realiza um resgate de uma aplicação financeira, o sistema deve calcular a alíquota de imposto de renda (IR) que deve ser aplicada sobre aquele resgate, levando em consideração o número de dias que o valor permaneceu aplicado
#Até 180 dias = alíquota de 22,5% de IR.
#De 181 a 360 dias = alíquota de 20% de IR.
#De 361 a 720 dias = alíquota de 17,5% de IR.
#Acima de 720 dias = alíquota de 15% de IR.
#É o que acontece, por exemplo, com o Certificado de Depósito Bancário (CDB), uma aplicação de renda fixa comumente oferecida pelas Fintechs. Outros investimentos em renda fixa, como LCI e LCA, respectivamente, Letra de Crédito #Imobiliário e Letra de Crédito do Agronegócio são isentos de imposto de renda. Escreva um programa que receba o tipo de investimento do qual se deseja realizar um resgate (1 para CDB, 2 para LCI e 3 para LCA), o valor a ser resgatado e o #número de dias que esse valor permaneceu investido e, se for o caso, calcule o valor referente ao imposto de renda.
#Atenção! O programa deve consistir se o investimento fornecido é válido, ou seja, 1, 2 o 3.


print("=== Cálculo de Imposto de Renda sobre Resgate de Investimentos ===")

print("Tipos de investimento:")
print("1 - CDB")
print("2 - LCI")
print("3 - LCA")


while True:
    tipo = int(input("Digite o tipo de investimento (1, 2 ou 3): "))
    if tipo == 1 or tipo == 2 or tipo == 3:
        break
    else:
        print("Tipo inválido. Por favor, digite 1, 2 ou 3.")


valor_resgate = float(input("Digite o valor a ser resgatado: R$ "))
dias = int(input("Digite o número de dias que o valor permaneceu investido: "))


if tipo == 1:
    # CDB é tributado conforme o tempo
    if dias <= 180:
        aliquota = 0.225
    elif dias <= 360:
        aliquota = 0.20
    elif dias <= 720:
        aliquota = 0.175
    else:
        aliquota = 0.15

    imposto = valor_resgate * aliquota
    valor_liquido = valor_resgate - imposto

    print("\n=== Resumo do Resgate ===")
    print("Tipo de investimento: CDB")
    print("Dias aplicados:", dias)
    print("Alíquota de IR aplicada: {:.1f}%".format(aliquota * 100))
    print("Valor do imposto: R$ {:.2f}".format(imposto))
    print("Valor líquido a receber: R$ {:.2f}".format(valor_liquido))

else:
    # LCI e LCA são isentos
    print("\n=== Resumo do Resgate ===")
    if tipo == 2:
        print("Tipo de investimento: LCI")
    else:
        print("Tipo de investimento: LCA")

    print("Dias aplicados:", dias)
    print("Este tipo de investimento é isento de Imposto de Renda.")
    print("Valor a receber: R$ {:.2f}".format(valor_resgate))
