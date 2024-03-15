#Código de solicitação do número ao usuario
num = int(input('Informe um número inteiro de 1 a 10:'))
#Código para gerar a tabuada
print(f'Tabuada do {num}:')
for i in range (1, 11):
    resultado = num * i
    print(f'{num} x {i} = {resultado}')