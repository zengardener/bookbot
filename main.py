# solution:
#def main():
#    book_path = "books/frankenstein.txt"
#    text = get_book_text(book_path)
#    num_words = get_num_words(text)
#    print(f"{num_words} words found in the document")
#
#
#def get_num_words(text):
#    words = text.split()
#    return len(words)
#
#
#def get_book_text(path):
#    with open(path) as f:
#        return f.read()

# My solution:
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        print(len(words))

    print(count_letters(file_contents))

def count_letters(file_contents):
    letters = []
    lowerized_letters = file_contents.lower()
    letter = list(lowerized_letters)
    return len(letters)

main()