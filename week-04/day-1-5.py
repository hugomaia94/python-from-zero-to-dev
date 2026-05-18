class Library:
    def __init__(self, books="empty list"):
        self.books = []

    def add_book(self, title, author):
        book = {"title": title, "author": author}
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)
                print(f"'{title}' removed successfully.")
                return
        print("Book not found.")

    def list_books(self):
        for book in self.books:
            print(f"Title: {book['title']} | Author: {book['author']}")

    def search_by_author(self, author):
        for book in self.books:
            if author == book["author"]:
                print(f"Title: {book['title']} | Author: {book['author']}")
