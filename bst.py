from __future__ import unicode_literals
from time import time
from collections import deque


class _BstNode(object):  # each node is the root of the subtree
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.depth = 1

    def left_depth(self):
        return self.left.depth if self.left else 0

    def right_depth(self):
        return self.right.depth if self.right else 0

    def _update_depth(self):
        self.depth = max(self.left_depth(), self.right_depth()) + 1

    def balance(self):
        return self.left_depth() - self.right_depth()

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

    def pre_order(self):
        yield self.value
        if self.left:
            for l in self.left.pre_order():
                yield l
        if self.right:
            for r in self.right.pre_order():
                yield r

    def in_order(self):
        if self.left:
            for l in self.left.in_order():
                yield l
        yield self.value
        if self.right:
            for r in self.right.in_order():
                yield r

    def post_order(self):
        if self.left:
            for l in self.left.post_order():
                yield l
        if self.right:
            for r in self.right.post_order():
                yield r
        yield self.value

    def breadth_first(self):
        q = deque([self])
        while q:
            node = q.popleft()
            yield node.value
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def _delete_help(self):
        q = deque([self])
        while q:
            node = q.popleft()
            yield node
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def delete(self, val):
        parent_node = None
        del_node = self
        nodes = self._delete_help()
        while nodes:
            parent_node = nodes.next()
            if parent_node.value == val:
                break
            if parent_node.left is not None:
                if parent_node.left.value == val:
                    del_node = parent_node.left
                    break
            if parent_node.right is not None:
                if parent_node.right.value == val:
                    del_node = parent_node.right
                    break
        if del_node.left is not None and del_node.right is not None:
            temp_node = None
            if self.balance() > 1:
                temp_node = del_node.left
                while temp_node.right is not None:
                    if temp_node.right.right is None:
                        unwire = temp_node
                        temp_node = temp_node.right
                        unwire.right = None
                        break
                    temp_node = temp_node.right
            else:
                temp_node = del_node.right
                while temp_node.left is not None:
                    if temp_node.left.left is None:
                        unwire = temp_node
                        temp_node = temp_node.left
                        unwire.left = None
                        break
                    temp_node = temp_node.left
            if parent_node == del_node:
                if self.right == temp_node:
                    temp_node.left = self.right
                else:
                    temp_node.right = self.left
                self.value = temp_node.value
            elif parent_node.right == del_node:
                parent_node.right = temp_node
                temp_node.left = del_node.left
            else:
                parent_node.left = temp_node
                temp_node.right = del_node.right
        elif del_node.left is not None:
            if parent_node == del_node:
                self.value = self.left.value
                self.left = self.left.left
            elif parent_node.left == del_node:
                parent_node.left = del_node.left
            else:
                parent_node.right = del_node.left
        elif del_node.right is not None:
            if parent_node == del_node:
                self.value = self.right.value
                self.right = self.right.right
            elif parent_node.left == del_node:
                parent_node.left = del_node.left
            else:
                parent_node.right = del_node.left
        else:
            if parent_node.left == del_node:
                parent_node.left = None
            else:
                parent_node.right = None


class BST(object):
    def __init__(self):
        self._size = 0
        self._root = None

    def __len__(self):
        return self._size

    def insert(self, val):
        """
        Insert the value val into the BST.  If val is already present,
        it will be ignored.
        """
        size_increased = False
        if self._root:
            size_increased = self._root.insert(val)  # value to insert
            if size_increased:
                self._size += 1
        else:
            self._root = _BstNode(val)
            self._size += 1
            size_increased = True
        return size_increased

    def contains(self, val):
        """Return True if val is in the BST, False if not."""
        return self._root.contains(val) if self._root else False

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
        return self._root.depth if self._root else 0

    def balance(self):
        """
        Return an integer, positive or negative that represents how well
        balanced the tree is. Trees which are higher on the left than the right
        should return a positive value, trees which are higher on the right
        than the left should return a negative value. An ideally-balanced tree
        should return 0.
        """
        return self._root.balance() if self._root else 0

    def pre_order(self):
        """
        Will return a generator that will return the values in the tree using
        pre-order traversal, one at a time.
        """
        if self._root:
            # Return the pre_order generator at self._root
            return self._root.pre_order()

    def in_order(self):
        """
        Will return a generator that will return the values in the tree using
        in-order traversal, one at a time.
        """
        if self._root:
            return self._root.in_order()

    def post_order(self):
        """
        Will return a generator that will return the values in the tree using
        post-order traversal, one at a time.
        """
        if self._root:
            return self._root.post_order()

    def breadth_first(self):
        """
        Will return a generator that will return the values in the tree using
        breadth_first traversal, one at a time.
        """
        if self._root:
            return self._root.breadth_first()

    def delete(self, val):
        if self.contains(val):
            self._size -= 1
            return self._root.delete(val)


if __name__ == '__main__':
    def populate(numlist):
        tree = BST()
        for num in numlist:
            tree.insert(num)
        return tree

    def crappy():
        numlist = range(1, 10)
        populate(numlist)

    def ideal():
        numlist = [5, 2, 8, 1, 3, 7, 9, 6, 10]
        populate(numlist)

    t0 = time()
    crappy()
    crappy_time = time() - t0
    print "Single List {}".format(crappy_time)

    t0 = time()
    ideal()
    ideal_time = time() - t0
    print "Balanced Tree {}".format(ideal_time)
