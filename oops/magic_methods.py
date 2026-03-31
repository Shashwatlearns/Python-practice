class Book:
    def __init__(self,title,author, num_pages):
        self.title=title
        self.author=author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self,other):
        return self.title == other.title and self.author == other.author

    def __lt__(self,other):
        return self.num_pages < other.num_pages

    def __gt__(self,other):
        return self.num_pages > other.num_pages

    def __add__(self,other):
        return f"{self.num_pages + other.num_pages} pages"

    def __contains__(self,keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self,key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"'{key}' was not found in {self.title}"

book1=Book("Crime And Punishment","F.D.",400)
book2=Book("Harry Potter","J.K. Rowling",320)
book3=Book("Concepts Of Physics","H.C. Verma",450)
book4=Book("Crime And Punishment","F.D.",2)

print(book1)
print(book2)
print(book3)

print(book1 == book4)
print(book1 < book4)
print(book1 > book4)
print(book1 + book3)

print("Concepts" in book3)
print("H.C." in book3)

print(book1["title"])
print(book2["author"])
print(book3["num_pages"])
print(book4["colour"])
