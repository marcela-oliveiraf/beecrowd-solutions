a, b, c = map(float, input().split(' '))

delta = b**2 - 4*a*c

if (a == 0.0 or delta <= 0.0): 
    print("Impossivel calcular")
else:
    r1 = (-b + (delta**0.5))/(2*a)
    r2 = (-b - (delta**0.5))/(2*a)
    print("R1 = %0.5f"%r1)
    print("R2 = %0.5f"%r2)    
    