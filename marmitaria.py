print("Gil Marmitas agradece seu contato!")
nome = input("Qual o seu nome?")
print("Olá", nome, "! Bem vindo a Gil Marmitas!")

marmitas = "Churrasco, Frango, Lasanha, Panqueca, Strogonoff de Frango, Contra-Filé Acebolado, Almôndegas"

print("Consulte nosso cardápio e valores : ", marmitas)

pedido = input("Qual é o seu pedido?")

while pedido not in marmitas:
    pedido = input(
        " Selecione uma opcao válida: Churrasco, Frango, Lasanha, Panqueca, Strogonoff de Frango, Contra-Filé Acebolado, Almôndegas"
    )
if (pedido) == "Churrasco":
    print("Acompanha Fraldinha Frango e Linguiça assados")
elif (pedido) == "Frango":
    frango = input("Temos Frango Empanado e Frango Grelhado")
elif (pedido) == "Lasanha":
    print("Acompanha Queijo ")
elif (pedido) == "Panqueca":
    print("Acompanha Molho")
elif (pedido) == "Strogonoff de Frango":
    print("Acompanha Queijo")
elif (pedido) == "Contra-Filé Acebolado":
    print("Acompanha cebola e batata frita")
elif (pedido) == "Almôndegas":
    print("Acompanha Molho")

else:
    print("Não existe essa opção")

if (pedido) == "Churrasco":
    print("Marmita Pequena de Churrasco = $18,00 / Marmita Média de Churrasco = $22,00")
elif (pedido) == "Frango":
    print("Marmita Pequena de Frango = $16,00/ Marmita Média de Frango = $18,00")
elif (pedido) == "Lasanha":
    print("Marmita Pequena de Lasanha = $15,00/ Marmita Média de Lasanha = $17,00")
elif (pedido) == "Panqueca":
    print("Marmita Pequena de Panqueca = $15,00/ Marmita Média de Panqueca = $17,00")
elif (pedido) == "Strogonoff de Frango":
    print(
        "Marmita Pequena de Strogonoff = $18,00/ Marmita Média de Strogonoff = $22,00"
    )
elif (pedido) == "Contra-Filé Acebolado":
    print(
        "Marmita Pequena de Contra-Filé = $18,00/ Marmita Média de Contra-Filé = $22,00"
    )
elif (pedido) == "Almôndegas":
    print(
        "Marmita Pequena de Almôndegas = $15,00/ Marmita Média de Almôndegas = $17,00"
    )

tamanho = input("Gostaria do tamanho P ou M?")

n1 = input("Quantas marmitas?")

print("Aceitamos dinheiro, debito e credito como forma de pagamento")
pagamento = input("Qual a forma de pagamento?")

endereço = input("Qual seu endereço para entrega?")

if (pagamento) == "Dinheiro":
    print(
        "Confirma seu pedido de",
        pedido,
        "no tamanho",
        tamanho,
        "com pagamento em",
        pagamento,
        "no endereço",
        endereço,
    )
elif (pagamento) == "Debito":
    print(
        "Confirma seu pedido de",
        pedido,
        "no tamanho",
        tamanho,
        "com pagamento em",
        pagamento,
        "no endereço",
        endereço,
    )
elif (pagamento) == "Credito":
    print(
        "Confirma seu pedido de",
        pedido,
        "no tamanho",
        tamanho,
        "com pagamento em",
        pagamento,
        "no endereço",
        endereço,
    )

print(
    "Seu pedido foi confirmado e ficou no total de ",
)
