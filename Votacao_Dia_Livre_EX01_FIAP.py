#A Bidu é uma startup na área de Fintech fundada em 2011 que ajuda os usuários a controlar suas fontes de receitas, gastos, dívidas e investimentos.  Ela precisa realizar uma votação para escolher qual dia da semana é o melhor para a realização das lives com o time da mentoria financeira. Desenvolva um programa em que os colaboradores informem um dos 5 dias da semana (segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira) da sua preferência para participar da live. Verifique e exiba ao final, qual dia foi o escolhido pelos colaboradores.
#Observação: Verifique o número de colaboradores que irão participar da votação para programar sua estrutura de repetição.
#Ponto de atenção: É importante o programa validar a possibilidade de empate. rm564257






print("Votação para o melhor dia da live de mentoria financeira")

segunda = 0
terca = 0
quarta = 0
quinta = 0
sexta = 0

quantidade = int(input("Quantos colaboradores irão votar? "))

contador = 1
while contador <= quantidade:
    print("\nOpções de dias:")
    print("1 - Segunda-feira")
    print("2 - Terça-feira")
    print("3 - Quarta-feira")
    print("4 - Quinta-feira")
    print("5 - Sexta-feira")

    voto = input(f"Colaborador {contador}, escolha um dia (digite o nome do dia): ").lower()

    if voto == "segunda-feira":
        segunda += 1
        contador += 1
    elif voto == "terça-feira" or voto == "terca-feira":
        terca += 1
        contador += 1
    elif voto == "quarta-feira":
        quarta += 1
        contador += 1
    elif voto == "quinta-feira":
        quinta += 1
        contador += 1
    elif voto == "sexta-feira":
        sexta += 1
        contador += 1
    else:
        print("Dia inválido! Tente novamente com a grafia correta.")


print("\n=== Resultado da votação ===")
print("Segunda-feira:", segunda)
print("Terça-feira:", terca)
print("Quarta-feira:", quarta)
print("Quinta-feira:", quinta)
print("Sexta-feira:", sexta)


maior = segunda
dia_vencedor = "Segunda-feira"

if terca > maior:
    maior = terca
    dia_vencedor = "Terça-feira"
elif terca == maior:
    dia_vencedor += ", Terça-feira"

if quarta > maior:
    maior = quarta
    dia_vencedor = "Quarta-feira"
elif quarta == maior and "Quarta-feira" not in dia_vencedor:
    dia_vencedor += ", Quarta-feira"

if quinta > maior:
    maior = quinta
    dia_vencedor = "Quinta-feira"
elif quinta == maior and "Quinta-feira" not in dia_vencedor:
    dia_vencedor += ", Quinta-feira"

if sexta > maior:
    maior = sexta
    dia_vencedor = "Sexta-feira"
elif sexta == maior and "Sexta-feira" not in dia_vencedor:
    dia_vencedor += ", Sexta-feira"


print("\nDia(s) mais votado(s):", dia_vencedor)
