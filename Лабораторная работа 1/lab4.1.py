class Tree:
    def __init__(self, species: str, age: int, height: float):
        """
        Создание объекта "Дерево".

        :param species: Вид дерева.
        :param age: Возраст дерева в годах.
        :param height: Высота дерева в метрах.

        :raise ValueError: Если возраст или высота дерева заданы отрицательными числами.

        Примеры:
        >>> oak_tree = Tree("Oak", 20, 15.5)
        """
        if not isinstance(species, str):
            raise TypeError("Вид дерева должен быть строкой")
        self.species = species

        if not isinstance(age, int):
            raise TypeError("Возраст дерева должен быть целым числом")
        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным числом")
        self.age = age

        if not isinstance(height, (int, float)):
            raise TypeError("Высота дерева должна быть числом")
        if height < 0:
            raise ValueError("Высота дерева не может быть отрицательным числом")
        self.height = height

    def photosynthesis(self) -> str:
        """
        Симуляция фотосинтеза дерева.

        :return: Сообщение о том, что фотосинтез выполнен.

        Примеры:
        >>> oak_tree = Tree("Oak", 20, 15.5)
        >>> oak_tree.photosynthesis()
        'Photosynthesis process completed.'
        """
        ...

    def shed_leaves(self, num_leaves: int) -> int:
        """
        Процесс опадения листьев дерева.

        :param num_leaves: Количество листьев, которые должны опасть.
        :return: Фактическое количество опавших листьев.

        Примеры:
        >>> oak_tree = Tree("Oak", 20, 15.5)
        >>> oak_tree.shed_leaves(5)
        5
        """
        ...

    def grow(self, growth_rate: float) -> None:
        """
        Увеличение высоты дерева.

        :param growth_rate: Скорость роста дерева.

        Примеры:
        >>> oak_tree = Tree("Oak", 20, 15.5)
        >>> oak_tree.grow(0.2)
        """
        ...


class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        Создание объекта "Книга".

        :param title: Название книги.
        :param author: Автор книги.
        :param pages: Количество страниц в книге.

        :raise ValueError: Если количество страниц меньше 1.

        Примеры:
        >>> my_book = Book("Python Programming", "John Doe", 300)
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        self.title = title

        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть строкой")
        self.author = author

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if pages < 1:
            raise ValueError("Количество страниц должно быть больше 0")
        self.pages = pages

    def read_page(self, page_number: int) -> str:
        """
        Чтение указанной страницы.

        :param page_number: Номер страницы для чтения.
        :return: Текст, прочитанный на странице.

        Примеры:
        >>> my_book = Book("Python Programming", "John Doe", 300)
        >>> my_book.read_page(10)
        'Read content from page 10.'
        """
        ...

    def bookmark_page(self, page_number: int) -> None:
        """
        Установка закладки на странице.

        :param page_number: Номер страницы для установки закладки.

        Примеры:
        >>> my_book = Book("Python Programming", "John Doe", 300)
        >>> my_book.bookmark_page(50)
        """
        ...

    def calculate_reading_progress(self, current_page: int) -> float:
        """
        Расчет прогресса чтения книги.

        :param current_page: Текущая страница, на которой находится читатель.
        :return: Прогресс в процентах.

        Примеры:
        >>> my_book = Book("Python Programming", "John Doe", 300)
        >>> my_book.calculate_reading_progress(100)
        33.33
        """
        ...

class Vehicle:
    def __init__(self, brand: str, model: str, fuel_type: str, fuel_tank_capacity: float):
        """
        Создание объекта "Транспортное средство".

        :param brand: Марка транспортного средства.
        :param model: Модель транспортного средства.
        :param fuel_type: Тип используемого топлива.
        :param fuel_tank_capacity: Объем топливного бака в литрах.

        :raise ValueError: Если емкость топливного бака меньше 0.

        Примеры:
        >>> car = Vehicle("Toyota", "Camry", "Petrol", 60.0)
        """
        if not isinstance(brand, str):
            raise TypeError("Марка транспортного средства должна быть строкой")
        self.brand = brand

        if not isinstance(model, str):
            raise TypeError("Модель транспортного средства должна быть строкой")
        self.model = model

        if not isinstance(fuel_type, str):
            raise TypeError("Тип топлива должен быть строкой")
        self.fuel_type = fuel_type

        if not isinstance(fuel_tank_capacity, (int, float)):
            raise TypeError("Объем топливного бака должен быть числом")
        if fuel_tank_capacity < 0:
            raise ValueError("Объем топливного бака не может быть отрицательным числом")
        self.fuel_tank_capacity = fuel_tank_capacity

    def start_engine(self) -> str:
        """
        Запуск двигателя транспортного средства.

        :return: Сообщение о том, что двигатель запущен.

        Примеры:
        >>> car = Vehicle("Toyota", "Camry", "Petrol", 60.0)
        >>> car.start_engine()
        'Engine started successfully.'
        """
        ...

    def refuel(self, amount: float) -> None:
        """
        Заправка транспортного средства топливом.

        :param amount: Количество топлива для заправки.

        :raise ValueError: Если количество топлива для заправки меньше 0.

        Примеры:
        >>> car = Vehicle("Toyota", "Camry", "Petrol", 60.0)
        >>> car.refuel(30.0)
        """
        ...

    def drive(self, distance: float) -> str:
        """
        Поездка на транспортном средстве.

        :param distance: Пройденное расстояние.

        :return: Сообщение о пройденном расстоянии.

        Примеры:
        >>> car = Vehicle("Toyota", "Camry", "Petrol", 60.0)
        >>> car.drive(100.0)
        'Vehicle traveled 100.0 kilometers.'
        """
        ...

