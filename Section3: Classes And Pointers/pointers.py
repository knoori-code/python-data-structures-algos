num1 = 11
num2 = num1

print('This is the value of num1:', num1)
print('This is the value of num2:', num2)

# Shows the location in memory
print('This is the location of num1:', id(num1))
print('This is the location of num2:', id(num2))

num2 = 23

print('This is the value of num1:', num1)
print('This is the value of num2:', num2)

# num2 changes its location in memory from the original location
print('This is the location of num1:', id(num1))
print('This is the location of num2:', id(num2))
