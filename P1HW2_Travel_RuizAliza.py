# Making a Travel Expense using IDLE
# 09/22/2022
# CTI-110 P1HW2 - Travel Expense
# Aliza Ruiz
#

print('This program calculates and displays travel expenses')
print()
budget = int(input('Enter Budget:'))
print()
destination = input('Enter your travel destination:')
print()
spend_gas = int(input('How much do you think you will spend on gas?'))
print()
hotel = input('Approximately, how much will you need for accomodation/hotel?')
print()
food = int(input('Last, how much do you need for food?'))
print()
print('------------Travel Expenses------------')
print('Location:', destination)
print('Initial Budget:',budget)
total = spend_gas + int(hotel) + int(food)
end_price = budget - int(total)
print('Fuel:',spend_gas)
print('Accomodation:',hotel)
print('Food:',food)
print()
print('Remaining Balance:',end_price)
