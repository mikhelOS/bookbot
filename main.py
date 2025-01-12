def sort_on(list):
    return list.sort(key=lambda x: x[1], reverse=True)

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = 0
        char_count = {}
        lowercase = file_contents.lower()
        lowercase_words = lowercase.split()

        words = file_contents.split()
        chars = list("".join(lowercase_words))
        for char in chars:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        sorted_chars = dict(sorted(char_count.items(), reverse=True))
        new_char_count = [(l, c) for l, c in sorted_chars.items()]
        # print(type(new_char_count))
        sort_on(new_char_count)
        char_count = tuple()
        char_count = new_char_count
        # print(type(char_count))
        word_count = len(words)
        print("--- Begin Report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")
        print(" ")
        for x, y in char_count:
            if x.isalpha():
                print(f"The '{x}' character was found '{y}' times")
            else:
                pass
        print("--- End report ---")

main()
