class User:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books = []

    def info(self):
        ordered_books = list(sorted(self.books))
        return ordered_books

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.info()}"

