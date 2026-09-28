#Implement Stack Using Python

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(item, "added to stack")

    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            item = self.stack.pop()
            print(item, "removed from stack")

    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Top item is:", self.stack[-1])

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def display(self):
        print("Stack:", self.stack)


# Create stack
s = Stack()

# Add items
s.push(10)
s.push(20)
s.push(30)

# Display stack
s.display()

# See top item
s.peek()

# Remove item
s.pop()

# Display again
s.display()

# Check if empty
print("Is stack empty?", s.is_empty())
