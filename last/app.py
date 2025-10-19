def solve_case(A):
    n = len(A)

    # Build prefix XOR and frequency map of values over indices 0..n
    pref = 0
    freq = {0: 1}  # P[0] = 0
    for x in A:
        pref ^= x
        freq[pref] = freq.get(pref, 0) + 1

    # Total length sum over all subarrays
    total_length_sum = n * (n + 1) * (n + 2) // 6

    # S1 = sum C(c,2), S2 = sum C(c,3)
    S1 = 0
    S2 = 0
    for c in freq.values():
        if c >= 2:
            S1 += c * (c - 1) // 2
        if c >= 3:
            S2 += c * (c - 1) * (c - 2) // 6

    ans = total_length_sum - S1 - S2
    return ans


def main():
    # Read all lines from input.txt
    with open("input.txt", "r") as f:
        lines = f.read().strip().split("\n")

    T = int(lines[0])
    idx = 1
    results = []

    for t in range(1, T + 1):
        N = int(lines[idx])
        A = list(map(int, lines[idx + 1].split()))
        idx += 2

        ans = solve_case(A)
        results.append(f"Case #{t}: {ans}")

    # Write to output.txt
    with open("output.txt", "w") as f:
        f.write("\n".join(results) + "\n")


if __name__ == "__main__":
    main()