def left(i):
  return 2*i+1 

def right(i):
  return 2*i+2

def parent(i):
  if i!=0:
    if(i%2!=0):
      return (i//2)
    else:
      return (i//2)-1
  else:
    return None

def Heapify(A, i):
  print(A)
  l = left(i)
  r = right(i)
  print("Debug heapify: l=",l," r=",r)
  if l<= len(A) and A[l] > A[i]:
    largest = l
  else:
    largest = i
  if r<= len(A) and A[r] > A[largest]:
    largest = r
  if i!=largest:
    A[largest], A[i] = A[i], A[largest]
    return Heapify(A, largest)
  else:
    return A


def build(A):
  for i in range(len(A)//2, 0, -1):
    print("Starting iteration: i=", i)
    print("A: ", A)
    A = Heapify(A[::], i)
    print("Finished iteration: ", i)
    