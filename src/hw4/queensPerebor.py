import itertools as iter





def count_queens(n):
    count = 0

    for p in iter.permutations(range(n)):
        ok = True

        for i in range(n):
            for j in range(i+1,n):
                if abs(i-j) == abs(p[i]-p[j]):
                    ok = False
                    break
            if not ok:
                break
        if ok:
            count += 1
    return count



n = int(input())

print(count_queens(n))




