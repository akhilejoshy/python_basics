# class students:
#     def __init__(self,student_name,roll,age):
#         self.s=student_name
#         self.r=roll
#         self.a=age
#     def display(self):
#         print(self.s)
#         print(self.r)
#         print(self.a)
#
# stud=students('akhil',12,22)
# stud.display()

#Q create a class library_management
# init /initialize the library name
#and set a public varible books=[]
# add book (title)
# remove boo(title)
# list of books()

class library:
    def __init__(self,lib_name='new library',books=[]):
        self.lib_name=lib_name
        self.books=books
    def add_book(self,book):
        self.books.append(book)
    def remove_book(self,book):
        if book in self.books:
            self.books.remove(book)
        else:
            print('book not found')
    def list_book(self):
        print('library name=',self.lib_name)
        print(self.books)
lib=library()
lib.add_book('python')
lib.add_book('java')
lib.add_book('c++')
lib.remove_book('c++')
lib.list_book()