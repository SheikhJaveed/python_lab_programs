def word_meanings():
    dictionary = {
        "Python": "A programming language",
        "Algorithm": "A step-by-step procedure for solving a problem",
        "Data": "Facts and statistics collected for analysis"
    }
    
    while True:
        print("\nMenu:")
        print("1. Add entry")
        print("2. Search for a word")
        print("3. Find words with same meaning")
        print("4. Remove entry")
        print("5. Display sorted words")
        print("6. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            word = input("Enter word: ")
            meaning = input("Enter meaning: ")
            dictionary[word] = meaning
        elif choice == 2:
            word = input("Enter word to search: ")
            print(f"Meaning of {word}: {dictionary.get(word, 'Word not found')}")
        elif choice == 3:
            meaning = input("Enter meaning to search for words: ")
            words = [word for word, mean in dictionary.items() if mean == meaning]
            print("Words with same meaning:", words)
        elif choice == 4:
            word = input("Enter word to remove: ")
            dictionary.pop(word, None)
        elif choice == 5:
            for word in sorted(dictionary.keys()):
                print(f"{word}: {dictionary[word]}")
        elif choice == 6:
            break

word_meanings()
