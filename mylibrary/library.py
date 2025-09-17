class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append({"title": title, "author": author})

    def remove_book(self, title):
        self.books = list(filter(lambda book:book["title"] != title, self.books))

    def search_book(self, title):
        for book in self.books:
            if book["title"] == title:
                return True
        return False

    def show_books(self):
        return self.books
