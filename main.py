# My solution:
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        print(len(words))

    print(count_letters(file_contents))
    print(convert_dict_to_list(count_letters(file_contents)))


def count_letters(file_contents):
    letters = []
    counted_letters = {}
    lowerized_letters = file_contents.lower()
    letters = list(set(lowerized_letters))
    for i in letters:
        counted_letters[i] = lowerized_letters.count(i)
    return counted_letters

def sort_on(dict):
    return dict['occurence']

# Convert dict to list of dictionaries
def convert_dict_to_list(dict):
    list_of_letters = []
    dict_of_letters = {}
    # First, get each key/value pair which will be used to 
    # populate new list. Check if the key is letter since
    # this is what is needed, other chars are irelevant.
    # From the valid key/value pair, create new dict that
    # will have name of the key to which the original key 
    # will be assigned as value, then name of the value
    # to which the original value will be assigned.
    # This is so that we can sort it easily later.
    for k, v in dict.items():
        if k.isalpha():
            dict_of_letters['letter'] = k
            dict_of_letters['occurence'] = v
            # print(dict_of_letters)
            list_of_letters.append(dict_of_letters)
            # Set dict to empty at the loop end so that 
            # next run will have again just one instance
            # of letter and value and will not be accumulated.
            dict_of_letters = {}
    
    sorted_letters=sorted(list_of_letters, reverse=True, key=sort_on)
    return sorted_letters

main()