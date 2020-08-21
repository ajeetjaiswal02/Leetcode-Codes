# Binary search tree searching and inserting values

class Node:
    def __init__(self,data = None):
        self.data = data
        self.left = None
        self.right = None

class Binary:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data,self.root)

    def _insert(self,data,cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data,cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:   
                self._insert(data,cur_node.right)

    def find(self,data):
        if self.root:
            is_found = self._find(data,self.root)
            if is_found:
                return True
            return False
        else:
            return None

    def _find(self,data,cur_node):
        if data > cur_node.data and cur_node.right:
            return self._find(data,cur_node.right)
        elif data < cur_node.data and cur_node.left:
            return self._find(data,cur_node.left) 
        if data == cur_node.data:
            return True

gst = Binary()
gst.insert(2)
gst.insert(4)
gst.insert(6)
gst.insert(7)
output = gst.find(41)
print(output)
                                 