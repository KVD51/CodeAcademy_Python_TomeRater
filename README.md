# TomeRater
This is a project I completed while learning Python

Files included:
1- TomeRater.py
2- populate.py

TomeRater.py is a program that allows users to read and rate books. The purpose of the program is to illustrate knowledge of basic Python syntax as well as lists, loops, strings, dictionaries, and control flow. The program is not intended to be used by consumers as a true rating app - though, it could be used for fun by people who know the command line and Python.

Classes:
There are five different classes that interact with one another.
1- User: create users object
2- Book: create book object
3- Fiction: subclass of Book for fiction books
4- Non_Fiction: subclass of Book for non-fiction books
5- TomeRater: links User and Book classes

Functions/Methods:
5- TomeRater:
    create_book(title, isbn, price)
    create_novel(title, author, isbn, price)
    create_non_fiction(title, subject, level, isbn, price)
    add_book_to_user(book, email, rating=None)
    add_user(name, email, user_books=None)
    print_catalog()
    print_users()
    most_read_book()
    highest_rated_book()
    most_positive_user()
    get_n_most_expensive_books(n)

*There are more functions within the other classes. See code.

*The populate.py file has some code that will use TomeRater.py to run some examples. Try running the file.

*Example use of code:

from TomeRater import *

Tome_Rater = TomeRater()

#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 1234567891, 34.00)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 8767954325, 45.50)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452090, 22.50)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")

#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)

#Some output
Tome_Rater.print_catalog()
Tome_Rater.print_users()
Tome_Rater.most_positive_user()
Tome_Rater.highest_rated_book()

