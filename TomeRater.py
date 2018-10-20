#Add User Class
class User(object):
    def __init__(self, name, email):
        self.uname = name
        if type(name) == str and type(email) == str and email.count("@") == 1 and (email[-4:]==".com" or email[-4:]==".edu" or email[-4:]==".org"):
            self.name = name
            self.email = email
            self.books = {}
            print("User '{n}' has been created".format(n=self.name))
        else:
            if type(name) != str:
                print("User '{u}' cannot be created. Invalid name. Please enter name as text".format(u=self.uname))
            if type(email) != str or email.count("@") != 1 or (email[-4:]!=".com" or email[-4:]!=".edu" or email[-4:]!=".org"):
                print("User '{u}' cannot be created. Invalid email. Please enter email as text and ensure one '@' symbol is used with extension '.com', '.edu', or '.org'".format(u=self.uname))

    def get_email(self):
        if hasattr(self, "email"):
            return self.email
        else:
            print("Cannot get email. No User attributes exist for user '{u}'. User was not propertly defined".format(u=self.uname))

    def change_email(self, address):
        if hasattr(self, "email"):
            if type(address) == str and address.count("@") == 1:
                self.email = address
                print("The email address for user '{n}' has been updated to '{e}'".format(n=self.name, e=self.email))
            else:
                print("Email not changed for user '{n}'. Please enter email as text and ensure one '@' symbol is used".format(u=self.name))
        else:
            print("Cannot change email. No User attributes exist for user '{u}'. User was not propertly defined".format(u=self.uname))

    def __repr__(self):
        try:
            count = 0
            for book in self.books:
                count += 1
            return "User {n}, email: {e}, books read: {c}".format(n=self.name, e=self.email, c=count)
        except AttributeError:
            return "No User attributes exist for user '{u}'. User was not propertly defined".format(u=self.uname)

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email

    def read_book(self, book, rating):
        if hasattr(book, "isbn"):
            self.books[book] = rating
            print("Book '{b}' has been added to user '{u}'.".format(b=book.bname, u=self.name))
        else:
            print("Book '{b}' not added to user '{u}'. Book is not a valid book object".format(b=book.bname, u=self.name))

    def get_avg_rating(self):
        if hasattr(self, "email"):
            count = 0
            total = 0
            for book in self.books:
                if self.books[book] != None:
                    count += 1
                    total += self.books[book]
            try:
                return round(total / count, 1)
            except ZeroDivisionError:
                print("No avg book rating for '{u}'. User has not rated any books".format(u=self.name))
        else:
            print("Cannot get avg rating. No User attributes exist for user '{u}'. User was not propertly defined".format(u=self.uname))


class Book(object):
    def __init__(self, title, isbn, price):
        isbn = str(isbn)
        self.bname = title
        if type(title) == str and isbn.count("-") == 0 and (len(isbn) == 10 or len(isbn) == 13) and type(price) == float:
            self.title = title
            self.isbn = int(isbn)
            self.price = price
            self.ratings = []
            print("Book '{b}' has been created".format(b=self.title))
        else:
            if type(title) != str:
                print("Book '{t}' cannot be created. Invalid title. Please enter title as text".format(t=title))
            if isbn.count("-") != 0 or (len(isbn) != 10 and len(isbn) != 13):
                print("Book '{t}' cannot be created. Invalid isbn. Please enter the isbn as a 10 or 13 digit number without spaces or dashes".format(t=title))
            if type(price) != float:
                print("Book '{t}' cannot be created. Invalid price. Please enter price with dollars and cents".format(t=title))

    def get_title(self):
        if hasattr(self, "title"):
            return self.title
        else:
            print("A title attribute does not exist for book '{b}'. Book was not propertly defined".format(b=self.bname))

    def get_isbn(self):
        if hasattr(self, "isbn"):
            return self.isbn
        else:
            print("An isbn attribute does not exist for book '{b}'. Book was not propertly defined".format(b=self.bname))

    def get_price(self):
        if hasattr(self, "price"):
            return self.price
        else:
            print("A price attribute does not exist for book '{b}'. Book was not propertly defined".format(b=self.bname))

    def set_isbn(self, nisbn):
        if hasattr(self, "isbn"):
            nisbn = str(nisbn)
            if nisbn.count("-") == 0 and (len(nisbn) == 10 or len(nisbn) == 13):
                self.isbn = nisbn
                print("The isbn for book '{b}' has been updated to '{i}'".format(b=self.title, i=self.isbn))
            else:
                print("ISBN not changed. Please enter the isbn as a 10 or 13 digit number without spaces or dashes")
        else:
            print("ISBN not changed. No Book attributes exist for book '{b}'. Book was not propertly defined".format(b=self.bname))

    def set_price(self, nprice):
        if hasattr(self, "price"):
            if type(nprice) == float:
                self.price = nprice
                print("The price for book '{b}' has been updated to '{p}'".format(b=self.title, p=self.price))
            else:
                print("Price not changed. Please enter the price with dollars and cents")
        else:
            print("No Book attributes exist for book '{b}'. Book was not propertly defined".format(b=self.bname))

    def add_rating(self, rating):
        try:
            if rating != None:
                if rating >= 0 and rating < 5:
                    self.ratings.append(rating)
                    print("A rating of '{r}' has been added to book '{t}'".format(r=rating, t=self.title))
                else:
                    print("Invalid rating for book '{b}'. Please enter a rating from 0 to 4".format(b=self.title))
        except AttributeError:
            return "Rating not added for book '{b}'. No Book attributes exist. Book was not properly defined".format(b=self.bname)

    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn

    def get_avg_rating(self):
        if hasattr(self, "ratings"):
            count = 0
            total = 0
            for rating in self.ratings:
                count += 1
                total += rating
            try:
                return round (total / count,1)
            except ZeroDivisionError:
                print("Cannot get avg rating for book '{b}'. Book has not been rated".format(b=self.title))
        else:
            print("Cannot get avg rating. No Book attributes exist for user '{b}'. Book was not propertly defined".format(b=self.bname))


    def __repr__(self):
        try:
            return "'{t}'".format(t=self.title)
        except AttributeError:
            return "No Book attributes exist for book '{b}'. Book was not propertly defined".format(b=self.bname)

    def __hash__(self):
        return hash((self.title, self.isbn))


class Fiction(Book):
    def __init__(self, title, author, isbn, price):
        super().__init__(title, isbn, price)
        if hasattr(self, "isbn"):
            self.author = author

    def get_author(self):
        if hasattr(self, "isbn"):
            return self.author
        else:
            print("An author attribute does not exist for book '{b}'. Book was not properly defined".format(b=self.bname))

    def __repr__(self):
        try:
            return "'{t}' by {a}".format(t=self.title, a=self.author)
        except AttributeError:
            return "No Book attributes exist for book '{b}'. Book was not properly defined".format(b=self.bname)



class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn, price):
        super().__init__(title, isbn, price)
        if hasattr(self, "isbn"):
            self.subject = subject
            self.level = level

    def get_subject(self):
        if hasattr(self, "isbn"):
            return self.subject
        else:
            print("A subject attribute does not exist for book '{b}'. Book was not properly defined".format(b=self.bname))

    def get_level(self):
        if hasattr(self, "isbn"):
            return self.level
        else:
            print("A level attribute does not exist for book '{b}'. Book was not properly defined".format(b=self.bname))

    def __repr__(self):
        try:
            return "'{t}' a/an {l} manual on {s}".format(t=self.title, l=self.level, s=self.subject)
        except AttributeError:
            return "No Book attributes exist for book '{b}'. Book was not properly defined".format(b=self.bname)


class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn, price):
        return Book(title, isbn, price)

    def create_novel(self, title, author, isbn, price):
        return Fiction(title, author, isbn, price)

    def create_non_fiction(self, title, subject, level, isbn, price):
        return Non_Fiction(title, subject, level, isbn, price)

    def add_book_to_user(self, book, email, rating=None):
        if hasattr(book, "isbn"):
            if email in self.users:
                self.users[email].read_book(book, rating)
                book.add_rating(rating)
                if book in self.books:
                    self.books[book] += 1
                else:
                    self.books[book] = 1
            else:
                print("No user with email {e}".format(e=email))
        else:
            print("Book '{b}' not added to {e}. Book argument entered is not a valid book object. Please create a book/novel/non-fiction object".format(b=book.bname, e=email))

    def add_user(self, name, email, user_books=None):
        self.users[email] = User(name, email)
        if user_books != None:
            if type(user_books) == list:
                for book in user_books:
                    try:
                        if len(book) > 2:
                            print("Some user books not added. Items in user_book list cannot have more than two arguments")
                        elif len(book) == 2:
                            self.add_book_to_user(book[0], email, book[1])
                    except TypeError:
                        self.add_book_to_user(book, email)
            else:
                print("User books not added. user_books attribute must be a list")

    def print_catalog(self):
        for book in self.books:
            print(book)

    def print_users(self):
        for user in self.users:
            print(self.users[user])

    def most_read_book(self):
        count = 0
        most_read_val = 0
        most_read_book = []
        for book in self.books:
            if self.books[book] >= most_read_val:
                most_read_val = self.books[book]
        for book in self.books:
            if self.books[book] == most_read_val:
                count += 1
                most_read_book.append(book)
        if count > 1:
            print("{c} books were read the most; each read {n} times. They are:".format(c=count, n=most_read_val))
            for book in most_read_book:
                print(book)
        elif count == 1:
            print("The most read book is {b}, read {n} times".format(b=most_read_book[0], n=most_read_val))
        else: print("No books have been read")
        #return most_read_book

    def highest_rated_book(self):
        count = 0
        high_rating_val = 0
        ratings = []
        high_rating_book = []
        for book in self.books:
            avg_rating = book.get_avg_rating()
            if avg_rating != None and avg_rating >= high_rating_val:
                ratings.append([book, avg_rating])
                high_rating_val = avg_rating
        for rating in ratings:
            if rating[1] == high_rating_val:
                count += 1
                high_rating_book.append(rating[0])
        if count > 1:
            print("{c} books are rated the highest; each has an average rating of {r}. They are:".format(c=count, r=high_rating_val))
            for book in high_rating_book:
                print(book)
        elif count == 1:
            print("The highest rated book is {b}, with an average rating of {r}".format(b=high_rating_book[0], r=high_rating_val))
        else: print("No books have been read")
        #return high_rating_book

    def most_positive_user(self):
        count = 0
        most_positive_val = 0
        positive_vals = []
        most_positive_users = []
        for user in self.users:
            avg_rating = self.users[user].get_avg_rating()
            if avg_rating != None and avg_rating >= most_positive_val:
                positive_vals.append([self.users[user].name, avg_rating])
                most_positive_val = avg_rating
        for val in positive_vals:
            if val[1] == most_positive_val:
                count += 1
                most_positive_users.append(val[0])
        if count > 1:
            print("{c} users are the most positive; each has an average book rating of {r}. They are:".format(c=count, r=most_positive_val))
            for user in most_positive_users:
                print(user)
        elif count == 1:
            print("The most positive user is '{u}', with an average book rating of {r}".format(u=most_positive_users[0], r=most_positive_val))
        else: print("No users have rated books")
        #return most_positive_users

    def get_n_most_expensive_books(self, n):
        book_prices = {}
        count = 0
        for book in self.books:
            count += 1
        if n <= count:
            for book in self.books:
                book_prices[book.title] = book.price
            sbooks = sorted(book_prices.items(), reverse = True, key = lambda kv: kv[1])
            print("The {n} most expensive books are:".format(n=n))
            for i in range(n):
                print(sbooks[i])
        else:
            print("Requested number of books is too high. Only {c} books exist".format(c=count))
