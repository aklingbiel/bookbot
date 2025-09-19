import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text(sys.argv[1])
    return text

from stats import count_words
from stats import character_count
from stats import sorted_characters

#print(f'{count_words(main())} words found in the document')
#print(character_count(main()))

print(f'''============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------''')
print(f'''Found {count_words(main())} total words
--------- Character Count -------''')
ch_count_list = sorted_characters(character_count(main()))
for entry in ch_count_list:
    if entry["char"].isalpha():
        print(f'{entry["char"]}: {entry["num"]}')
print('============= END ===============')