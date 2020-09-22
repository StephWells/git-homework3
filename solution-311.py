total_gallons_used = 0 
total_miles_driven = 0
confirmation = 'yes'
 
while confirmation == 'yes':
   tank_gallons = float(input('Please enter the gallons used'))
   tank_miles = float(input('Please enter the miles driven'))
   total_gallons_used += tank_gallons
   total_miles_driven += tank_miles
   tank_avg = tank_miles / tank_gallons
   print(f'The miles per gallon for this tank was: {tank_avg}')
   confirmation = input('Enter yes if you want to enter more tank information')
if confirmation != 'yes':
  overall_avg = total_miles_driven / total_gallons_used
  print(f'The overall average miles per gallon was: {overall_avg}')
