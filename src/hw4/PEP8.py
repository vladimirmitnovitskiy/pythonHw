import itertools as it


def count_queens(n):
    count = 0

    for permutation in it.permutations(range(n)):
        is_valid = True

        for i in range(n):
            for j in range(i + 1, n):
                if abs(i - j) == abs(permutation[i] - permutation[j]):
                    is_valid = False
                    break
            if not is_valid:
                break

        if is_valid:
            count += 1

    return count


if __name__ == "__main__":
    n = int(input())
    print(count_queens(n))
