# print all subsequences of string
# print all subsequences of string
def subsequences(s, current='', i=0):
    # Base case: when index reaches the length of the string
    if i == len(s):
        print(current)
        return

    # Recursive case: two choices, either include the character at index or skip it
    subsequences(s, current + s[i], i + 1)  # Include character at index
    subsequences(s, current, i + 1)             # Skip character at index

# Example usage:
string = "abc"
print("All subsequences of", string, "are:")
subsequences(string)
#recursion
