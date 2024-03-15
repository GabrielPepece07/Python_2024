#Temos os seguintes dados referentes aos gastos de um cartão.
gastos = [2172.54, 3702.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

#Para encontrar a média é necessário definir os parâmetros  dos dados a sem dividos
#Será usado sum() para realizar a soma de todas os itens e o len() para contar quantos itens.

total_gastos = sum(gastos)
quantidade_compras = len(gastos)
#feito isso é tirado a média entre todos os valores
media_gastos = total_gastos / quantidade_compras
#Saída
print(f"A média de gastos foi de R$ {media_gastos}.")