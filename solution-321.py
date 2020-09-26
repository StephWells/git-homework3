#Exercise 3.21 scenario
#Purchase price = 27 cents
#Purchaser pays with a dollar  = 100 cents
#Change due = 73 cents
#Determine the amount of change in fewest coins

q = 25
d = 10
n = 5
p = 1

purchase_price = int(input("Please enter your purchase price in cents of a dollar or less: "))

calculate_change = 100 - purchase_price

if purchase_price == 100:
    print('Your change is 0 cents')
elif purchase_price != 100:
    counter_q = calculate_change // q
    print('Your change is:')
    print(counter_q, "quarters")
    calculate_change = calculate_change % q


if calculate_change != 0:        
    counter_d = calculate_change // d
    calculate_change = calculate_change % d
    print(counter_d, 'dimes')
elif calculate_change != 0:        
    counter_n = calculate_change // n
    calculate_change = calculate_change % n
    print(counter_n, 'nickels')     
      
if calculate_change != 0:        
    print(calculate_change, 'pennies')
