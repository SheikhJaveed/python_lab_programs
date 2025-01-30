def filter_odd_numbers():
    import random
    numbers = [random.randint(10, 10000) for _ in range(20)]
    print("Random Numbers:", numbers)
    
    odd_numbers = [num for num in numbers if num % 2 != 0 and (len(str(num)) == 2 or len(str(num)) == 4)]
    print("Filtered Odd Numbers:", odd_numbers)

filter_odd_numbers()
