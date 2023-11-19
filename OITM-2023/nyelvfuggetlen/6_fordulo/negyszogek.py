import os
import hashlib


def load_data(file_name: str) -> list[list[int]]:
    with open(os.path.join(os.getcwd(), file_name), "r") as f:
        t = [[int(number) for number in numbers.split()] for numbers in f.readlines()]
        t_points = []
        for quad in t:
            points = []
            for i in range(0, len(quad), 2):
                points.append((quad[i], quad[i+1]))
            t_points.append(points)
        print(t_points)
        return t_points


def distance(p1: tuple[int, int] , p2: tuple[int, int]) -> float:
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5


def area(p1: tuple[int, int], p2: tuple[int, int], p3: tuple[int, int]) -> float:
    return abs(p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1])) / 2.0


def classify_quadrilateral(points: list[tuple[int, int]]) -> str:
    # TODO: Fix this function to match sample outputs.

    A, B, C, D = points
    AB = distance(A, B)
    BC = distance(B, C)
    CD = distance(C, D)
    DA = distance(D, A)
    AC = distance(A, C)
    BD = distance(B, D)

    if any((A == B, B == C, C == D, D == A)) or not any((area(A, B, C), area(B, C, D), area(C, D, A), area(D, A, B))):
        return 'E'  # Degenerate

    if AB == BC == CD == DA:  # All sides are equal
        if AC == BD:  # Diagonals are equal
            return 'N'  # Square
        return 'R'  # Rhombus

    if AB == CD and BC == DA:  # Opposite sides are equal
        if AC == BD:  # Diagonals are equal
            return 'T'  # Rectangle
        return 'P'  # Parallelogram

    if (AB == CD or BC == DA) and AC != BD:  # One pair of opposite sides are equal
        return 'Z'  # Trapezoid

    if AB == BC and CD == DA and AC != BD:
        return 'D'  # Deltoid

    if (AB + BC > AC and BC + CD > BD) or (AB + DA > AC and DA + CD > BD):
        return 'M'  # Self-intersecting

    return 'L'  # General quadrilateral


if __name__ == "__main__":
    quadrilaterals = load_data("negyszog.pelda1.in.txt")
    classifications = [classify_quadrilateral(q) for q in quadrilaterals]
    classification_string = ''.join(classifications)
    print(classification_string)
    hash_object = hashlib.sha256(classification_string.encode())
    hex_dig = hash_object.hexdigest()
    print(hex_dig)
