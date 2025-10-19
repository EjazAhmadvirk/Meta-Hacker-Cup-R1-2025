def solve_game(s: str) -> str:
    l, r = 0, len(s) - 1
    alice_turn = True

    while l <= r:
        if alice_turn:
            # Alice needs an 'A' in [l, r]; eat the leftmost one and drop the prefix
            while l <= r and s[l] != 'A':
                l += 1
            if l > r:  # no 'A' available
                return "Bob"
            l += 1        # remove up to and including this 'A'
            alice_turn = False
        else:
            # Bob needs a 'B' in [l, r]; eat the rightmost one and drop the suffix
            while l <= r and s[r] != 'B':
                r -= 1
            if l > r:  # no 'B' available
                return "Alice"
            r -= 1        # remove from this 'B' to the end
            alice_turn = True

    # If interval becomes empty, the player who just moved took the last dish,
    # so the *next* player has no move and loses. That’s handled in-loop.
    # This line won’t normally be reached, but default to the opponent of the last mover:
    return "Bob" if alice_turn else "Alice"


# I/O stays the same
with open('input.txt', 'r', encoding='utf-8') as infile:
    lines = infile.readlines()

results = []
t = int(lines[0].strip())
line_idx = 1

for case_num in range(1, t + 1):
    n = int(lines[line_idx].strip())
    s = lines[line_idx + 1].strip()
    line_idx += 2

    result = solve_game(s)
    results.append(f"Case #{case_num}: {result}")

with open('output.txt', 'w', encoding='utf-8') as outfile:
    outfile.write('\n'.join(results) + '\n')
