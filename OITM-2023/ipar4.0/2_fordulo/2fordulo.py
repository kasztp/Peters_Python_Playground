def read_input(path: str) -> tuple:
    with open(path, 'r') as file:
        line = file.readline()
        width, height, x, y = [int(x) for x in line.split()]
        print(width, height, x, y)
        return width, height, x, y


def calculate_resolution(width: int, height: int, x: int, y: int) -> str:
    """Calculate the biggest possible x:y aspect ratio resolution on a screen,
    with the given width and height in pixels.

    Output can be only integer numbers in the format: "x_width y_height"
    
    If there is no solution, return "0 0".
    """
    # Calculate the maximum possible scale factor for the given aspect ratio
    scale = min(width // x, height // y)

    # If no valid scale factor can be found, return "0 0"
    if scale == 0:
        return "0 0"

    # Calculate the resolution using the scale factor
    res_width = x * scale
    res_height = y * scale

    # Return the resolution as a string in the format "x_width y_height"
    return f"{res_width} {res_height}"


if __name__ == "__main__":
    width, height, x, y = read_input("OITM-2023/ipar4.0/teszt_input_2forduló.txt")
    print(calculate_resolution(width, height, x, y))
    width, height, x, y = read_input("OITM-2023/ipar4.0/input_2forduló_6feladat.txt")
    print(calculate_resolution(width, height, x, y))
