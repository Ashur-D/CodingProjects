#fstring example with numbers and rounding
num1 = 9.93843
num2 = 1.0934
num3 = 213
# using print we round num1 and num2 to the second decimal point and use \n to go to the next line
print(f"{num1:10.2}\n{num2:10.2}") # 10 is the number of spaces when allocated to display the value of num1 & num2
print(f"{num1:15.2}\n{num2:.3}")
print(f" price1: {num1:15.2}\n price2: {num2:15.2}\n price3: {num3:15}")