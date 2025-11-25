import sys

def get_book_text(filepath):
    with open(filepath) as f:
        filecontents = f.read()
        return filecontents

def main():
    from stats import word_count, character_count, sorted_dictionary

    # Check if a file argument was supplied
    if len(sys.argv) == 1:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    else:
        book_text = get_book_text(sys.argv[1])
        #book_text = get_book_text("./books/frankenstein.txt")
        num_words = word_count(book_text)
        characters = character_count(book_text)
        sorted_characters = sorted_dictionary(characters)
        #print(f'Found {num_words} total words')
        #print(characters)

    # Printing a report
    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    for entry in sorted_characters:
        if entry['char'].isalpha():
            print(f'{entry['char']}: {entry['count']}')
    print('============= END ===============')
    sorted_dictionary(characters)
main()



