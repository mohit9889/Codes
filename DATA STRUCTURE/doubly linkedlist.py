class Node():
    def __init__(self, data):
        self.data=data
        self.next=None
        self.pvr=None

class doubly():
    def __init__(self):
        self.head = None
        self.last_node = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.last_node = new_node
        else:
            new_node.pvr = self.last_node
            new_node.next = None
            self.last_node.next = new_node
            self.last_node = new_node

    def display_forward(self):
        print("Diplaying forward...")
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def display_pvr(self):
        print("Displaying previous...")
        current = self.last_node 
        while current is not None:
            print(current.data)
            current = current.pvr

if __name__ == "__main__":
    doubly = doubly()
    n = int(input("No. of elements: "))
    for i in range(n):
        data = int(input("Data: "))
        doubly.append(data)
    doubly.display_forward()
    doubly.display_pvr()


            
            
        
            
        
