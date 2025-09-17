from mylibrary import Library

if __name__ == "__main__":
    library = Library()

    while True:
        print("\n1. Add Book\n2. Remove Book\n3. Search Book\n4. Show Books\n5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter the book title: ")
            author = input("Enter the author: ")
            library.add_book(title, author)
            print(f"Book '{title}' by {author} added.")
        elif choice == "2":
            title = input("Title to remove: ")
            library.remove_book(title)
            print(f"Book '{title}' removed (if it existed).")
        elif choice == "3":
            title = input("Title to search: ")
            found = library.search_book(title)
            print("Found!" if found else "Not Found")
        elif choice == "4":
            books = library.show_books()
            if books:
                print("Books in library:")
                for index, book in enumerate(books, start=1):
                    print(f"{index}. {book['title']} by {book['author']}")
            else:
                print("No books in library.")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")
