#!/usr/bin/env python3
import hashlib

class Point:
  def __init__(self, x, y):
    assert isinstance(x, int), x
    assert isinstance(y, int), y
    self._x = x
    self._y = y
    
  @property
  def x(self):
    return self._x
    
  @property
  def y(self):
    return self._y
  
  def __eq__(self, other):
    return self.x == other.x and self.y == other.y
  
  def __ne__(self, other):
    return not (self == other)
    
  def __neg__(self):
    return Point(-self.x, -self.y)

  def __add__(self, other):
    return Point(self.x + other.x, self.y + other.y)

  def __sub__(self, other):
    return Point(self.x - other.x, self.y - other.y)

def sgn(x):
  if x < 0:
    return -1
  if x > 0:
    return 1
  return 0

def rotate90Left(p:Point):
  return Point(-p.y, p.x)

def rotate90Right(p:Point):
  return Point(p.y, -p.x)

def dot(p, q):
  return p.x*q.x + p.y*q.y

def cross(p, q):
  return p.x*q.y - p.y*q.x
  
def sqrLen(p):
  return dot(p, p)
  
def segmentsIntersect(a, b, c, d):
  xc = cross(c-a, b-a)
  assert xc # különben a, b, c egy egyenesbe esne
  xd = cross(d-a, b-a)
  assert xd # különben a, b, d egy egyenesbe esne
  if sgn(xc) == sgn(xd):
    return False

  xa = cross(a-c, d-c)
  assert xa # különben a, c, d egy egyenesbe esne
  xb = cross(b-c, d-c)
  assert xb # különben b, c, d egy egyenesbe esne
  if sgn(xa) == sgn(xb):
    return False
    
  return True

def isColinear(a, b, c):
  return isParallel(b-a, c-a)
  
def isParallel(a, b):
  return cross(a, b) == 0
  
def categorizeQuad(q):
  assert len(q) == 4, q
  
  for i in range(4):
    if isColinear(q[i], q[(i+1)%4], q[(i+2)%4]):
      return "E"
      
  if segmentsIntersect(q[0], q[1], q[2], q[3]) or segmentsIntersect(q[1], q[2], q[3], q[0]):
    return "M"
    
  dAB = q[1] - q[0]
  dBC = q[2] - q[1]
  dCD = q[3] - q[2]
  dDA = q[0] - q[3]
  
  isParallelogram = (dAB == -dCD) and (dBC == -dDA)
  if isParallelogram:
    if dBC == rotate90Left(dAB) or dBC == rotate90Right(dAB):
      assert sqrLen(dBC) == sqrLen(dAB)
      return "N"
    if dot(dBC, dAB) == 0:
      return "T"
    if sqrLen(dBC) == sqrLen(dAB):
      return "R"
    return "P"
    
  if isParallel(dCD, dAB) or isParallel(dDA, dBC):
    return "Z"
  
  if (sqrLen(dAB) == sqrLen(dBC) and sqrLen(dCD) == sqrLen(dDA)) or \
    (sqrLen(dBC) == sqrLen(dCD) and sqrLen(dDA) == sqrLen(dAB)):
    return "D"
    
  return "L"

def solve(quads:list):
  result = "".join(map(categorizeQuad, quads))
  assert len(result) == len(quads)
  return result

def solveFile(fn:str, fOut):
  quads = []
  with open(fn) as f:
    for line in f:
      coords = tuple(map(int, line.strip().split()))
      assert len(coords) == 8
      quad = []
      for i in range(4):
        quad.append(Point(coords[2*i], coords[2*i+1]))
      quads.append(tuple(quad))
  assert quads
  
  s = solve(quads)
  hash = hashlib.sha256(s.encode("utf-8")).hexdigest()
  assert hash == hash.lower()

  message = "Output for %s: %s %s" % (fn, hash, hash.upper())
  print(message)
  fOut.write(message+"\n")

  if "pelda" in fn:
    fnPeldaOut = fn.replace(".in.", ".out.")
    assert fnPeldaOut != fn
    with open(fnPeldaOut, "w") as fPeldaOut:
      fPeldaOut.write(hash + "\n")
      fPeldaOut.write(s + "\n")

def main():
  problemName = "negyszog"
  with open("out.txt", "w") as fOut:
    for i in range(1, 6):
      solveFile(problemName + "%s.in.txt" % (i,), fOut)
    for i in range(1, 3):
      solveFile(problemName + ".pelda%s.in.txt" % (i,), fOut)

if __name__ == "__main__":
  main()
