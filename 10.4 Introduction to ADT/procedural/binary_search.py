"""
This program is intended to demonstrate a static memory allocation approach to implementing a Binary Search Tree.

* Note: We are infact doing dynamic memory allocation in the init() phase to initially construct the BST

"""
import numpy


def init():
  """

  """
  tree_list = []

  for i in range(0,10):
    #       value, leftP, rightP
    node = [0,     i+1,   -1]
    tree_list.append(node)
  return numpy.asarray(tree_list)

def insert(value):
  global bst, rootP, freeP

  currentP = rootP
  if freeP == -1:
    print("Error -- no room")
    return
  found = False

  if rootP == -1:
    rootP = freeP
    found = True

  while not found:
    if bst[currentP][0] == value:
      print("error -- value already exists")
      return
    elif bst[currentP][0] > value:
      if bst[currentP][1] != -1:
        currentP = bst[currentP][1]
      else:
        bst[currentP][1] = freeP
        found = True
    else:
      if bst[currentP][2] != -1:
        currentP = bst[currentP][2]
      else:
        bst[currentP][2] = freeP
        found = True

  bst[freeP][0] = value
  temp = freeP
  freeP = bst[freeP][1]
  bst[temp][1] = -1

# Our global variables
freeP = 0
rootP = -1
bst = init()

print("Initially:")
print(bst)
print("----")
for v in [99,80,200,40,85,125,250]:
  print("inserting",v)
  insert(v, freeP, rootP)
  print("free",freeP,"rootP",rootP)
  print(bst)
  print("--------")