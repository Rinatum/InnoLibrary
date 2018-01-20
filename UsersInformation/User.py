from abc import ABCMeta , abstractclassmethod , abstractproperty
class User():
    def __init__(self , name , cardNumber ):
        self.librCard = cardNumber
        self.name_in_system = name
    __metaclass__ = ABCMeta
    librCard = None
    name_in_system = None

class Librarian(User):
    def check_overdue(self):
        pass
    def add(self):
        pass
    def delete(self):
        pass
    def modify(self):
        pass

class Patron(User):
    def __init__(self , name , cardNumber , isFaculty):
        self.librCard = cardNumber
        self.name_in_system = name
        self.isFaculty = isFaculty
    def search_for(self):
        pass
    def check_out(self):
        pass
    def return_documents(self):
        pass







