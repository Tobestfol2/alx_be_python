# library_management.py: Contains the Book and Library classes.

class Book:
    """Represents a book with a title, author, and availability status."""
    
    def __init__(self, title: str, author: str):
        # Public attributes
        self.title = title
        self.author = author
        # Private attribute (conventionally marked with a single underscore)
        self._is_checked_out = False

    def __str__(self):
        """Returns a user-friendly string representation of the book."""
        return f"{self.title} by {self.author}"

    def check_out(self):
        """Marks the book as checked out if it is currently available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as available (returned)."""
        self._is_checked_out = False

    def is_available(self):
        """Returns the current availability status of the book."""
        return not self._is_checked_out


class Library:
    """Manages a collection of Book objects."""
    
    def __init__(self):
        # Private attribute: list to store Book instances
        self._books = []

    def add_book(self, book: Book):
        """Adds a Book object to the library's collection."""
        self._books.append(book)
        print(f"Added book: {book.title}")

    def _find_book(self, title: str):
        """Helper method to find a book object by title."""
        for book in self._books:
            if book.title.lower() == title.lower():
                return book
        return None

    def check_out_book(self, title: str):
        """Attempts to check out a book by title."""
        book = self._find_book(title)
        if book:
            if book.check_out():
                print(f"SUCCESS: Checked out '{title}'.")
            else:
                print(f"FAILURE: '{title}' is already checked out.")
        else:
            print(f"FAILURE: Book with title '{title}' not found.")

    def return_book(self, title: str):
        """Attempts to return a book by title."""
        book = self._find_book(title)
        if book:
            if not book.is_available():
                book.return_book()
                print(f"SUCCESS: Returned '{title}'.")
            else:
                print(f"NOTE: '{title}' was already available.")
        else:
            print(f"FAILURE: Book with title '{title}' not found.")

    def list_available_books(self):
        """Prints all books that are currently available."""
        available_count = 0
        for book in self._books:
            if book.is_available():
                print(f"   {book}")
                available_count += 1
        
        if available_count == 0:
            print("   No books are currently available.")
