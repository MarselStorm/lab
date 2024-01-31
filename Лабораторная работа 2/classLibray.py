class Library:
    def __init__(self, books=None):
        """
        Инициализация объекта класса Library.

        :param books: Список книг (по умолчанию None).
        """
        self.books = books if books is not None else []

    def get_next_book_id(self) -> int:
        """
        Метод, возвращающий идентификатор для добавления новой книги в библиотеку.

        :return: Идентификатор для новой книги.
        """
        if not self.books:
            return 1
        return self.books[-1]['id'] + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Метод, возвращающий индекс книги в списке по идентификатору.

        :param book_id: Идентификатор книги.
        :return: Индекс книги в списке.
        :raise ValueError: Если книги с запрашиваемым id не существует.
        """
        for index, book in enumerate(self.books):
            if book['id'] == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


library_example = Library([
    {'id': 1, 'name': 'Book 1', 'pages': 200},
    {'id': 2, 'name': 'Book 2', 'pages': 150},
    {'id': 3, 'name': 'Book 3', 'pages': 300},
])

print(library_example.get_next_book_id())
print(library_example.get_index_by_book_id(2))
