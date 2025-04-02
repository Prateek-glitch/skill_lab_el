def reverse_string(s):
    stack = list(s)  # Push all characters onto the stack
    return ''.join(stack[::-1])  # Pop all characters to reverse

# Example usage
s = "hello"
print(reverse_string(s))  # Output: "olleh"
