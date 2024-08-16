class Node:
    def _init_(self, book):
        self.left = None
        self.right = None
        self.book = book

class BinarySearchTree:
    def _init_(self):
        self.root = None

    def insert(self, book):
        if self.root is None:
            self.root = Node(book)
        else:
            self._insert(self.root, book)

    def _insert(self, root, book):
        if book.title < root.book.title:
            if root.left is None:
                root.left = Node(book)
            else:
                self._insert(root.left, book)
        else:
            if root.right is None:
                root.right = Node(book)
            else:
                self._insert(root.right, book)