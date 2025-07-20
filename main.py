from stats import get_num_words

def get_book_text(book_path):
    with open(book_path) as book:
        book_contents = book.read()
    return book_contents 

def main():
    print(str(get_num_words("books/frankenstein.txt")) + " words found in the document")

main() 