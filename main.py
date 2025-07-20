from stats import get_num_words, get_character_count

def get_book_text(book_path):
    with open(book_path) as book:
        book_contents = book.read()
    return book_contents 

def main():
    word_count = str(get_num_words("books/frankenstein.txt")) + " words found in the document"
    character_count = get_character_count("books/frankenstein.txt")

    print(word_count)
    print(character_count)
main() 