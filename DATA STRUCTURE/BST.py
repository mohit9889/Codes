class Node():
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class bst():
    def __init__(self):
        self.root = None

    def create(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            current = self.root
            while(1):
                if data < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(data)
                elif data > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(data)
                else:
                    break

    def inorder(self,node):
        if node is not None:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)
            
    def preorder(self, node):
        if node is not None:
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)
            
    def postorder(self, node):
        if node is None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data)

tree = bst()
arr = [50,30,20,40,70,60,80]
for i in arr:
    tree.create(i)
print("inorder")
bst.inorder(tree.root)
print("preorder")
bst.preorder(tree.root)
print("postorder")
bst.postorder(tree.root)
