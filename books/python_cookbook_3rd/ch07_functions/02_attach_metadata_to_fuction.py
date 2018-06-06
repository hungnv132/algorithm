
def attach_metadata_to_function_arguments():
    """
    - Problem: You would like to attach some additional information to the
    arguments
    - Solution: Function argument annotations.
    """

    def add(x: int, y: int) -> int:
        return x + y

    print(add(2, 3))  # 5


if __name__ == '__main__':
    attach_metadata_to_function_arguments()