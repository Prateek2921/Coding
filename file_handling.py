count = int(input("How many books do you want to enter? "))
books = []

class Books:
    def __init__(self , title , author , pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display (self):
        print(f'Title:{self.title}\nAuthor:{self.author}\nPages:{self.pages} ')

    def is_long(self):
        if self.pages>300:
            print('This is a long book')
        else:
            print('This is a short book')

for i in range(count):
    title = input('Title of the book:')
    author = input('Author of the book:')
    pages = int(input('Number of pages in the book:'))

    book = Books(title , author , pages)
    books.append(book) 

for b in books:
    b.display()
    b.is_long()
    print()
