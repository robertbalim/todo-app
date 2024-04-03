FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Read a textfile and return a todo items.
    :param filepath:
    :return: To-do items:
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Open a textfile and write the todo items
    :param todos_arg:
    :param filepath:
    :return:
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
