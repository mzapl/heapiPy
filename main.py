from sized import Heapify, left, right, build, heapSort, div

myarr = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
# prawidłowy? wynik [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
myarr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
# prawidłowy? wynik [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
myarr = [12, 11, 13, 5, 6, 7]

myarr = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]

myarr = [84, 22, 19, 10, 3, 17, 6, 5, 9]



div()
size = len(myarr)
print("start:", myarr)

div()
wynik = build(myarr, size)
print("build:", wynik)

div()
wynik = heapSort(myarr[::], size)
print("heapsort:", wynik)

div()