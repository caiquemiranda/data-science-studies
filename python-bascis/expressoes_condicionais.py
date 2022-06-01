# variaveis
a = 'Dentro do if'
b = 'Fora do if'


# True
# se(verdade):
#     execute o bloco de codigo
# senao:
#     execute o bloco de codigo

# ======================================================
# True:

if( 2==2 ):
    print(a)
else:
    print(b)

# ======================================================
# False:

if( 2!=2 ):
    print(a)
else:
    print(b)

# ======================================================
# Blocos de codigo maiores

# variavel
num = 40 

# bloco a
if num > 40:

    if num <= 50:
        print('num menor que 50')
    else:
        print('num maior que 50')

# bloco b
else:

    if num <= 40:
        if num >= 10:
            print('num maior que 10 e menor que 40')
        else:
            print('num menor que 10 e menor que 40')

# ======================================================

# false
if 2 > 3:
    print('2 é maior que 3')

# false
elif 2 == 3:
    print('2 é igual a 3')

# true
elif 2 < 3:
    print('2 é menor que 3')

# ======================================================

a = 10 # valor par 

# não vai execultar o bloco de codigo
if False:

    a = a % 2
    b == 0
    print('é par')

# vai executar o bloco de codigo
else:

    print('é impar')

# ======================================================

a = 10 # variavel

# condição
b = a % 2

if b==0:
    print('é par')

else:
    print('é impar')

