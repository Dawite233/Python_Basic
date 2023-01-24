# Creatign class author 

class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

# This is the publisheing method

    def publish(self, title):
        title=title.lower()
        

        if title in self.books:
            print('The book is already in the books that given\n! This program does not allowed duplicated')
        else:
            self.books.append(title)


    # _str_ methos checking the authors published books 


    def __str__(self):
        if self.books:
            titles = ', '.join(self.books)
        else:
            titles = ' There is no books that published'
        return f'name { self.name}. Books. { titles}'



def main():
    Daniel = Author('Daniel Migos')
    Daniel.publish('Fearless')
    Daniel.publish('Attraction')
    Daniel.publish('Humble')
    print(Daniel)

    Rebecca = Author('Rebecca Peter')
    Rebecca.publish('Fearless')
    Rebecca.publish('Summmer Time')
    Rebecca.publish('Ring it up')
    Rebecca.publish('Ring it up')
    print(Rebecca)



    Andrew = Author('Andrew Jackson')
    Andrew.publish('The Harmonial Man')
    Andrew.publish('The present afe adn inner life')
    Andrew.publish('Death and afeter life')
    Andrew.publish('Man\'s pysychological condition adn powers')
    print(Andrew)


main()

