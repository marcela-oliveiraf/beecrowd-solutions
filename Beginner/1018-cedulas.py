n = int(input())
print(n)

result = n//100
print("%d nota(s) de R$ 100,00"%result)
result1 = n%100

result = result1//50
print("%d nota(s) de R$ 50,00"%result)
result2 = result1%50

result = result2//20
print("%d nota(s) de R$ 20,00"%result)
result3 = result2%20

result = result3//10
print("%d nota(s) de R$ 10,00"%result)
result4 = result3%10

result = result4//5
print("%d nota(s) de R$ 5,00"%result)
result5 = result4%5

result = result5//2
print("%d nota(s) de R$ 2,00"%result)
result6 = result5%2

result = result6//1
print("%d nota(s) de R$ 1,00"%result)
