#Formatação de números
#A formatação de um número, pode ser feito da seguinte forma:
num = 1/3.0 #atribuição de valor na variável num, da divão de 1 por 3
print(num)

#notação de manipulação de engenharia
print("%e" % num)

#formatando a saída, para conter 4 dígitos no total, contendo 2 números após a casa decimal
print("%4.2f" % num)

#Formatando a saída, para conter 6 dígitos no total, contendo 2 números após a casa decimal, e preenchendo com zero os valores a esquerda
print("%06.2f" % num)
