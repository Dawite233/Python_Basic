class Author:
    def __init__(self, name):
        self.name = name
        self.books = []


    def publish(self, title):
        self.books.append(title)

    def __str__(self):
        titles = ', '.join(self.books) or 'No published books'
        return f'{self.name}. Books: {titles}'

def main():

    rowling = Author('J. K. Rowling')
    rowling.publish('Harry Potter and The Philosopher\'s Stone')
    rowling.publish('Fantastic Beasts and Where to find Them')



    print(rowling)




dawit = Author('Fearless')
print(dawit)

main()