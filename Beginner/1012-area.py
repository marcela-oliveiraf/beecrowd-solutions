a, b, c = map(float, input().split(' '))

pi = 3.14159

triangle = (a*c)/2
radius_circle = pi*c*c
trapezium = ((a+b)*c)/2
square = b*b
rectangle = a*b

print("TRIANGULO: %0.3f"%triangle)
print("CIRCULO: %0.3f"%radius_circle)
print("TRAPEZIO: %0.3f"%trapezium)
print("QUADRADO: %0.3f"%square)
print("RETANGULO: %0.3f"%rectangle)