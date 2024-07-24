def kyabalancehai(str1):
    l = []
    for ele in str1:
        if ele in '{([':
            l.append(ele)
        elif ele == ')':
            if not l or l[-1] != '(':
                return False
            l.pop()
        elif ele == '}':
            if not l or l[-1] != '{':
                return False
            l.pop()
        elif ele == ']':
            if not l or l[-1] != '[':
                return False
            l.pop()
    return not l

# Get the input from the user
str1 = input("Enter the string: ")
print(kyabalancehai(str1))