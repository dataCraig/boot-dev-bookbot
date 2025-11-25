def word_count(book_text):
    words = book_text.split()
    return len(words)

def character_count(book_text):
    character_count = {}
    book_text = book_text.lower()

    for letter in book_text:
        character_count[letter] = character_count.get(letter, 0) + 1

    character_count = sorted(character_count.items(), key=lambda x: x[0], reverse=False)

    character_count = dict(character_count)
    return character_count

def sort_on(items):
    return items["count"]

def sorted_dictionary(books):
    sorted_dictionary = []
    for character, count in books.items():
        sorted_dictionary.append({'char': character, 'count': count})

    sorted_dictionary.sort(reverse=True, key=sort_on)
    return sorted_dictionary

