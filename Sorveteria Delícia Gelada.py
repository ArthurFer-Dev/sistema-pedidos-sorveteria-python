# ==============================================
# Sistema de Pedidos - Sorvete Delícia Gelada
# Primeira Entrega - Paradigmas de Linguagem de Programação
# Professor: Aluízio Santos
# ==============================================

# ----- Constantes -----
NOME_LOJA = "Sorveteria Delícia Gelada"

# Tabela de preços
PRECO_SABORES = {
    "chocolate": 6.00,
    "morango": 6.00,
    "baunilha": 5.00,
    "flocos": 6.50
}

PRECO_ACOMPANHAMENTOS = {
    "calda de chocolate": 2.00,
    "granulado colorido": 1.50,
    "paçoca": 2.50
}

PRECO_EMBALAGEM = {
    "copo": 1.00,
    "casquinha": 2.00
}

# ----- Boas-vindas -----
print("=" * 45)
print(f"Bem-vindo(a) à {NOME_LOJA}!")
print("=" * 45)

# ----- Menu -----
print("\nSabores disponíveis:")
for sabor, preco in PRECO_SABORES.items():
    print(f" - {sabor.title()} : R$ {preco:.2f}")

print("\nAcompanhamentos:")
for acomp, preco in PRECO_ACOMPANHAMENTOS.items():
    print(f" - {acomp.title()} : R$ {preco:.2f}")

print("\nTipos de embalagem:")
for emb, preco in PRECO_EMBALAGEM.items():
    print(f" - {emb.title()} : R$ {preco:.2f}")

# ----- Captura das escolhas -----
sabor = input("\nDigite o sabor escolhido: ").strip().lower()
acomp = input("Digite o acompanhamento desejado: ").strip().lower()
embalagem = input("Digite o tipo de embalagem: ").strip().lower()

# ----- Validação simples -----
if sabor not in PRECO_SABORES:
    print("Sabor inválido! Usando 'baunilha' como padrão.")
    sabor = "baunilha"

if acomp not in PRECO_ACOMPANHAMENTOS:
    print("Acompanhamento inválido! Usando 'granulado colorido' como padrão.")
    acomp = "granulado colorido"

if embalagem not in PRECO_EMBALAGEM:
    print("Embalagem inválida! Usando 'copo' como padrão.")
    embalagem = "copo"

# ----- Cálculo do preço -----
preco_total = PRECO_SABORES[sabor] + PRECO_ACOMPANHAMENTOS[acomp] + PRECO_EMBALAGEM[embalagem]

# Promoção exemplo: se o sabor for chocolate e o acompanhamento for calda, ganha 10% de desconto
if sabor == "chocolate" and acomp == "calda de chocolate":
    desconto = preco_total * 0.10
    preco_total -= desconto
    print("\nPromoção aplicada: 10% de desconto no combo Chocolate + Calda!")

# ----- Exibição do resultado -----
print("\n===== RESUMO DO PEDIDO =====")
print(f"Sabor: {sabor.title()}")
print(f"Acompanhamento: {acomp.title()}")
print(f"Embalagem: {embalagem.title()}")
print(f"Total a pagar: R$ {preco_total:.2f}")
print("===============================")
print("Obrigado pela preferência!")
