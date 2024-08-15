from book import Book
from binary_search_tree import BinarySearchTree

def main():
    bst = BinarySearchTree()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Search Book")
        print("3. List Books")
        print("4. Remove Book")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            book = Book(title, author, isbn)
            bst.insert(book)
            print("Book added successfully.")

        elif choice == '2':
            title = input("Enter title to search: ")
            book = bst.search(title)
            if book:
                print(f"Book found: Title: {book.book.title}, Author: {book.book.author}, ISBN: {book.book.isbn}")
            else:
                print("Book not found.")

        elif choice == '3':
            books = bst.inorder_traversal()
            print("Books in library:")
            for book in books:
                print(book)

        elif choice == '4':
            title = input("Enter title to remove: ")
            bst.delete(title)
            print("Book removed successfully.")

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()