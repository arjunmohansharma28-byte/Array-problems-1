def reverse(n):
    arr, i, j = list(range(1, n + 1)), 0, n - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr

print("  reverse(4) =", reverse(4))
print("  reverse(5) =", reverse(5))
n = int(input("Enter list size ( try 6 or 7): "))

print("left and right swap and move inward untill they meet in the middle")
print(" reverse(" + str(n) +") =", reverse(n))