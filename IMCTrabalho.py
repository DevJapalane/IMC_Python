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


kilograma = float(input('Quantos kilos você pesa?: '))
metros = float(input('Qual sua altura?: '))

indice = kilograma/(metros**2) # Fóromula IMC
indiceredondo = round(indice, 2) # Round arredondando 2 numeros após a virgula
print('seu IMC é: ', indiceredondo) # Print do índice
