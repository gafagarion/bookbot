def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print_report(book_path,num_words,chars_dict)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def convert_dict(chars_dict):
    def sort_on(dict):
        return dict["num"]
    
    list_dict = []
    for key in chars_dict:
        if key.isalpha():
            list_dict.append({"name":key,"num":chars_dict[key]})
    list_dict.sort(reverse=True,key=sort_on)
    return list_dict

def print_report(book_path,num_words,chars_dict):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    for character in convert_dict(chars_dict):
        print(f"The '{character["name"]} character was found {character["num"]} times'")
    print("--- End report ---")

main()