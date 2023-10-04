class Book:  # Создание объекта КНИГА с параметрами
    def __init__(self, title: str, author: str, year: int, genre: str, aviable: bool = True) -> None:
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.aviable = aviable  # есть ли в наличии


class Reader:  # Создание объекта ЧИТАТЕЛЬ с параметрами
    def __init__(self, id: int, name: str, borrowed_books: list = []) -> None:
        self.id = id
        self.name = name
        self.borrowed_books = borrowed_books  # Арендованые книги

    def borrow_book(self, book: Book) -> None:  # Взять книгу
        self.borrowed_books.append(book)

    def return_book(self, book: Book) -> None:  # Вернуть книгу
        self.borrowed_book.remove(book)


class Library:  # Создание объека БИБЛИОТЕКА с параметрами
    def __init__(self, catalog_book: dict = dict(), readers: list = []) -> None:
        self.catalog_book = catalog_book
        self.readers = readers

    def add_book(self, book: Book, isbn: int) -> None:  # Добавить книгу в библиотеку
        self.catalog_book[isbn] = book

    def remove_book(self, title: str, author: str) -> None:  # Удалить книгу из библиотеки
        for isbn in self.catalog_book:
            book = self.catalog_book[isbn]
            if book.title == title and book.author == author:
                del self.catalog_book[isbn]
                break

    def search_by_title(self, title: str) -> list:  # Поиск всех книг по имени
        res = list()
        for isbn in self.catalog_book:
            book = self.catalog_book[isbn]
            if book.title == title:
                res.append(isbn)
        return res

    def search_by_author(self, author: str) -> list:  # Поиск всех книг по автору
        res = list()
        for isbn in self.catalog_book:
            book = self.catalog_book[isbn]
            if book.author == author:
                res.append(isbn)
        return res

    def search_by_genre(self, genre: str) -> list:  # Поиск всех книг по жанру
        res = list()
        for isbn in self.catalog_book:
            book = self.catalog_book[isbn]
            if book.genre == genre:
                res.append(isbn)
        return res

    def get_all_books(self) -> list:  # Вывод всех книг с параметрами
        res = list()
        for isbn in self.catalog_book:
            book = self.catalog_book[isbn]
            res.append(
                f'{book.title}, {book.author}, {book.year}, {book.genre}')
        return res

    def get_reader(self, reader: Reader) -> None:  # Добавить читателя в библиотеку
        self.readers.append(reader)

    def remove_reader(self, reader_id: int) -> None:  # Удалить читателя из библиотеки
        for reader in self.readers:
            if reader_id == reader.id:
                self.readers.remove(reader)
                break

    # список всех взятых читателем книг
    def list_borrowed_books(self, reader_id: int) -> list:
        for reader in self.readers:
            if reader_id == reader.id:
                return reader.borrowed_books

    # взять книгу из библиотеки читателем
    def checkout_book(self, reader_id: int, isbn_book: int) -> None:
        if self.catalog_book[isbn].aviable == True:
            for isbn in self.catalog_book:
                if isbn == isbn_book:
                    for index, reader in enumerate(self.readers):
                        if reader.id == reader_id:
                            self.readers[index].borrowed_books.append(
                                self.catalog_book[isbn])
                            self.catalog_book[isbn].aviable = False
                            break
                    break

    # вернуть книгу взятую читателем из библиотеки
    def checkin_book(self, reader_id: int, isbn_book: int) -> None:
        if self.catalog_book[isbn].aviable == False:
            for isbn in self.catalog_book:
                if isbn == isbn_book:
                    for index, reader in enumerate(self.readers):
                        if reader.id == reader_id:
                            if self.catalog_book[isbn] in self.readers[index].borrowed_books:
                                self.readers[index].borrowed_books.remove(
                                    self.catalog_book[isbn])
                                self.catalog_book[isbn].aviable = True
                                break
                    break
