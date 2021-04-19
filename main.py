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
        A = Heapify(A, size, i)
    return A


def heapSort(A, size):
    A = build(A, size)
    for i in range(size - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        A = Heapify(A, i, 0)
    return A


def div():
    print("\n", "-" * 30, "\n")


def main():
    examples = [
        [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0],
        [84, 22, 19, 10, 3, 17, 6, 5, 9],
        [16, 4, 10, 14, 7, 9, 3, 2, 8, 1],
        [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    ]
    for example in examples:
        size = len(example)
        print("start:", example)

        wynik = build(example, size)
        print("build:", wynik)

        wynik = heapSort(example, size)
        print("heapsort:", wynik)

        div()


main()
