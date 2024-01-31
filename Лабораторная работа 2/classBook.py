class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Инициализация объекта класса Book.

        :param id_: Идентификатор книги.
        :param name: Название книги.
        :param pages: Количество страниц в книге.
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """
        Метод возвращает строку формата: "Книга "название_книги"".

        :return: Форматированная строка.
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Метод возвращает строку для инициализации точно такого же экземпляра.

        :return: Строка для инициализации экземпляра.
        """
        return f'Book(id_={self.id}, name={repr(self.name)}, pages={self.pages})'


book_example = Book(id_=1, name='test_name_1', pages=200)


print(str(book_example))  # Книга "test_name_1"
print(repr(book_example))  # Book(id_=1, name='test_name_1', pages=200)
