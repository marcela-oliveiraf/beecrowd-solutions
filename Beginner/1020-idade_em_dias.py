age = int(input())

year = age//365
print("%d ano(s)"%year)

day = age%365
moth = day//30
print("%d mes(es)"%moth)

day = day%30
print("%d dia(s)"%day)