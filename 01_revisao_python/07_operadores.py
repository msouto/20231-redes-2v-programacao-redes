#operadores
#Precedência de operadores
#a * b + c * d  
# Consultar tabela de precedência em: https://docs.python.org/3/reference/
# /expressions.html?highlight=precedence#operator-precedence 

#Agrupamento por parênteses
#(x + y) * z   # Parênteses alteram precedência
#x + (y * z)


#Mistura de Tipos
print(40 + 3.14)   # Conversão para float antes da operação
print(40 + int(3.14)) # Conversão explícita

#diferença entre conversão para int e arredondamento
print(int(3.77))
print(round(3.77))