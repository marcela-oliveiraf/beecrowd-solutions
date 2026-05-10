valores = list(map(float,input().split(' ')))

a, b, c = sorted(valores)[::-1]

continua = True 

if(a >= b + c):
    print("NAO FORMA TRIANGULO") 
    continua = False
if(a*a ==  b*b + c*c and continua):
    print("TRIANGULO RETANGULO")
if(a*a > b*b + c*c and continua):
    print("TRIANGULO OBTUSANGULO")
if(a*a < b*b + c*c and continua):
    print("TRIANGULO ACUTANGULO")
if(a == b == c and continua):
    print("TRIANGULO EQUILATERO")
if(a == b != c and continua):
    print("TRIANGULO ISOSCELES")
if(a == c != b and continua): 
    print("TRIANGULO ISOSCELES")
if(b == c != a and continua): 
    print("TRIANGULO ISOSCELES")