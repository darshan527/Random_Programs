def pascalTriangle(n) -> int:
    """
    Pascal's triangle is a triangular array
    with binomial co-efficients.
    N = 6
    1                        1
    2                    1       1
    3                1       2       1
    4            1       3       3       1
    5        1       4       6       4       1
    6    1       5       10      10      5       1    

    Nth element can be calculated using: nCr = (nCr-1 * (n-r+1)) / r
    """

    prev = 1
    print(prev, end=" ")
    for i in range(1, n + 1):
        cur = (prev * (n - i + 1)) // i
        print(cur, end=" ")
        prev = cur


n = int(input())
pascalTriangle(n)