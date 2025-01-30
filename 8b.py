def count_file_details():
    with open("sample.txt", "w") as f:
        for _ in range(5):
            line = input("Enter a line of text: ")
            f.write(line + "\n")
    
    with open("sample.txt", "r") as f:
        text = f.read()
        upper = sum(1 for c in text if c.isupper())
        lower = sum(1 for c in text if c.islower())
        digits = sum(1 for c in text if c.isdigit())
        print("Uppercase letters:", upper)
        print("Lowercase letters:", lower)
        print("Digits:", digits)

count_file_details()
