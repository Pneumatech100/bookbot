
def string_word_count(book_text):
    words = book_text.split()
    return len(words)



def string_character_count(book_text):
    text =book_text.lower()
    characters = {}
    for character in text:
        if character not in characters:
            characters[character] = 1
        else:
            characters[character] +=1 
    return characters

def sort_on(character):
    return character["num"]

def report(book_text):
    words = string_word_count(book_text)
    chardict = string_character_count(book_text)
    counts = {}
    dictlist = []
    for char, count in chardict.items():
        if char.isalpha():
            dictlist.append({"char": char, "num": count})
    dictlist.sort(reverse=True, key=sort_on)
    return dictlist
#print("============ BOOKBOT ============")
#print("Analyzing book found at books/frankenstein.txt...")
#print (f"Found{string_word_count('books/frankenstein.txt')} Total Words")
#for item in dictlist:
 #   print(f"{item['char']}: {item['num']}")
