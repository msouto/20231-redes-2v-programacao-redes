#Listas
#Listas são coleções ordenadas de objetos
#Listas podem conter quaisquer tipos de objetos
#Listas são Objetos Mutáveis (Podem ter seus elementos alterados)
#Listas têm tamanho variável, são heterogêneas e arbitrariamente aninhadas
##Pode-se adicionar ou remover elementos
##Podem conter tipos diferentes
##Podem conter outras listas como elementos (Equivalente aos arrays)

#Lista vazia
L = []
L = list()

#Lista com 4 itens
L = [4, 'abc', 1.23, [9,8,7],[1,2,3,4,5]]
print(L)

#Lista de um objeto iterável
L = list('spam')
print(L)

#Indexaçã e slide
L = [4, 'abc', 1.23]
print(L[0]) 
print(L[-2])
print(L[:2])

#Operações básicas com listas
L = [4, 'abc', 1.23]
M = ['fgh', 5.6, 10, 145]

print(len(L))
print(len(M))

print(L+M) #concatenando listas
print(len(L+M))

#repetição de elementos
print(3*L)

#Iteração e associação
L = [4, 'abc', 1.23]
print('abc' in L)

#iterando sobre a lista
for x in L:
    print(x)

#List comprehensions
#Recurso para criação de listas por iteração a outro objeto

res = [i*4 for i in 'abc']
print(res)