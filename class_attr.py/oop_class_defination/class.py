# class Book:

#     def __init__(self, title, author, pages,price) :

#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.price = price


#     def getprice(self):
        
#         if hasattr(self, "discount"):

#             return self.price - (self.price * self.discount)
#         else:

#            return self.price

    
#     def setprice(self, amount):

#         self.discount = amount



# class Newspaper:

#     def __init__(self, name) -> None:
#          self.name =  name



# book = Book("why we code", "Abdul_Muizz", "150", 250)
# news = Newspaper("Observer News")
# news2 = Newspaper("Daily news paper")
# #compare two types together
# # print(type(book) == type(news))
# # print(type(news) == type(news2))

# # object is instance of a class

# print (isinstance(book, Book))
# print(isinstance(news, Newspaper))
# print(isinstance(news2, Book))
# print(isinstance(news2, object))

# # print(book.getprice())
# # book.setprice(0.3)
# # print (book.getprice())


class Books_Type:

    Book_Types = ["HardCover", "PaperCover", "Ebook"]

    __books = None

    @staticmethod
    def get_books():
       if Books_Type.__books == None:
          Books_Type.__books = []
       return Books_Type.__books

    @classmethod
    def get_booktype(cls):
        return cls.Book_Types
    

    def __init__(self, name, booktype) -> None:
       self.name = name

       if (not booktype in Books_Type.Book_Types):
           raise ValueError("book does not exist")
       else:
        self.book_types = booktype

print ("book types is ", Books_Type.Book_Types)

b1  = Books_Type("why er code", "HardCover")
b2  = Books_Type("why er code", "Ebook")

listbook = Books_Type.get_books()
listbook.append(b1)
listbook.append(b2)
print(listbook)