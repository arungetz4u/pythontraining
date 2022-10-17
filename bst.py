class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

        def insert(self, data):
            if data == self.data:
                return
            if data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = BST(data)
            else:
                if self.riht:
                    self.right.insert(data)
                else:
                    self.right = BST(data)
