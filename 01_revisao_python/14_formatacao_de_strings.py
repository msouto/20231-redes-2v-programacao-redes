nome = 'joao'

print(f'a casa de {nome} fica em natal')
print('a casa de %s fica em natal' % nome)

#A sintaxe completa da expressão é:
#%[(nomedachave)] [flags] [tamanho] [.precisão] código
#Aonde:
#(nome da chave) - Caso se utilize dicionários para os valores
#   flags - Especifica alguns aspectos, tais como, justificação (-), sinais numéricos (+), números positivos sem sinal e negativos com sinal (espaço), preenchimento com zeros
#   tamanho - Tamanho minimo do texto substituído
#   precisão - Para ponto flutuante, o número de casas decimais
#   Código - Código que representa o tipo de dado a ser substituído

#formatação de strings - códigos mais comuns
#Código	Significado
#s	String
#d	decimal
#i	inteiro
#x	hexadecimal
#e	Ponto flutuante com expoente
#f	Ponto flutuante

x = 1234
print('inteiros: ... %d ... %-6d ... %06d' % (x, x, x))


x = 1.23456789
print('%-6.2f | %05.2f | %+06.2f' % (x, x, x))