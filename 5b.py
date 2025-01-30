def text_file_operations():
    with open("sample.txt", "w") as f:
        for _ in range(5):
            line = input("Enter a line of text: ")
            f.write(line + "\n")
    
    with open("sample.txt", "r") as f:
        words = f.read().split()
        longest_word = max(words, key=len)
        shortest_word = min(words, key=len)
        print("Longest Word:", longest_word, "Length:", len(longest_word))
        print("Shortest Word:", shortest_word, "Length:", len(shortest_word))

text_file_operations()
