from user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def find_user_by_id(self, user_id):
        user = None
        for u in self.user_records:
            if u.user_id == user_id:
                user = u
                return user

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if author in self.books_available.keys():
            if book_name in self.books_available[author]:
                user.books.append(book_name)
                self.books_available[author].remove(book_name)
                if user.username not in self.rented_books.keys():
                    self.rented_books[user.username] = {}
                self.rented_books[user.username][book_name] = days_to_return
                return f"{book_name} successfully rented for the next {days_to_return} days!"
        book_rented = False
        days = None
        for user in self.rented_books.keys():
            if book_rented:
                break
            for b, d in self.rented_books[user].items():
                if b == book_name:
                    book_rented = True
                    days = d
                    break
        if book_rented:
            return f'The book "{book_name}" is already rented and ' \
                   f'will be available in {days} days!'

    def return_book(self, author: str, book_name: str, user: User):
        if user.username in self.rented_books.keys():
            if book_name in self.rented_books[user.username].keys():
                del self.rented_books[user.username][book_name]
                self.books_available[author].append(book_name)
                user.books.remove(book_name)
            else:
                return f"{user.username} doesn't have this book in his/her records!"



