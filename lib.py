library = {}

while True:
    print("Library Management System:")
    print("1. Add a book")
    print("2. Search for a book")
    print("3. Checkout a book")
    print("4. Display library inventory")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        if title not in library:
            library[title] = {'author': author, 'checked_out': False}
            print(f"Book '{title}' by {author} added to the library.")
        else:
            print(f"Book '{title}' is already in the library.")
    elif choice == '2':
        title = input("Enter the title of the book to search: ")
        if title in library:
            info = library[title]
            availability = "available" if not info['checked_out'] else "checked out"
            print(f"Book '{title}' by {info['author']} is {availability}.")
        else:
            print(f"Book '{title}' not found in the library.")
    elif choice == '3':
        title = input("Enter the title of the book to checkout: ")
        if title in library:
            if not library[title]['checked_out']:
                library[title]['checked_out'] = True
                print(f"Book '{title}' checked out successfully.")
            else:
                print(f"Book '{title}' is already checked out.")
        else:
            print(f"Book '{title}' not found in the library.")
    elif choice == '4':
        print("Library Inventory:")
        for title, info in library.items():
            availability = "available" if not info['checked_out'] else "checked out"
            print(f"{title} by {info['author']} - {availability}")
    elif choice == '5':
        print("Exiting the Library Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
