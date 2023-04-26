#tuplas
""" Tuplas são coleções ordenadas de objetos
Tuplas têm algumas similaridades com listas, porém, com menos métodos disponíveis.
Tuplas são Objetos Imutáveis (Não podem ter seus elementos alterados)
Tuplas têm tamanho fixo, são heterogêneas e arbitrariamente aninhadas
Podem conter tipos diferentes
Podem conter outras listas como elementos (Equivalente aos arrays) """

#tupla vazia
T = ()

T = tuple()

#Tupla com itens
T = (4,)

print(T)

T = (4,'abc',1.23,(9,8,7))
print(T)

T = 10,20 
print(T)
print(type(T))

#Tupla a partir de um objeto iterável
T = ('spam')
print(T)

T = tuple(range(0,10))
print(T)