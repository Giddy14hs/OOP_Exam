class Book:
    def __init__(self, bookID, title, author, availability=True):
        self.bookID = bookID
        self.title = title
        self.author = author
        self.availability = availability

    def __str__(self):
        return f"BookID: {self.bookID}, Title: {self.title}, Author: {self.author}, Available: {self.availability}"

class Student:
    def __init__(self, studentID, name):
        self.studentID = studentID
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.availability:
            self.borrowed_books.append(book)
            book.availability = False
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.availability = True
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} does not have '{book.title}'")

    def __str__(self):
        books = ", ".join([book.title for book in self.borrowed_books])
        return f"StudentID: {self.studentID}, Name: {self.name}, Borrowed Books: {books}"

# Example usage
book1 = Book(1, "Python Basics", "Author A")
book2 = Book(2, "Data Structures", "Author B")
student = Student(101, "Alice")

student.borrow_book(book1)
student.return_book(book1)
print(student)
print(book1)
