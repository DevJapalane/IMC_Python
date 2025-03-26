# IMC FORMULA
# IMC = Peso / Altura² 
# Altura² = Altura x Altura

# Indices:
# IMC (kg/m²):                   Classificação:

# Menor que 16,9              Muito abaixo do peso.
# 17,0 a 18,4                 Abaixo do peso.
# 18,5 a 24,9                 Peso normal.
# 25,0 a 29,9                 Acima do peso.
# 30,0 a 34,9                 Obesidade Grau I.
# 35,0 a 40,0                 Obesidade Grau II.
# Maior que 40,0              Obesidade Grau III.

def ifelse(indiceretornado):
    if indiceretornado in id1:
        return print('Muito abaixo do peso.')
    elif indiceretornado in id2:
        return print("Abaixo do peso.")
    elif indiceretornado in id3:
        return print("Peso normal.")
    elif indiceretornado in id4:
        return print("Acima do peso.")
    elif indiceretornado in id5:
        return print("Obesidade Grau I.")
    elif indiceretornado in id6:
        return print("Obesidade Grau II.")
    elif indiceretornado in id7:
        return print("Obesidade Grau III.")
    else:
        return print("ERRO!")

def indice(kilograma, metros):
    return round(kilograma/(metros**2))

id1 = list(range(0, 17))
id2 = list(range(18, 19))
id3 = list(range(20, 25))
id4 = list(range(26, 30))
id5 = list(range(31, 35))
id6 = list(range(36, 40))
id7 = list(range(51, 101))

kilograma = float(input('Quantos kilos você pesa?: '))
metros = float(input('Qual sua altura?: '))
indiceretornado = indice(kilograma, metros)

print('seu IMC é: ', indiceretornado)

classificaçãoretornada = ifelse(indiceretornado)

# Em input insira os números decimais com "." (ponto) e não virgula, Exemplo:
# Quantos kilos você pesa?: 1.75
