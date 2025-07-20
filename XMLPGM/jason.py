
# def first_non_repeating_char(s):
#     # Create a dictionary to count characters
#     char_count = {}

#     # Count each character in the string
#     for char in s:
#         char_count[char] = char_count.get(char, 0) + 1

#     # Find the first character with a count of 1
#     for char in s:
#         if char_count[char] == 1:
#             return char

#     return None  # If no non-repeating character is found

# # Example usage
# input_str = "sswiss"
# result = first_non_repeating_char(input_str)

# if result:
#     print("First non-repeating character:", result)
# else:
#     print("No non-repeating character found.")



def sample(st):
    orgdict={}
    for x in st:
        orgdict[x]=orgdict.get(x,0)+1

    for x in st:
        if orgdict[x]==1:
            return x
    
    return none
print(sample("sshii"))

