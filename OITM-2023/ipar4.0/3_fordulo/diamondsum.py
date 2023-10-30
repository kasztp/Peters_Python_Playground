import os


def load_input_files(prefix: str) -> list[list[str, int]]:
    """Load input files from the current path starting with prefix, and ending with .txt
    Return a list of lists containing the filename and the number contained in the given file.
    """
    files = []
    for file in os.listdir(os.getcwd()):
        if file.startswith(prefix) and file.endswith(".txt"):
            with open(file, "r") as f:
                files.append([file, int(f.readline())])
    return files


def calculate_diamond_sum(number: int) -> int:
    """Calculate the diamond sum for the given number.
    It is calculated from the number x number matrix, where the numbers are from 1 to number^2.
    The diamond sum is calculated as the below example shows.

    Example:
    1  2  3   4  5
    6  7  8   9 10
    11 12 13 14 15
    16 17 18 19 20
    21 22 23 24 25
    The diamond sum is 3 + 7 + 9 + 11 + 15 + 17 + 19 + 23 = 104.

    Return the diamond sum.
    """
    # TODO: implement this function properly



if __name__ == "__main__":
    files = load_input_files("teszt_input")
    print(f"Number of files: {len(files)}")
    print(f"Files: {files}")
    for file in files:
        print(f"{file[0]}: {calculate_diamond_sum(file[1]) % 987654321}")
