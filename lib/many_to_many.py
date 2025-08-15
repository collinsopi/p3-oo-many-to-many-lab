class Book:
    all = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]


class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("book must be a Book instance")
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        # Author validation
        if not isinstance(author, Author):
            raise Exception("author must be an Author instance")
        self.author = author

        # Book validation
        if not isinstance(book, Book):
            raise Exception("book must be a Book instance")
        self.book = book

        # Date validation
        if not isinstance(date, str):
            raise Exception("date must be a string")
        self.date = date

        # Royalties validation
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")
        self.royalties = royalties

        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        if not isinstance(date, str):
            raise Exception("date must be a string")
        return [contract for contract in cls.all if contract.date == date]
