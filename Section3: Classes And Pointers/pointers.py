num1 = 11
num2 = num1

print('Before num2 value is updated:')
print('num1 =', num1)
print('num2 =', num2)

# Shows the location in memory
print('\nnum1 points to:', id(num1))
print('num2 points to:', id(num2))

num2 = 23

print('\nAfter num2 value is updated:')
print('num1 =', num1)
print('num2 =', num2)

# num2 changes its location in memory from the original location
print('\nnum1 points to:', id(num1))
print('num2 points to:', id(num2))
