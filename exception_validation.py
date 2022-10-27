def start_exercice():
    catch_division_by_zero()
    catch_int_conversion_error()
    catch_your_own_exception()


def catch_division_by_zero():
    try:
        x = int(5)
        y = int(0)
        result = x / y
        return result
    except ZeroDivisionError:
        print("La division par zéro n'est pas autorisée")
    finally:
        print("Fin de catch_division_by_zero")


def catch_int_conversion_error():
    return int("a")


class MyAwesomeException:
    pass


def raise_my_own_exception():
    pass


def catch_your_own_exception():
    exception_catched = False
    try:
        raise_my_own_exception()
    except MyAwesomeException:
        exception_catched = True
    if not exception_catched:
        print("Error: MyAwesomeException not catched")


def main():
    try:
        start_exercice()
    except Exception:
        print("Error: Exception catched")


if __name__ == "__main__":
    main()
