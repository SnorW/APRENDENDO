print('Irei pedir seu peso e altura para calcular o IMC!')
peso = float(input('Qual o seu peso?'))
altura = float(input('Qual a sua altura?'))

imc = peso / (altura * altura)

print('Com o peso de {:.2f}kg e a altura de {:.2f}m seu IMC é de {:.1f}'.format(peso, altura, imc))

if imc < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 <= imc <= 25:
    print('Você está no peso ideal!')
elif 25 < imc <= 30:
    print('Você está no sobrepeso!!')
elif 30 < imc <= 40:
    print('Você está com obesidade!!')
elif 40 < imc:
    print('Você está com obesidade morbida!!')
