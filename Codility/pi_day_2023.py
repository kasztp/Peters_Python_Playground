from collections import Counter

def solution(P: str, Q: str) -> int:
    """ Generate a list of len(P) == len(Q) length strings that can be obtained from the string P and Q by selecting a character from either P or Q for a given position.
        Then select the string where the number of distinct characters is the smallest.
        Return the number of different characters in the selected string. """
    p_counts = Counter(P)
    q_counts = Counter(Q)
    combo_counts = Counter(P + Q)
    word = ""
    for i in range(len(P)):

        if p_counts[P[i]] < q_counts[Q[i]] or combo_counts[P[i]] < combo_counts[Q[i]]:
            word += Q[i]
        elif p_counts[P[i]] > q_counts[Q[i]] or combo_counts[P[i]] > combo_counts[Q[i]]:
            word += P[i]
        elif P[i] in word:
            word += P[i]
        elif Q[i] in word:
            word += Q[i]
        else:
            word += P[i]
    return len(Counter(word))


if __name__ == '__main__':
    print(solution("ABC", "BCD"))
    print(solution("ABCD", "ADDR"))
    print(solution("ABCD", "ABCD"))
    print(solution("ABCD", "AAAA"))
    print(solution("xye", "yxb"))
    print(solution("dcba", "cbad"))
