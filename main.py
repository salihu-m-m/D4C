from stats import count_words, count_characters, sorted_characters
import sys

def get_book_text(filepath): # 
    with open(filepath, 'r') as f: 
        contents = f.read() 
    return contents

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
def main():
    path =sys.argv[1]
    text =get_book_text(path)
    num_of_words = count_words(text)
    num_of_char = count_characters(text)
    sorted = sorted_characters(num_of_char)             
    print("============ BOOKBOT ============\n" 
f"Analyzing book found at {path}...\n"
"----------- Word Count ----------\n"
f"Found {num_of_words} total words\n"
"--------- Character Count -------")
    for item in sorted:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
   
main()
