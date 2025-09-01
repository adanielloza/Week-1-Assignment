class Book:
    # Attributes initialized to blank strings by default
    author = ""
    title = ""

    def __init__(self, author, title):
        """Initialize a new Book with author and title."""
        self.author = author
        self.title = title

    def display(self):
        """Print book details in the format: title, written by author."""
        print(f"{self.title}, written by {self.author}")


if __name__ == "__main__":
    # Create two book objects
    book1 = Book("J. K. Rowling", "Harry Potter and the Goblet of Fire")
    book2 = Book("Walter Scott", "Ivanhoe: A Romance")

    # Display their details
    book1.display()
    book2.display()

