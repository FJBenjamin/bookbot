def get_book_text(book_path):
    with open(book_path) as book:
        book_contents = book.read()
    return book_contents 

def main():
    print(get_book_text("books/frankenstein.txt"))

main() 