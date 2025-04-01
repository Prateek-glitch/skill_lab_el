def max_rectangle_area(histogram):
    stack = []  # Stack to store indices
    max_area = 0  # Initialize max area
    index = 0  # Current index
    
    while index < len(histogram):
        if not stack or histogram[index] >= histogram[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            top = stack.pop()
            height = histogram[top]
            width = index if not stack else index - stack[-1] - 1
            max_area = max(max_area, height * width)
    
    while stack:
        top = stack.pop()
        height = histogram[top]
        width = index if not stack else index - stack[-1] - 1
        max_area = max(max_area, height * width)
    
    return max_area

# Example usage:
histogram = [2, 1, 5, 6, 2, 3]
print(max_rectangle_area(histogram))  # Output: 10
