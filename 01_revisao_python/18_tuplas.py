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

#por que Tuplas?

""" A semelhança com listas é evidente
Por que existe Tuplas se Listas têm mais funcionalidades?
Tuplas  é um termo originado da Matemática e portanto foi pensada com esse objetivo
Tuplas são imutáveis e, portanto, mantém integridade dos objetos
Podem ser usadas aonde listas não podem: 
Chaves de Dicionários
Algumas built-in exigem o uso de Tuplas """

#indexação e slide
T = (10, 3.56, 200, 'casa')
print(T[0])
print(T[-1]) #ultimo elemento

print(T[1:3]) #range de elementos

print(T[2:])

#Operações básicas com tuplas
print((1,2)+(3,4))

print((1,2)*3)

#Iteração e associação
T = (10,20,30)

print(10 in T)

for x in T:
    print(x)

#Tuple comprehensions
#é um recurso para criação de tuplas por iteração a outro objeto

a = 'ifrn'
res = tuple(c*2 for c in a)
print(res)

#Peculariedade
# O uso dos paranteses da tupla pode confundir

x=(10) #o inteiro 10
print(x)
print(type(x))
y=(10,) #a tupla com um elemento inteiro
print(y)
print(type(y))


#Conversão
# Por exemplo, como as Tuplas são imutáveis, para ordena-las, é necessário converter para lista.

T = ('c','a','x','r')

#Converter para lista
tmp = list(T)
print(type(tmp))
print(tmp)
tmp.sort()
print(tmp)

#Converter para tupla
T = tuple(tmp)
print(type(T))
print(T)


#métodos 
T = (1,2,3,2,5,2)

#offset do primeiro elemento com valor 2
print(T.index(2))

#o próximo indice com valor 2 após o indice 2
print(T.index(2,2))

#Quantas vezes o valor 2 aparece
print(T.count(2))
