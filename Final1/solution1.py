from math import isqrt

def best_divisor_leq_A(B: int, A: int) -> int:
    """
    Return the largest d | B with d <= A, in O(sqrt(B)).
    """
    if A >= B:
        return B
    if B % A == 0:
        return A

    best = 1
    # Scan up to sqrt(B), checking both i and B//i
    r = isqrt(B)
    for i in range(1, r + 1):
        if B % i == 0:
            # i is a divisor
            if i <= A and i > best:
                best = i
            j = B // i  # paired divisor
            if j <= A and j > best:
                best = j
            # Early exit: if we already hit A, it's optimal
            if best == A:
                break
    return best


def solve():
    # Fast file I/O while keeping your input/output file contract
    with open("input.txt", "r", encoding="utf-8") as fin:
        T = int(fin.readline().strip())
        results = []

        for case_idx in range(1, T + 1):
            N, A, B = map(int, fin.readline().split())

            D = best_divisor_leq_A(B, A)
            # Build the sequence:
            # [1, 1, ..., 1, D] + [1, 1, ..., 1, B//D]
            first_half = [1] * (N - 1) + [D]
            second_half = [1] * (N - 1) + [B // D]
            seq = first_half + second_half

            results.append(f"Case #{case_idx}: " + " ".join(map(str, seq)))

    with open("output.txt", "w", encoding="utf-8") as fout:
        fout.write("\n".join(results))


if __name__ == "__main__":
    solve()
