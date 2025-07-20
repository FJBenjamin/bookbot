def get_book_text(book_path):
    with open(book_path) as book:
        book_contents = book.read()
    return book_contents 

def num_words(book_path):
    return len(get_book_text(book_path).split())


def main():
    print(str(num_words("books/frankenstein.txt")) + " words found in the document")

main() 