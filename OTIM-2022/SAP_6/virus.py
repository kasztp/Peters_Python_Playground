import multiprocessing
import os

path = os.getcwd() + "/OTIM-2022/SAP_6/"


def find_most_severe_virus(genome: str) -> int:
    """ Generate a viruses from a genome. Return the most severe virus severity.
        A virus is a string of the genome that contains n occurrences of each of the characters V,I,R,U,S in that order.
        The  virus can  be  generated  by  removing  any  number  of  characters  from  the  genome.
        The virus can't contain any other characters than V,I,R,U,S.
        The severity of the virus is the number n of occurrences of each character in the virus.

    Parameters
    ----------
    genome : str
        Genome

    Returns
    -------
    int
        Severity of the virus
        0 if there is no virus.
    """
    return None


def generate_possible_viruses(genome: str) -> list:
    """ Generate a viruses from a genome. Return the list of viruses.
        A virus is a string of the genome that contains n occurrences of each of the characters V,I,R,U,S in that order.
        The  virus can  be  generated  by  removing  any  number  of  characters  from  the  genome.
        The virus can't contain any other characters than V,I,R,U,S.

    Parameters
    ----------
    genome : str
        Genome

    Returns
    -------
    list
        List of viruses
    """
    result_list = []
    for i in range(len(genome)):
        for j in range(i, len(genome)):
            virus = genome[i:j + 1]
            if virus.count('V') == virus.count('I') == virus.count('R') == virus.count('U') == virus.count('S'):
                result_list.append(virus)
    print(result_list)
    return result_list


if __name__ == '__main__':
    for filename in sorted(os.listdir(path)):
        if filename.endswith(".in.txt"):
            with open(path + filename, "r", encoding="utf8") as f:
                text = f.readline().strip()
            result = find_most_severe_virus(text)
            print(f"{filename} --> {result}")
