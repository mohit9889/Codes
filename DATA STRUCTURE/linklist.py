class node():
    def __init__(self, data):
        self.data = data
        self.next = None

class linklist():
    def __init__(self):
        self.head = None
        self.last_node = None

    def append(self, data):
        if self.last_node is None:
            self.head = node(data)
            self.last_node = self.head
        else:
            self.last_node.next = node(data)
            self.last_node = self.last_node.next

    def display(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

if __name__ == "__main__":
    linklist = linklist()
    n = int(input("No. of elements: "))
    for i in range(n):
        data = int(input("Enter data: "))
        linklist.append(data)
    print("Printing...")
    linklist.display()
    
        
    
    
