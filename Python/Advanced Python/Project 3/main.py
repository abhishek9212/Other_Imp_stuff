class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in this Library are:")
        for book in self.books:
            print(' *' + book) # We can use enumerate if we want to list with 1, 2, 3 etc...

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f'You have been issued {bookName}. Please keep it safe and return it within 30 days')
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print('Thanks for returing this book! Hope you enjoyed reading it. Have a great day ahead!')

class Student:
    # def __init__(self):
    #     self.bookList = []

    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book
         # self.bookList.append(reqBook)

    def returnBook(self):
        self.book = input("Enter the name of the book you want to add/return: ")
        return self.book
       


if __name__ == "__main__":
    centralLibrary = Library(['Algorithms', 'Django', 'Clrs', 'Python Notes'])
    student = Student()
    # centralLibrary.displayAvailableBooks()
    while(True):
        welcomeMsg = '''\n ===== Welcome to Central Library =====
        Please choose an option:
        1.List all the books
        2.Request a book
        3.Add/Return a book
        4.Exit the Library
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))

        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing Central Library. Have a great day ahead!\n")
            exit()
        else:
            print('Invalid choice!\n')
        