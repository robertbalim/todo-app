FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Read and extract the to-do items from a text file

    :param filepath: The default string path specifying the text file to be read.
    :return: Return a list of to-do items
    """

    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos_param, filepath=FILEPATH):
    """
    Write in a text file the list of to-do items

    :param todos_param: A non-default list of to-do items to be written into the text file.
    :param filepath: The default string path specifying the text file for writing.
    :return: none
    """

    with open(filepath, 'w') as file:
        file.writelines(todos_param)


def parse(feet_inches):
    """
    Extract the feet and inches and return a dictionary

    :param feet_inches: Non-default string parameter
    :return: Return a dictionary of feet and inches
    """
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    return {"feet": feet, "inches": inches}


def convert(feet, inches):
    """
    Conversion of feet and inches to meters

    :param feet: Non-default float parameter
    :param inches: Non-default float parameter
    :return: Return a converted meters based on feet and inches
    """
    meters = feet * 0.3048 + inches * 0.0254
    return meters


def count(phrase):
    return phrase.count('.')


if __name__ == "__main__":
    print("Hello World")
    print(get_todos())