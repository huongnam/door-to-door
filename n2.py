class BOOK:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return "{0} by {1}".format(self.title, self.title)
    def __len__(self):
        return self.pages
    def __del__(self):
        print("A book has been deleted")

abook = BOOK("nam", "NAM", 300)
print(abook)
str(abook)
# del abook
print(len(abook))
