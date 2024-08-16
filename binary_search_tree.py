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
    def search(self, title):
        return self._search(self.root, title)

    def _search(self, root, title):
        if root is None or root.book.title == title:
            return root
        if title < root.book.title:
            return self._search(root.left, title)
        return self._search(root.right, title)

    def inorder_traversal(self):
        elements = []
        self._inorder_traversal(self.root, elements)
        return elements

    def _inorder_traversal(self, root, elements):
        if root:
            self._inorder_traversal(root.left, elements)
            elements.append(root.book.title)
            self._inorder_traversal(root.right, elements)

    def delete(self, title):
        self.root = self._delete(self.root, title)

    def _delete(self, root, title):
        if root is None:
            return root
        if title < root.book.title:
            root.left = self._delete(root.left, title)
        elif title > root.book.title:
            root.right = self._delete(root.right, title)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self._min_value_node(root.right)
            root.book = temp.book
            root.right = self._delete(root.right, temp.book.title)
        return root

    def _min_value_node(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current
