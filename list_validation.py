def create_task_list():
    return []


def add_to_list(list_task, task):
    pass


def size_of_list(list_task):
    pass


def list_contains(list_task, task):
    pass


def upper_task_in_tasklist(list_task):
    pass


def main():
    list_task = create_task_list()

    if not isinstance(list_task, list):
        print("Error: list_task is not a list")

    add_to_list(list_task, "task1")
    add_to_list(list_task, "task2")

    if size_of_list(list_task) != 2:
        print("Error: list size is not 2")

    if not list_contains(list_task, "task1"):
        print("Error: list does not contain task1")

    if not list_contains(list_task, "task2"):
        print("Error: list does not contain task2")

    task_list_upper = upper_task_in_tasklist(list_task)

    if not list_contains(task_list_upper, "TASK1"):
        print("Error: list does not contain TASK1")

    if not list_contains(task_list_upper, "TASK2"):
        print("Error: list does not contain TASK2")

    if size_of_list(task_list_upper) != 2:
        print("Error: list size is not 2")













if __name__ == "__main__":
    main()