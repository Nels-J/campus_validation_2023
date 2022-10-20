def create_people_by_age():
    return {}


def add_to_dict(peoples_by_age, name, age):
    return peoples_by_age.update({name: age})


def dict_contains(peoples_by_age, name):
    if name in peoples_by_age:
        return True


def age_of_people(peoples_by_age, name):
    return peoples_by_age[name]


def list_people(peoples_by_age):
    pass


def list_age(peoples_by_age):
    pass


def size_of_dict(peoples_by_age):
    return len(peoples_by_age)


def main():
    peoples_by_age = create_people_by_age()
    if not isinstance(peoples_by_age, dict):
        print("Error: peoples_by_age is not a dict")

    add_to_dict(peoples_by_age, "John Doe", 25)
    add_to_dict(peoples_by_age, "Robert Durand", 54)

    if size_of_dict(peoples_by_age) != 2:
        print("Error: dict size is not 2")

    if not dict_contains(peoples_by_age, "John Doe"):
        print("Error: dict does not contain John Doe")

    if not dict_contains(peoples_by_age, "Robert Durand"):
        print("Error: dict does not contain Robert Durand")

    if age_of_people(peoples_by_age, "John Doe") != 25:
        print("Error: age of John Doe is not 25")

    if age_of_people(peoples_by_age, "Robert Durand") != 54:
        print("Error: age of Robert Durand is not 54")

    if list_people(peoples_by_age) != ["John Doe", "Robert Durand"]:
        print("Error: list of people is not correct")

    if list_age(peoples_by_age) != [25, 54]:
        print("Error: list of age is not correct")


if __name__ == "__main__":
    main()
