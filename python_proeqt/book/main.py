import json


def file_reader():
    with open("book.json", mode="r", encoding="utf-8") as file:
        read_file = json.load(file)
        return read_file

class Book():
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        
    def add_book(self):
        books = file_reader()
        book_list = {"title": self.title,
         "author": self.author,
         "year": self.year}
        books.append(book_list)
        with open("book.json", mode="w", encoding="utf-8") as file:
            json.dump(books, file, indent=2)
        print("file is add")


    
                
class Book_manager():
   

    def book_list(self):
        print(f"{"title":<20} {"author":<25} {"year"}")
        print("=" * 55)
        for book  in file_reader():
           
            print(f"{book["title"]:<20} {book["author"]:<25} {book["year"]}")
            print("-" * 55)

    def search_book(self):
        input_title = input("enter title... ")
      
        for book in file_reader():
            book_lower = book["title"]
             
            if input_title.lower() in book_lower.lower():
                print(book)

    def first(self):
      choose = 0
      while choose != 4:

        print("-" * 40)
        print("* enter 1 for book list ")
        print("-" * 40)
        print("* enter 2 for add book in list ")
        print("-" * 40)
        print("* enter 3 for search in  book list ")
        print("-" * 40)
        print("* enter 4 for exit")
        print("-" * 40)

        try:
            choose = int(input("... "))
        except ValueError:
            print("enter only number...")

        if choose == 1:
            book2 = Book_manager()
            print(book2.book_list())

        elif choose == 2:

            title = input("enter title ")
            author = input("enter author ")
            try:
                year = input("year ")
            except ValueError:
                print("enter only number...")

            book1 = Book(title, author, year)
            print(book1.add_book())
        
        elif choose == 3:

            book2 = Book_manager()
            print(book2.search_book())
        
        elif choose == 4:
            print("Good bye...")
            break
        
        else:
            print("Error...")



functional = Book_manager()
functional.first()


