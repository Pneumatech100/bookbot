def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
    return file_content
from stats import string_word_count
from stats import string_character_count
from stats import report
import sys

def main():
   # path ="books/franken(stein.txt"
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  
    path = sys.argv[1] 
    book_text = get_book_text(path)
    words =string_word_count(book_text)
    chardict = string_character_count(book_text)
    #print(book_text)
    #print(f"{words} words found in the document.")
    #print(chardict)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    rep = report(book_text)
    for item in rep:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()