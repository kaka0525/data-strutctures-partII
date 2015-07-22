class BinaryTreeNode(object):

    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = val
        self.size = 0

    def length(self):
        return self.size

    def insert(self, val):
        """
        Insert the value val into the BST.  If val is already present,
        it will be ignored.
        """
        pass

    def contains(self, value):
        """Return True if val is in the BST, False if not."""
        pass

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
