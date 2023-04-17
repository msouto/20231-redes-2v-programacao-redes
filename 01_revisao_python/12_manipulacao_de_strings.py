#String são objetos utilizados para representar qualquer coisa que possa ser codificada como texto ou sequencia de bytes

#Em Python, Strings são denominadas de “Sequências imutáveis”

#Sequência porque trata-se de uma sequencia de caracteres

#Imutável porque, uma vez criado, o objeto do tipo string não pode ser alterado 

#Ex: 
s = "casa" 
x = ""

print(s)
print(x)

#Cota simples(simple-quoted) ou cota dupla (double-quoted)
#Um objeto do tipo string pode ser criado com cota simples ou dupla. A diferença é apenas se dentro da string precisamos representar o caractere de cota simples (‘) ou de cota dupla (“)

#Ex: 
w = "D'agua" 
print(w)
z = 'knight”s'  
print(z)

#É possível utilizar o mesmo tipo de cota, contudo deve-se usar o recurso de “Escapar” (Escape) os caracteres de cota dentro da string
#Ex:
w = 'D\'agua' 
z = "knight\"s"
print(w)
print(z)

#Representação de sequências de Escape

#O recurso de escapar caracteres serve também para incluir dentro de strings caracteres que não tem representação direta no teclado 
s = 'a\nb\nc\vd\ve\vf\t\rg\th\ti'       # A sequencia \n significa Enter ou quebra de linha 
print(s)
print(len(s))

#Alguns caracteres de strings especiais
#Escape	ASCII character
#\n	Newline
#\r	Carriage return
#\t	Horizontal tab
#\v	Vertical tab



#Raw Strings (cruas, sem tratamento)

#Pode ser mais conveniente, quando trabalhando com escape, usar um formato de strings do tipo raw.

#Raw string é criado com o caractere (r) antes da string

#Ex:  Caso precisemos criar uma string para um caminho
s = 'c:\novo\texto.txt'
print(s)

 
w = 'c:\\novo\\texto.txt'  
print(w)
z = r'c:\novo\texto.txt' 
print(z)


#Cota tripla

#Por conveniência, podemos criar string que ocupam mais de uma linha usando as cotas triplas

s = ''' Sempre olhe
...    pelo lado
... bom da vida '''
print(s)
print(len(s))


# Operações básicas com strings
s = 'casa'
print(len(s))

#Concatenação e repetição
s = 'agua' + 'salgada' 
print(s)

s = 'abc' 
print(4*s)


#iterações em uma string

#É possível usar um laço for para iterar sobre os elementos da string

s = 'python' 
print(s)
for i in s:
  print(i, end=' ')


print('t' in s)
print('z' in s)

#indexação e slice (recorte)
s = 'python\n\r'
print(s[0])
print(s[-1])
print(s[0:2])
print(s[0:-2])

#Os elementos iniciam com índice ‘0'

#Elementos negativos representam a ordem da direita pra esquerda, iniciando com o último elemento sendo ‘-1’

#No slice, o limite inferior é inclusivo e o limite superior é não-inclusivo

#Existe o terceiro parâmetro no slice que representa o passo que, por padrão é 1. Por exemplo, X[i:j:k], 
                # i representa o limite inferior, 
                # j representa o limite superior e 
                # k representa o passo.

s = 'abcdefghijklmnop'
print(s[1:10:2]) #alterando o passo padrão do slice

print(s[::2]) #alterei o passo para 2, incluindo toda a sequência da string

s = 'hello'
print(s[::-1]) #invertendo a sequência

#conversão de strings

#Para utilizar uma string em uma operação matemática é preciso convertê-la antes
s = '42' 
#x = s + 5
#print(x) #Erro, ao tentar concatenar tipos diferentes

x = int(s) + 5    # Soma aritmética
print(x)

x = s + str(5)    # Concatenação
print(x)
