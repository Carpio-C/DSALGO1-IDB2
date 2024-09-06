'''
nintendoWii = 100
money = int (input("How much money do you have?: "))
print("i have: ",money,"pesos")

youAfford = int(money/nintendoWii)
neededMoney = ((money % nintendoWii) - nintendoWii)

print("You can afford: ", youAfford, "Nintendo Wiis" )
print("you need:",neededMoney,"to afford Wii")
'''

'''
sum = 0
for x in range(1, 11):
    print(sum, "Is the the sum of the numbers 1 - 10")
'''

'''
Input1=int(input("enter first number: "))
Input2=int(input("enter second number: "))
sum = 0

for x in range(Input1,Input2):
    sum = sum + x
print(sum, "is the total sum of ", Input1, " and ", Input2)
'''
'''
userInt=int(input("Enter a number: "))
factorial = 1
for x in range (1, userInt+1):
    factorial = factorial * x

print("The factorial of ", x, " is ", factorial)
'''

'''
userInput= int (input("Enter a number: "))
for x in range (1, userInput + 1):
    if userInput % x == 0:
        print(x)
'''
