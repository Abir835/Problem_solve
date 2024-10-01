def removeStars(s: str) -> str:
    stack = []

    for char in s:
        if char == '*':
            if stack:
                stack.pop()  # Remove the character before the '*'
        else:
            stack.append(char)  # Add the character to the stack

    return ''.join(stack)


print(removeStars("leet**cod*e"))