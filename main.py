import sys

def get_word_count(text):
    return len(text.split())

def count_letters(text):
    lettercount = {
        "a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0,
        "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0,
        "u":0, "v":0, "w":0, "x":0, "y":0, "z":0
    }
    for char in text.lower():
        if char in lettercount:
            lettercount[char] += 1
    return lettercount

def sort_on(dict):
    return dict["num"]

def main():
    # Default path
    path = "books/frankenstein.txt"
    
    # If command line argument provided, use that path instead
    if len(sys.argv) > 1:
        path = sys.argv[1]
    #    print(f"Debug: Using path: {path}")  # used for debug for filepath
    
    with open(path) as f:
        file_contents = f.read()
    
    word_count = get_word_count(file_contents)
    lettercount = count_letters(file_contents)

    
    # Convert to list of dictionaries
    char_list = []
    for char, count in lettercount.items():
        char_list.append({"char": char, "num": count})
    
    # Sort the list
    char_list.sort(reverse=True, key=sort_on)
    
    # Print report
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")
    
    # Now use the sorted list to print results
    for char_dict in char_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
    
    print("--- End report ---")

if __name__ == "__main__":
    main()