# controllers -> operators
# Arithmetic operators -> { + , - , / , // , * , ** }

cab_fare = 1000 
tax = 0.18

Tax_to_pay = cab_fare * tax
Total_fare = cab_fare + Tax_to_pay

print("Total fare is:",Total_fare)
print("Tax to pay is:",Tax_to_pay)



num1 = 10
num2 = 20
print("division is:", num1 / num2)  #Floating point division

print('Integral division is:', num1 // num2)   #Integral division

num3 = 2
num4 = 3
num5 = num3 ** num4     #exponential
print('Cube of 2 is:', num5)

# number system
print(num1)
print(bin(num1))
print(oct(num1))
print(hex(num1))