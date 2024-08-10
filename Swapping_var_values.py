# 1.	Write a Python program to swap the values of two variables without using a temporary variable.

a = 10 
b = 20 
print(a , b)
c = a
a = b
b = c
print(a, b )

a , b = b , a

print(a, b )

# This method only works for integers and works faster 
# because this method uses bit operation 
# (for same values, output = 0 and for different values, output = 1) .

# XOR Operations (bitwise Operator)
a ^= b
b ^= a 
a ^= b 
print(a ,b )