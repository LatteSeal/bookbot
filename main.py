def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        # print(file_contents)
        words = number_of_words(file_contents)
        # print(character_count(file_contents))
        character_count_list = character_count(file_contents)
        report(character_count_list, words)

def number_of_words(text):
    return len(text.split())

def character_count(text):
    lowered_text = text.lower()
    character_count = {}
    character_count_list = []

    for letter in lowered_text:
        if letter in character_count and letter.isalpha():
            character_count[letter] += 1
        elif letter.isalpha():
            character_count[letter] = 1

    for character in character_count:
        character_count_list.append({"letter": character, "num": character_count[character]})

    def sort_on(dict):
        return dict["num"]
    
    character_count_list.sort(reverse=True, key=sort_on)
    return character_count_list

def report(character_count_list, number_of_words):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{number_of_words} words found in the document")
    for character in character_count_list:
        print(f"The {character['letter']} character was found {character['num']} times")
    print("--- End report ---")

main()