#!/usr/bin/env python3

# Unió-Holvan adatstruktúra
class DisjointSet:
  def __init__(self):
    self.parent = {}
  
  def getGroup(self, i:int):
    path = []
    while True:
      p = self.parent.get(i, i)
      if p == i:
        for x in path:
          assert x != i
          self.parent[x] = i
        return i
      path.append(i)
      i = p
  
  def union(self, iGroup:int, jGroup:int):
    assert iGroup != jGroup
    assert iGroup not in self.parent
    assert jGroup not in self.parent
    self.parent[iGroup] = jGroup

    
def solveFile(fn:str, fOut):
  edges = []
  with open(fn) as f:
    n, m  = map(int, f.readline().strip().split())
    for _ in range(m):
      i, j, cost = map(int, f.readline().strip().split())
      assert 0 <= i < n
      assert 0 <= j < n
      assert i != j
      assert 0 <= cost
      edges.append((i, j, cost))
  
  edges.sort(key = lambda elem: elem[2])
  
  disjointSet = DisjointSet()
  totalCost = 0
  nComponents = n
  if nComponents > 1:
    for i, j, cost in edges:
      iGroup = disjointSet.getGroup(i)
      jGroup = disjointSet.getGroup(j)
      if iGroup != jGroup:
        disjointSet.union(iGroup, jGroup)
        totalCost += cost
        nComponents -= 1
        if nComponents == 1:
          break
  
  assert nComponents == 1
  
  result = totalCost
  message = "Output for %s: %s" % (fn, result)
  print(message)
  fOut.write(message+"\n")

  if "pelda" in fn:
    fnPeldaOut = fn.replace(".in.", ".out.")
    assert fnPeldaOut != fn
    with open(fnPeldaOut, "w") as fPeldaOut:
      fPeldaOut.write(str(result))

def main():
  with open("out.txt", "w") as fOut:
    for i in range(1, 6):
      solveFile("utak%s.in.txt" % (i,), fOut)
    for i in range(1, 3):
      solveFile("utak.pelda%s.in.txt" % (i,), fOut)

if __name__ == "__main__":
  main()
