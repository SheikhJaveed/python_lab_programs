def handle_exceptions():
    try:
        name = int("hello")
    except NameError:
        print("NameError occurred")
    except IndexError:
        print("IndexError occurred")
    except KeyError:
        print("KeyError occurred")
    except ZeroDivisionError:
        print("ZeroDivisionError occurred")
    finally:
        print("Exception handling complete")

handle_exceptions()
