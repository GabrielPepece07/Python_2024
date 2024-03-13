#Descontos aplicados por litro em um posto de combustível 
#Primeiro passo: coletar a quantidade de litros e o tipo de combustível.
quantidade_litros = float(input('informe a quantidade de litros vendidos:'))
tipo_combustivel = input('Informe o tipo de combustivel (E para etanol e G para gasolina):')
#Em primeiro lugar é verificado o tipo do combustível
if tipo_combustivel == 'E':
    preco_litro = 1.70
    #Aplicação do desconto de acordo com a vulometria de litros Etanol
    if quantidade_litros <= 15:
        desconto = 0.02
    else:
        desconto = 0.04
elif tipo_combustivel == 'G':
    preco_litro = 2.00
    #Aplicação do desconto de acordo com a quantidade de litros Gasolina
    if  quantidade_litros <= 15:
        desconto = 0.03
    else:
        desconto = 0.05
#Caso ocorra erro ao colocar o tipo de combustível é considerado inválido a entrada e o preço é taxado 0
else:
    print('Entrada inválida')
    preço_litro = 0
    desconto = 0
# Cálculos de valor de desconto e após calculo do preço
valor_desconto = preco_litro * quantidade_litros * desconto
valor_pago = preco_litro * quantidade_litros - valor_desconto
#Saída
print(F'Valor final ao cliente: R$ {valor_pago}')
