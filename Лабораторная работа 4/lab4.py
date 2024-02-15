class Animal:
    """
    Базовый класс, представляющий животное.
    """

    def __init__(self, name: str, age: int):
        """
        Конструктор класса Animal.

        :param name: Имя животного.
        :param age: Возраст животного.
        """
        self._name = name
        self._age = age

    def make_sound(self) -> str:
        """
        Издать звук.

        :return: Строка с звуком, издаваемым животным.
        """
        return "Some generic animal sound"

    def __str__(self) -> str:
        """
        Возвращает строковое представление животного.

        :return: Строка с описанием животного.
        """
        return f"{self._name}, {self._age} years old"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление для использования в eval или при отладке.

        :return: Строка с описанием животного.
        """
        return f"Animal(name={self._name}, age={self._age})"


class Dog(Animal):
    """
    Дочерний класс, представляющий собаку.
    """

    def __init__(self, name: str, age: int, breed: str):
        """
        Конструктор класса Dog.

        :param name: Имя собаки.
        :param age: Возраст собаки.
        :param breed: Порода собаки.
        """
        super().__init__(name, age)
        self._breed = breed

    def bark(self) -> str:
        """
        Лаять.

        :return: Строка с звуком лая.
        """
        return "Woof! Woof!"

    def __str__(self) -> str:
        """
        Возвращает строковое представление собаки.

        :return: Строка с описанием собаки.
        """
        return f"{super().__str__()}, {self._breed} dog"



class Cat(Animal):
    """
    Дочерний класс, представляющий кошку.
    """

    def __init__(self, name: str, age: int, color: str):
        """
        Конструктор класса Cat.

        :param name: Имя кошки.
        :param age: Возраст кошки.
        :param color: Цвет кошки.
        """
        super().__init__(name, age)
        self._color = color

    def meow(self) -> str:
        """
        Мяукать.

        :return: Строка с звуком мяуканья.
        """
        return "Meow! Meow!"

    def __str__(self) -> str:
        """
        Возвращает строковое представление кошки.

        :return: Строка с описанием кошки.
        """
        return f"{super().__str__()}, {self._color} cat"
