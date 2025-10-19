def solve():
    with open("input.txt", "r") as fin:
        T = int(fin.readline().strip())
        cases = [tuple(map(int, fin.readline().split())) for _ in range(T)]
    
    results = []
    for i, (N, A, B) in enumerate(cases, 1):
        # Find a divisor D of B that is <= A
        D = 1
        for x in range(A, 0, -1):
            if B % x == 0:
                D = x
                break
        
        # Construct the sequence
        first_half = [1] * (N - 1) + [D]
        second_half = [1] * (N - 1) + [B // D]
        seq = first_half + second_half

        results.append(f"Case #{i}: " + " ".join(map(str, seq)))

    with open("output.txt", "w") as fout:
        fout.write("\n".join(results))


if __name__ == "__main__":
    solve()
