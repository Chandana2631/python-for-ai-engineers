# Python Lists

languages = ["Python", "Java", "C", "HTML", "C++"]
print("Original list:", languages)
    
# 1. Accessing elements in Lists
print("First item (index 0):", languages[0]) # First item 
print("Fifth item (index 4):", languages[4]) # Fifth item
print("Last item (index -1):", languages[-1]) # Last item
print("Second item (index -4):", languages[-4]) # Second item
print("Length of the list:", len(languages)) # Count of elements in the list

# 2. List Slicing
print("Slice [1:3] (Index 1 to 2):", languages[1:3]) # Index from 1 to 2
print("Slice [:2] (Start to index 1):", languages[:2]) # From start to index 1
print("Slice [1:] (Index 1 to end):", languages[1:]) # From index 1 to the end
print("Slice [-3:-1] (Third-last to second-last):", languages[-3:-1]) # Third-last to second-last
print("Slice [-3:] (Third-last to end):", languages[-3:]) # Third-last to the end
print("Slice [:-1] (All except last item):", languages[:-1]) # # Everything except the last item
print("Slice [::-1] (Reversed list):", languages[::-1]) # Reverse the list
print("Slice [::2] (Every 2nd element):", languages[::2]) # Every 2nd element starting from first element

# 3. Modifying Lists
# Add an element at the end
languages.append("Javascript")
print("After append('Javascript'):", languages)
# Add multiple elements at the end
languages.extend(["C#", "SQL"])  
print("After extend(['C#', 'SQL']):", languages)
# Update elements at the mentioned index
languages[0] = "Python3" 
print("After updating index 0 to 'Python3':", languages)
# Insert elements at the mentioned index
languages.insert(2, "CSS") 
print("After insert(2, 'CSS'):", languages)
# Remove an element at the end
languages.pop() 
print("After pop() (removed last element):", languages)
# Remove an element at the mentioned index
languages.pop(3) 
print("After pop(3) (removed index 3):", languages)
# Remove a mentioned element by value
languages.remove("Javascript") 
print("After remove('Javascript'):", languages)
# Sort list alphabetically (A-Z)
languages.sort() 
print("After sort() (A-Z):", languages)
# Sort list in descending order (Z-A)
languages.sort(reverse=True) 
print("After sort(reverse=True) (Z-A):", languages)
# Create a sorted copy without modifying the original
sorted_copy = sorted(languages)
print("Sorted copy using sorted():", sorted_copy)
# Reverse the current order of the list
languages.reverse() 
print("After reverse():", languages)
# Return the index of the mentioned element
print("Index of 'C++':", languages.index("C++"))
# Return the count of occurences of the mentioned element
print("Count of 'C++':", languages.count("C++"))
# Creates a copy of the list
copied_list = languages.copy()
print("Copied list using copy():", copied_list)
# Removes all elements in the list
languages.clear()
print("List after clear():", languages)