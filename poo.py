class ToDolist():
    def __init__(self):
        self.list = list()
    def append(self, task):
        self.list.append(task)

    def __iter__(self):
        return iter(self.list)

    def __len__(self):
        return len(self.list)

    def upper_task_in_tasklist(self):
        new_list = ToDolist()
        for task in self:
            new_list.append(task.upper())
        return new_list


def create_task_list():
    return ToDolist()


def add_to_list(list_task, task):
    list_task.append(task)


def size_of_list(list_task):
    return len(list_task)


def list_contains(list_task, task):
    return task in list_task


def upper_task_in_tasklist(list_task):
    return list_task.upper_task_in_tasklist()


def main():
    list_task = create_task_list()

    if not isinstance(list_task, ToDolist):
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
