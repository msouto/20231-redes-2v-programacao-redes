#conversão entre string e lista

#String
s = 'python'
print(s)
print(type(s))

#Instanciando e criando uma lista
L = list(s)
print(L)
print(type(L))

print(L[0])

L[0] = 'r' #Lista são mutáveis
print(L[0])
print(L)

#Conversão de uma lista em string
w = ''.join(L) 
print(w)

#Com o uso do método split é possível usar padrões de separação de strings para transformá-la em uma lista
s = 'joao,paulo,pedro,marco'
L = s.split(',')
print(L)
