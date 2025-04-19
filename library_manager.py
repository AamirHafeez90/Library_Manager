# library_manager.py

import os
import json

# Initialize the library
library = []

# File to save/load library
LIBRARY_FILE = 'library.txt'

# Load library from file if exists
def load_library():
    global library
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, 'r') as file:
            try:
                library = json.load(file)
            except json.JSONDecodeError:
                library = []

# Save library to file
def save_library():
    with open(LIBRARY_FILE, 'w') as file:
        json.dump(library, file)

# Add a book
def add_book():
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    while True:
        try:
            year = int(input("Enter the publication year: ").strip())
            break
        except ValueError:
            print("Please enter a valid year.")
    genre = input("Enter the genre: ").strip()
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read = True if read_input == 'yes' else False

    book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }
    library.append(book)
    print("Book added successfully!\n")

# Remove a book
def remove_book():
    title = input("Enter the title of the book to remove: ").strip()
    found = False
    for book in library:
        if book['title'].lower() == title.lower():
            library.remove(book)
            found = True
            print("Book removed successfully!\n")
            break
    if not found:
        print("Book not found.\n")

# Search for a book
def search_book():
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ").strip()
    if choice not in ['1', '2']:
        print("Invalid choice.\n")
        return
    keyword = input("Enter the title/author: ").strip().lower()
    matches = []
    for book in library:
        if (choice == '1' and keyword in book['title'].lower()) or \
           (choice == '2' and keyword in book['author'].lower()):
            matches.append(book)
    if matches:
        print("\nMatching Books:")
        for idx, book in enumerate(matches, start=1):
            read_status = 'Read' if book['read'] else 'Unread'
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
        print()
    else:
        print("No matching books found.\n")

# Display all books
def display_all_books():
    if not library:
        print("Your library is empty.\n")
        return
    print("\nYour Library:")
    for idx, book in enumerate(library, start=1):
        read_status = 'Read' if book['read'] else 'Unread'
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    print()

# Display statistics
def display_statistics():
    total = len(library)
    if total == 0:
        print("Your library is empty.\n")
        return
    read_count = sum(1 for book in library if book['read'])
    percentage = (read_count / total) * 100
    print(f"Total books: {total}")
    print(f"Percentage read: {percentage:.1f}%\n")

# Main menu
def main():
    load_library()
    while True:
        print("Menu\nWelcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_book()
        elif choice == '2':
            remove_book()
        elif choice == '3':
            search_book()
        elif choice == '4':
            display_all_books()
        elif choice == '5':
            display_statistics()
        elif choice == '6':
            save_library()
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
