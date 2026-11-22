# Python Operators

a = 10
b = 3

# 1. Arithmetic Operators
print("Addition (a + b):", a+b)
print("Subtraction (a - b):", a-b)
print("Multiplication (a * b):", a*b)
print("Division (a / b) [Quotient]:", a/b) # Division returning Quotient
print("Floor Division (a // b) [Integer Quotient]:", a//b) # Division returning integer Quotient
print("Modulus (a % b) [Remainder]:", a%b) # Division returning Reminder
print("Exponentiation (a ** b):", a**b)

# 2. Comparison Operators
print("a equals to b (a == b):", a==b)
print("a not equals to b (a != b):", a!=b)
print("a greater than b (a > b):", a>b)
print("a less than b (a < b):", a<b)
print("a greater than or equals to b (a >= b):", a>=b)
print("a less than or equals to b (a <= b):", a<=b)
# Note: '=' is for assigning a value & '==' is for comparison of two values

# 3. Logical Operators
print("Logical AND (a > 5 and b < 5):", a > 5 and b < 5)
print("Logical OR (a > 5 or b < 5):", a > 5 or b < 5)
print("Logical NOT (not(a > 5)):", not(a > 5))

# 4. Assignment Operators
a += 5 # a = a + 5
print("After a += 5:", a) # 15

b -= 2 # b = b - 2
print("After b -= 2:", b) # 1

a *= 4 # a = a * 4
print("After a *= 4:", a) # 60

b /= 2 # b = b / 2
print("After b /= 2:", b) # 0.5

a //= 2 # a = a // 2
print("After a //= 2:", a) # 30

b %= 2 # b = b % 2
print("After b %= 2:", b) # 0.5

a **= 2 # a = a ** 2
print("After a **= 2:", a) # 900

# 5. Identity Operators
language = "Python"
d = language
print("language is d:", language is d)
print("language is not d:", language is not d)

# 6. Membership Operators
print("'P' in language:", "P" in language)
print("'Pyt' in language:", "Pyt" in language)
print("'P' not in language:", "P" not in language)
print("'Java' not in language:", "Java" not in language)