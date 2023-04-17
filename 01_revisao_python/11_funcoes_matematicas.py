#Funções matemáticas 

#O Python tem módulos built-in com importantes funções matemáticas:
import math
print(math.sin(2*math.pi/180))  # trigonometria

math.sqrt(144)           # raiz quadrada

print(math.floor(2.743)) 
print(math.trunc(2.743,)) # arredonda ou trunca
print(round(2.74,2))


#Utilizando métodos aleatórios
import random
random.random()    # gera um número randomico entre 0 e 1
escolha = random.choice(["azul", "amarelo", "preto", "branco"])  
print(escolha)