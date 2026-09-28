
stack = []

text = input("Enter a string: ")

# Push each character into stack
for char in text:
    stack.append(char)

print("Reverse string: ", end="")

while len(stack) > 0:
    print(stack.pop(), end="")
