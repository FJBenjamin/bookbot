def get_num_words(book_path):
    with open(book_path) as book:
        num_words = len(book.read().split())
    return num_words

def get_character_count(book_path):
    char_dict = {}
   
    with open(book_path) as book:
        char_list = list(book.read().lower())

        for char in char_list:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1

    return char_dict 
