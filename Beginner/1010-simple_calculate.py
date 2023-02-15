line1 = input().split(' ')
line2 = input().split(' ')

product_code1, product_units1, unit_price1 = line1 
product_code2, product_units2, unit_price2 = line2 

total = (int(product_units1) * float(unit_price1)) + (int(product_units2) * float(unit_price2))
        
print("VALOR A PAGAR: R$ %0.2f"%total)  