def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def Heapify(A, size, i):
    largest = i
    l = left(i)
    r = right(i)

    if l < size and A[l] > A[i]:
        largest = l

    if r < size and A[r] > A[largest]:
        largest = r

    if i != largest:
        A[largest], A[i] = A[i], A[largest]
        return Heapify(A, size, largest)

    else:
        return A


def build(A, size):
    for i in range(size // 2, -1, -1):
        A = Heapify(A[::], size, i)
    return A


def heapSort(A, size):
    A = build(A[::], size)
    for i in range(size - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        A = Heapify(A[::], i, 0)
    return A


def div():
    print("\n", "-" * 30, "\n")


def parent(i):
    if i != 0:
        if i % 2 != 0:
            return i // 2
        else:
            return i // 2 - 1
    else:
        return None
