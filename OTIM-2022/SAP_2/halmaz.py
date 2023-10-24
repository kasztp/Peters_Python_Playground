import os

path = os.getcwd() + "/OTIM-2022/SAP_2/"


def number_of_results(n: int) -> int:
        input_set = list(range(1, n+1))
        result_set = []

        for x in input_set[::-1]:
            if x * 2 not in result_set:
                result_set.append(x)

        #print(f"N: {n}, Halmaz: {input_set} --> {result_set}")
        print(f"Input: {n} Output: {len(result_set)}")
        c = 0
        for i in range(n+1):
            #if 2**i >= n//2:
            #    break
            increase = (n - 2**i)//(2**(i+1)) + 1
            if increase == 1:
                break
            print(f"{i} | {2**i}: {increase}")
            c += increase
        print(f"Output with Calc: {c}")
        return(c)


for filename in os.listdir(path):
    if filename.endswith(".in.txt"):
        print(filename)
        with open(path + filename, "r", encoding="utf8") as f:
            n = int(f.readline().strip())

        input_set = list(range(1, n+1))
        result_set = []

        for x in input_set[::-1]:
            if x * 2 not in result_set:
                result_set.append(x)

        #print(f"N: {n}, Halmaz: {input_set} --> {result_set}")
        print(f"Input: {n} Output: {len(result_set)}")
        c = 0
        for i in range(1, n+1):
            increase = (n - 2**i)//(2**(i+1)) + 1
            print(f"{i} | {2**i}: {increase}")
            if increase == 0:
                break
            c += increase
        print(f"Output with Calc: {c}")
