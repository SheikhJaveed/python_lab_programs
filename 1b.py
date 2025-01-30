def string_length_tuples():
    strings = ["apple", "banana", "cherry", "date"]
    result = [(s, len(s)) for s in strings]
    result.sort(key=lambda x: x[1])  # Sort by length of the string
    print(result)

string_length_tuples()
