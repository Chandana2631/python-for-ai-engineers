# Python Strings

name = "Alex"
language = "Python"
role = " Web Developer "
print("Name:", name)
print("Language:", language)
print("Role:", role)

# String Slicing
print("Slice [0:4] (Full string):", name[0:4]) # Full string
print("Slice [2:3] (Part of string):", name[2:3]) # Part of string
print("Slice [:3] (Start to index 2):", name[:3]) # From start to mentioned destination
print("Slice [1:] (Index 1 to end):", name[1:]) # From the mentioned start to till end
print("Slice [::-1] (Reversed string):", name[::-1]) # Reverse the string

# String Methods
print("Uppercase (upper()):", language.upper()) # Converts to uppercase
print("Lowercase (lower()):", language.lower()) # Converts to lowercase
print("Count of 'y' (count('y')):", language.count("y")) # Counts occurrences of 'y'
print("Capitalize first letter (capitalize()):", language.capitalize()) # Capitalizes first letter
print("Starts with 'P' (startswith('P')):", language.startswith("P")) # Checks if string starts with 'P'
print("Ends with 'n' (endswith('n')):", language.endswith("n")) # Checks if string ends with 'n'
print("Find index of 'o' (find('o')):", language.find("o")) # Returns index of 'o' (-1 if not found)
print("Index of 'n' (index('n')):", language.index("n")) # Returns index of 'n' (error if not found)
print("Split into list (split()):", role.split()) # Splits string into a list
print("Replace 'e' with 'ee' (replace('e', 'ee')):", role.replace("e", "ee")) # Replaces 'e' with 'ee'
print("Strip outer spaces (strip()):", role.strip()) # Removes leading/trailing spaces but not between spaces

# String Formatting & Concatenation
print(name + " is a " + language + role) # Concatenation using '+'
print(f"{name} is a {language}{role}") # f-string formatting