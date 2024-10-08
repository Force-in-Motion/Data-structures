
class HashMap:
    def __init__(self):
        self.__count = 0
        self.__size = 1000 # Создаем по умолчанию количество ячеек динамического массива
        self.__array = [None] * self.__size # Создаем динамический массив, путем умножения None на количество определенных ранее ячеек self.__size = 1000

    def __hash(self, key) -> int:
        """
        Пропускает полученный ключ через hash функцию для получения текущего хэша переданного ключа, другими словами получаем случайный индекс типа int
        Динамического массива self.__array, по которому будет вставляться значение
        :param key: Принимает ключ
        :return: Возвращает полученный из функции хэш (индекс массива)
        """
        current_hash = hash(key)
        return current_hash % self.__size

    def add(self, key, value) -> bool:
        """
        Добавляет элемент в динамический массив если условия выполнены
        :param key: Принимает ключ
        :param value: Принимает значение, которое нужно добавить
        :return:
        """
        hash = self.__hash(key)  # Вызавыем функцию хэш и передаем ей ключ, получаем хэш (индекс массива self.__array)

        if not (self.__array[hash] is None):  # Проверяем, если по указанному хэшу (индексу) лежит не None, а любое другое значение, то возвращаем False
            return False

        self.__array[hash] = value  # Если все проверки пройдены успешно и по полученному хэшу лежит None то этой ячейке массива присваиваем новое значение

        self.__count += 1  # Увеличиваем количество элементов на 1

    def get(self, key) -> Exception or object:
        """
        Возвращает значение по полученному ключу
        :param key: Пренимает ключ
        :return: Возвращает значение
        """
        hash = self.__hash(key)  # Вызавыем функцию хэш и передаем ей ключ, получаем хэш (индекс массива self.__array)

        if self.__array[hash] is None:  # Проверяем, если по полученному ключу лежит значение None то выбрасываем исключение, поскольку ключ не соответствует значению
            raise Exception('Ключ не найден')

        return self.__array[hash]  # Иначе возвращаем значение

    def delete(self, key: any) -> bool or Exception:
        """
        Удаляет значение по полученному ключу если ключ существует в массиве
        :param key: Принимает ключ
        :return: Возвращает True or Exception
        """
        hash = self.__hash(key)

        if self.__array[hash] is None:
            raise Exception('Ключ не найден')

        self.__array[hash] = None

        self.__count -= 1

        return True