def main() -> list[dict]:  # Функция, выполняемая только при запуске файла main.py
    """
        Функция, которая запускает функцию генератор, формирует список
        из 100 книг (список словарей) и записывает его в json файл
        Модель получает из conf.py
    """
    import json

    def generate(pk: int) -> dict[str, int, dict]:  # Функция, генерирующая книгу
        """
            Функция возвращает данные о книге

            :param pk: Идентификатор книги (целое число)
            :return: Словарь
        """
        from conf import MODEL
        import random
        from faker import Faker

        def title() -> str:
            '''
            Функция открывает файл books.txt и выбиравет случайное название книги

            :return: Название книги
            '''
            from itertools import islice
            title = open('books.txt', 'r', encoding="utf-8")#.readlines()
            
            #for i in range(len(title)):
                #title[i] = title[i].replace('\n', '')
            #return random.choice(title)
            start = random.randint(0,4)
            line = next(islice(title, start, start+1))
            line = line.replace('\n', '')
            return line
        def year() -> int:
            '''
           Функция генерирует год издания книги

           :return: Год издания книги - целое число
           '''
            return random.randint(1500, 2022)

        def pages() -> int:
            '''
             Функция генерирует количество страниц

             :return: Целое число - количество страниц
             '''
            return random.randint(10, 1000)

        def rating() -> float:
            '''
            Функция генерирует рейтинг книги (с округлением до сотых)

            :return: Число с плавающей точкой - рейтинг
            '''
            return round(random.uniform(0, 5), 2)

        def price() -> float:
            '''
            Функция генерирует цену книги (с округлением до сотых)

            :return: Число с плавающей точкой - цену
            '''
            return round(random.triangular() * 1000, 2)

        def isbn() -> str:
            '''
            Функция генерирует isbn-номер книги
            Задействует модуль fake

            :return: Код вниги в текстовом формате
            '''
            fake = Faker()
            return fake.isbn13()

        def author() -> list[str]:
            '''
                        Функция генерирует от 1 до 3 авторов книги
                        Задействует модуль fake

                        :return: Список с именами авторов
                        '''
            fake = Faker()
            authors = random.randint(1, 3)
            return_authors = []
            for i in range(authors):
                return_authors.append(fake.name())
            return return_authors

        library = {}
        library['model'] = MODEL
        library['pk'] = pk
        fields = {}

        fields['Title'] = title()
        fields['year'] = year()
        fields['pages'] = pages()
        fields['isbn130'] = isbn()
        fields['rating'] = rating()
        fields['price'] = price()
        fields['author'] = author()

        library['fields'] = fields
        return library

    pk = int(input('Введите id первой книги.\nЕсли хотите испоьзовать значение по-умолчанию, введите 1: '))
    list_of_book = []

    for i in range(100):
        list_of_book.append(generate(pk))
        pk += 1
    print(list_of_book)

    filename = open("list_of_books.json", "w", encoding="utf-8")
    filename.write(json.dumps(list_of_book, indent=4, ensure_ascii=False))
    filename.close()
    return list_of_book


if __name__ == "__main__":
    main()
