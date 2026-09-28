#Implement Queue Using Python

class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(item, "added to queue")

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            item = self.queue.pop(0)
            print(item, "removed from queue")

    def peek(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Front item is:", self.queue[0])

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def display(self):
        print("Queue:", self.queue)


# Create queue
q = Queue()

# Add items
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

# Display queue
q.display()

# See front item
q.peek()

# Remove item
q.dequeue()

# Display again
q.display()

# Check if empty
print("Is queue empty?", q.is_empty())
