class Node:
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if self.value == data:   # not allowing duplicates
            return False
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def contains(self, data):
        if (self.value == data):
            return True
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.contains(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.contains(data)
            else:
                return False


class Tree:
    def __init__(self):
        self.root = None

    def length(self):
        return self.size

    def insert(self, data):
        """
        Insert the value val into the BST.  If val is already present,
        it will be ignored.
        """
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)

    def contains(self, data):
        """Return True if val is in the BST, False if not."""
        if self.root:
            return self.root.contains(data)
        else:
            return False

    def size(self):
        """
        Return the integer size of the BST (equal to the total number of values
        stored in the tree), 0 if the tree is empty.
        """
        pass

    def depth(self):
        """
        Return an integer representing the total number of levels in the tree.
        If there is one value, the depth should be 1, if two values it will be
        2, if three values it may be 2 or three, depending, etc.
        """
        pass

    def balance(self):
        """
        Return an integer, positive or negative that represents how well
        balanced the tree is.Trees which are higher on the left than the right
        should return a positive value, trees which are higher on the right
        than the left should return a negative value. An ideallyl-balanced tree
        should return 0.
        """
        pass
