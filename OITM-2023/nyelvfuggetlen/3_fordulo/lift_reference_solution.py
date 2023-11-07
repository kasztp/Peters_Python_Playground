#!/usr/bin/env python3
import itertools


def calculateDP(weights, dp, i, k, w):
  N = len(weights)
  if k == 0:
    return 1 if w == 0 else 0
  if i == N or w == 0:
    return 0
  result = dp[i+1, k, w]
  if weights[i] <= w:
    result += dp[i+1, k-1, w-weights[i]]
  return result


def solve(weights:list, K, W):
  N = len(weights)
  assert N
  assert 1 <= K < N
  assert W
  
  dp = {}
  for i in range(N, -1, -1):
    for k in range(0, K+1):
      for w in range(0, W+1):
        dp[i, k, w] = calculateDP(weights, dp, i, k, w)
    
  return dp[0, K, W]


# A lassú megoldás.
def solveBruteForce(weights:list, K, W):
  allIndices = list(range(len(weights)))
  result = 0
  for indexList in itertools.combinations(allIndices, K):
    if sum(weights[i] for i in indexList) == W:
      result += 1
  return result


def solveFile(fn:str, fOut):
  with open(fn) as f:
    n, k, w = map(int, f.readline().strip().split())
    weights = list(map(int, f.readline().strip().split()))
  assert len(weights) == n
  assert all(x > 0 for x in weights)
  
  result = solve(weights, k, w)

  message = "Output for %s: %s" % (fn, result)
  print(message)
  fOut.write(message+"\n")

  if "pelda" in fn:
    fnPeldaOut = fn.replace(".in.", ".out.")
    assert fnPeldaOut != fn
    with open(fnPeldaOut, "w") as fPeldaOut:
      fPeldaOut.write(str(result))


def main():
  problemName = "lift"
  with open("out.txt", "w") as fOut:
    for i in range(1, 6):
      solveFile(problemName + "%s.in.txt" % (i,), fOut)
    for i in range(1, 3):
      solveFile(problemName + ".pelda%s.in.txt" % (i,), fOut)


if __name__ == "__main__":
  main()
