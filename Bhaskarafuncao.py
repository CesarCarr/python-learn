import math

print("Solucione uma equação de 2º obtendo os valores das raízes")

a = float(input())
b = float(input())
c = float(input())

delta = float(((b**2) - (4*a*c)))

def delta(a, b, c):
    return ((b**2) - (4*a*c))

if delta == 0:
        print("a raiz desta equação é",X)
else:
        if delta < 0:
        
            False
        
            print("esta equação não possui raízes reais")

        else:
        
            delta > 0
            X = float((-b + math.sqrt(delta))/ (2*a))
        
            Y = float((-b - math.sqrt(delta))/ (2*a))

            if X > Y:
                print("as raízes da equação são",Y,"e",X)
            else:
                print("as raízes da equação são",X,"e",Y)



            
