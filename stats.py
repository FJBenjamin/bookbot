def get_num_words(book_path):
    with open(book_path) as book:
        num_words = len(book.read().split())
    return num_words
