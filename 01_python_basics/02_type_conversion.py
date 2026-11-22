# Python Type Conversion

# Integer Conversions
number = 25
print("--- Integer Conversions (number = 25) ---")
print("Integer to Float:", float(number))
print("Integer to String:", str(number))
print("Integer to Boolean:", bool(number))

# Float Conversions
price = 99.99
print("--- Float Conversions (price = 99.99) ---")
print("Float to Integer:", int(price))
print("Float to String:", str(price))
print("Float to Boolean:", bool(price))

# String Conversions
name = "Alex"
value = "100"
price = "99.99"
print("--- String Conversions ---")
# print("String 'Alex' to Integer:", int(name)) # ValueError
print("String '100' to Integer:", int(value))
# print("String '99.99' to Integer:", int(price)) # ValueError
# print("String 'Alex' to Float:", float(name)) # ValueError
print("String '100' to Float:", float(value))
print("String '99.99' to Float:", float(price))
print("String 'Alex' to Boolean:", bool(name))
print("String '100' to Boolean:", bool(value))
print("String '99.99' to Boolean:", bool(price))

# Boolean Conversions
status = True
print("--- Boolean Conversions (status = True) ---")
print("Boolean to Integer:", int(status))
print("Boolean to Float:", float(status))
print("Boolean to String:", str(status))
