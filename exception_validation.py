def start_exercice():
    catch_division_by_zero()
    catch_int_conversion_error()
    catch_your_own_exception()


def catch_division_by_zero():
    try:
        return 5 / 0
    except ZeroDivisionError as e:
        print(e.__class__)


def catch_int_conversion_error():
    try:
        return int("a")
    except ValueError as e:
        print(e.__class__)


class MyAwesomeException(Exception):
    pass


def raise_my_own_exception():
    raise MyAwesomeException


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
