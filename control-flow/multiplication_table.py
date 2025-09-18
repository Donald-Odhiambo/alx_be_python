#Multiplication Table Generator

number = input("Enter a number to see its multiplication table:.")

for num in range(1 ,int(number) + 1):
    product = int(number) * num
    print(number , '*', num, '=', product)
    