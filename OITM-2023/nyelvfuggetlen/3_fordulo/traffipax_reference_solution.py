#!/usr/bin/env python3

DAY_SECONDS = 24*3600


def solve(times:list, k:int):
  counts = [0] * DAY_SECONDS
  for t in times:
    counts[t] += 1
  
  # mozgóablak inicializálása
  sum = 0
  assert k < DAY_SECONDS
  for t in range(0, k+1):
    sum += counts[t]
  
  maxSum = sum
  for t in range(1, DAY_SECONDS):
    sum += counts[(t + k) % DAY_SECONDS] - counts[t - 1]
    if sum > maxSum:
      maxSum = sum
      
  assert 0 <= maxSum <= len(times)
  return maxSum


def solveFile(fn:str, fOut):
  with open(fn) as f:
    n, k = map(int, f.readline().strip().split())
    times = []
    for line in f:
      hour, min, sec = map(int, line.strip().split())
      assert 0 <= hour < 24
      assert 0 <= min < 60
      assert 0 <= sec < 60
      time = hour*3600 + min*60 + sec
      times.append(time)
  assert n
  assert k
  assert len(times) == n
  
  result = solve(times, k)

  message = "Output for %s: %s" % (fn, result)
  print(message)
  fOut.write(message+"\n")

  if "pelda" in fn:
    fnPeldaOut = fn.replace(".in.", ".out.")
    assert fnPeldaOut != fn
    with open(fnPeldaOut, "w") as fPeldaOut:
      fPeldaOut.write(str(result) + "\n")


def main():
  problemName = "traffipax"
  with open("out.txt", "w") as fOut:
    for i in range(1, 6):
      solveFile(problemName + "%s.in.txt" % (i,), fOut)
    for i in range(1, 3):
      solveFile(problemName + ".pelda%s.in.txt" % (i,), fOut)


if __name__ == "__main__":
  main()
