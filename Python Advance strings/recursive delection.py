def can_become_empty_with_slicing(string, substring):
  
    # If the string is empty, it can be considered successfully reduced to empty
    if not string:
        return True
    
    # Check if the substring exists at any position
    index = string.find(substring)
    if index != -1:
        # Remove the substring using slicing and recursively check
        return can_become_empty_with_slicing(string[:index] + string[index + len(substring):], substring)
    
    # If the substring is not found, and the string is not empty, return False
    return False

# Example test case
input_string = "geeksforgeeks"
substring = "geeks"

# Call the function and store the result
result = can_become_empty_with_slicing(input_string, substring)

print(result)
