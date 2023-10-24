def dino_reader(filename):
    """ Reads a file from the given input path,
        where each line contains the mass and the length of each dinosaur.
        Returns a list of tuples, where each tuple contains the mass and the length of a dinosaur.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()
        dinos = []
        for line in lines:
            mass, length = line.split()
            dinos.append((int(mass), int(length)))
        return dinos


def dino_sorter(dinos):
    """ Gives the number of dinosaurs that can not be eaten by any other dinosaurs.
        Returns the number of dinosaurs that can not be eaten by any other dinosaurs.

        A dino can be eaten only if it is smaller in both mass and length than the other dino.
    """
    dinos.sort()
    #print(dinos)
    count = 0
    for i, dino in enumerate(dinos):
        for j in range(i+1, len(dinos)):
            if dino[0] < dinos[j][0] and dino[1] < dinos[j][1]:
                break
        else:
            count += 1
    return count


from collections import namedtuple

Dinosaur = namedtuple('Dinosaur', ['mass', 'length'])

Dinosaur.__lt__ = lambda self, other: self.mass <= other.mass or self.length <= other.length
Dinosaur.__gt__ = lambda self, other: self.mass > other.mass and self.length > other.length


def dino_sorter_nt(dinos):
    """ Gives the number of dinosaurs that can not be eaten by any other dinosaurs.
        Returns the number of dinosaurs that can not be eaten by any other dinosaurs.

        A dino can be eaten only if it is smaller in both mass and length than the other dino.
    """
    dinos = [Dinosaur(*dino) for dino in dinos]
    dinos.sort()
    print(dinos)
    print(dinos[0] > dinos[1])
    count = 0
    for i, dino in enumerate(dinos):
        if all(dino > other for other in dinos[i+1:]):
            count += 1
    return count


if __name__ == "__main__":
    dinos = dino_reader("OITM-2023/nyelvfuggetlen/dino.pelda1.in.txt")
    #print(dinos)
    print(dino_sorter_nt(dinos))
