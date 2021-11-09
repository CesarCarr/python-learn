largura = int(input("Digite a largura de um retângulo: "))
altura = int(input("Digite a altura de um retângulo: "))

def linhavazia(x):
    print("#",end="")
    while x >= 3:
        print(" ",end="")
        x = x - 1
    print("#")

def Largura(i):
    while i >= 1:
        print("#", end="")
        i = i - 1

while altura >= 1 and largura >=1:
    Largura(largura)
    altura = altura - 1
    print(end='\n')
    while altura > 1:
        linhavazia(largura)
        altura = altura - 1
    Largura(largura)
    largura = 0

print(end='\n')
input("Aperte Enter para sair: ")