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

w = ''.join(L) #Conversão de uma lista em string
print(w)