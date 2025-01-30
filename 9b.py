def multiple_exceptions():
    try:
        num = int(input("Enter a number: "))
        result = 10 / num
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except ValueError:
        print("Invalid input, not an integer")
    else:
        print(f"Result is {result}")
    finally:
        print("Execution finished")

multiple_exceptions()
