print("Teste de formatação de strings")
myInteger = 12345
myFloat = 3.14159

myString = "curso de python"
print("Inteiro: ", myInteger)# Inteiro: valor variável

print("Decimal %d e um Inteiro %d" %(myInteger, myInteger)) #permaneceu o mesmo valor

print("Inteiro hexadecimal %x" %myInteger) #hexadecimal da variável inteiro     %x

print("Real", myFloat) #Real, valor variável

print("Default %f" %myFloat) #adicionou uma casa decimal

print("Exponencial %e" % myFloat) #Exponencial 3.141590e+00     %e

print("Justificar direita (%10d)" % myFloat) #formatação 10% direita e arredondamento pra baixo     %10d

print("Justificar a esquerda (%-10d)" % myFloat) #formatação 10% esquerda e arredondamento pra baixo    %-10d

print("For ar 9 digitos %.9d" % myInteger) # adiciona 0 esquerda

print("3 digitos depois do decimal (float) %.3f" %myFloat) #arredonda com 3 casas decimais

print("(%.10s) (%.5s)" % (myString, myString)) #formatando as strings para 10caracteres e 5caracteres
