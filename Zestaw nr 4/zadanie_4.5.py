def odwracanie_iteracyjne(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

    return L

def odwracanie_rekurencyjne(L, left, right):
    if left < right:
        L[left], L[right] = L[right], L[left]
        odwracanie_rekurencyjne(L, left + 1, right - 1)

    return L

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list)
odwracanie_iteracyjne(list, 1, 7)
print(list)

print()

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list2)
odwracanie_rekurencyjne(list2, 1, 7)
print(list2)
