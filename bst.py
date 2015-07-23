class _BstNode(object):  # each node is the root of the subtree
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.depth = 1

    def left_depth(self):
        if self.left:
            return self.left.depth
        else:
            return 0

    def right_depth(self):
        if self.right:
            return self.right.depth
        else:
            return 0

    def _update_depth(self):
        self.depth = max(self.left_depth(), self.right_depth()) + 1

    def insert(self, value_to_insert):
        if self.value == value_to_insert:  # not allowing duplicates
            return False
        else:
            return_val = False
            if self.value > value_to_insert:
                if self.left:
                    return_val = self.left.insert(value_to_insert)
                else:
                    self.left = _BstNode(value_to_insert)
                    return_val = True
            else:
                if self.right:
                    return_val = self.right.insert(value_to_insert)
                else:
                    self.right = _BstNode(value_to_insert)
                    return_val = True
            self._update_depth()
            return return_val

    def contains(self, value_to_find):
        if self.value == value_to_find:
            return True
        elif self.value > value_to_find:
            if self.left:
                return self.left.contains(value_to_find)
            else:
                return False
        else:
            if self.right:
                return self.right.contains(value_to_find)
            else:
                return False


class BST(object):
    def __init__(self):
        self._size = 0
        self._root = None
        self._balance = 0

    def __len__(self):
        return self._size

    def insert(self, val):
        """
        Insert the value val into the BST.  If val is already present,
        it will be ignored.
        """

        if self._root:
            size_increased = self._root.insert(val)  # value to insert
            if size_increased:
                self._size += 1
            return size_increased
        else:
            self._root = _BstNode(val)
            self._size += 1
            return True

    def contains(self, val):
        """Return True if val is in the BST, False if not."""
        if self._root:
            return self._root.contains(val)
        else:
            return False

    def size(self):
        """
        Return the integer size of the BST (equal to the total number of values
        stored in the tree), 0 if the tree is empty.
        """
        return self._size

    def depth(self):
        """
        Return an integer representing the total number of levels in the tree.
        If there is one value, the depth should be 1, if two values it will be
        2, if three values it may be 2 or three, depending, etc.
        """
        if self._root:
            return self._root.depth
        else:
            return 0

    def balance(self):
        """
        Return an integer, positive or negative that represents how well
        balanced the tree is.Trees which are higher on the left than the right
        should return a positive value, trees which are higher on the right
        than the left should return a negative value. An ideallyl-balanced tree
        should return 0.
        """
        if self._root:
            return self._root.left_depth() - self._root.right_depth()
        else:
            return 0
