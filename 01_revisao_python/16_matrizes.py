M = [ [1,2,3], [4,5,6], [7,8,9] ]
print(M)

print(M[0][0])

V = [x[1] for x in M]
print(V)

#alterações nessa lista
L = [1,5,6]
print(L)
L[1] = 9
print(L)

#alteração de listas utilizando indexação e slides
L = [1,5,6]
print(L)
#antes: [1,5,6]

#desejado: [1,9,10,5,6]
L[1:1] = [9,10]
print(L)

#desejado: [1,10,5,6]
L[1:2] = []
print(L)

#alterações com métodos
L = [1,5,6]
print(L)

#adicionando elemento
L.append(9)
print(L)

#removendo elemento
L.pop()
print(L)

#adicionar vários itens ao final
L = [1,5,6]
print(L)

L.extend([10,11])
print(L)

#remove elemento por posição
L.pop(3)
print(L)

#outros métodos de alteração
L = [1,9,6,5,2]
print(L)

#inverter a ordem da lista
L.reverse()
print(L)

#remover por conteúdo
L.remove(6)
print(L)

#ordenar a lista
L.sort()
print(L)
