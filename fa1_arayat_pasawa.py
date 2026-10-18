
class Publication:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)


class Book(Publication):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.set_number_of_pages(pages)

    def set_number_of_pages(self, pages):
        if pages > 0:
            self.__pages = pages
        else:
            print("The number of pages must be positive.")
            self.__pages = 0

    def get_number_of_pages(self):
        return self.__pages

    def display_info(self):
        super().display_info()
        print("Pages:", self.__pages)


class Magazine(Publication):
    def __init__(self, title, author, issue):
        super().__init__(title, author)
        self.set_issue_number(issue)

    def set_issue_number(self, issue):
        if issue > 0:
            self.__issue = issue
        else:
            print("The issue number must be positive.")
            self.__issue = 0

    def get_issue_number(self):
        return self.__issue

    def display_info(self):
        super().display_info()
        print("Issue Number:", self.__issue)


pub1 = Publication("Psychology Journal", "Ratchiff")
pub2 = Publication("Science Today", "John Smith")

book1 = Book("The Hobbit", "Tolkien", 310)
book2 = Book("Harry Potter", "Rowling", 350)

mag1 = Magazine("National Geographic", "Various Authors", 202)
mag2 = Magazine("Time Magazine", "Various Authors", 150)

print("PUBLICATIONS")
pub1.display_info()
pub2.display_info()

print("\nBOOKS")
book1.display_info()
book2.display_info()

print("\nMAGAZINES")
mag1.display_info()
mag2.display_info()
