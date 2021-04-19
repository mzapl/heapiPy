def left(i, size):
  return 2*i+1 if 2*i+1<size else None

def right(i, size):
  return 2*i+2 if 2*i+2<size else None


def Heapify(A, size, i):
  print(A)
  l = left(i, size)
  r = right(i, size)
  largest = i
  if l:
    if l< size and A[l] > A[i]:
      largest = l
  if r:
    if r< size and A[r] > A[largest]:
      largest = r
  if i!=largest:
    A[largest], A[i] = A[i], A[largest]
    return Heapify(A, size, largest)
  else:
    return A

def build(A, size):
  for i in range(size//2, -1, -1):
    # print("\n"+"-"*15+"\n")
    # print("Starting iteration: i=", i)
    # print("A: ", A)
    A = Heapify(A[::], size, i)
    # print("Finished iteration: ", i)
  return A

def heapSort(A, size):
  A = build(A[::], size)
  for i in range(size-1, 0, -1):
    A[0], A[i] = A[i], A[0]
    A = Heapify(A[::], i, 0)
  return A


def div():
  print("-"*15)

# def parent(i):
#   if i!=0:
#     if(i%2!=0):
#       return (i//2)
#     else:
#       return (i//2)-1
#   else:
#     return None