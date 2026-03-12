"""
Exercício 6:
Pedir o valor do produto
guardar o valor na variavel "valor1"
pedir a quantidade comprada
guardar o valor na variavel "quantidade1"
total=(valor1*0.85)*quantidade1
mostrar o "total" com desconto de 15%
"""

valor = float(input('Informe o valor do produto (00.00): '))
quantidade = int(input('Informe a quantidade comprada: '))

#enquanto % estiver presente na var desconto, ele volta o valor True e continua com o programa
while True:
    desconto = input('Informe o desconto (00%): ')
    if "%" in desconto:
        porcentagem = float(desconto[:-1]) / 100
#se o calculo de porcentagem for maior que um ele vai execultar a mensagem até estar certo
        if porcentagem > 1:
            print("desconto errado kkkkkkkkkk")
        else:
            break
#caso contrario ele vai execultar essa mensagem
    else:
        print("Colocar '%' junto do valor.")

total = (valor - (valor * porcentagem)) * quantidade
# .2f é pra mostrar só duas casas decimais
print(f'O valor total da compra é: R${total:.2f}')