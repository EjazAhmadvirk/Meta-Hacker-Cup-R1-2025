def solve_game(s):
    memo = {}
    
    def can_win(state, is_alice_turn):
        """
        Returns True if current player (Alice if is_alice_turn else Bob) can win
        from this state by playing optimally.
        """
        if not state:
            # No dishes left - previous player ate the last dish and won
            return False
        
        key = (is_alice_turn, state)
        if key in memo:
            return memo[key]
        
        if is_alice_turn:
            # Alice's turn - she wants to eat an 'A'
            has_move = False
            for i in range(len(state)):
                if state[i] == 'A':
                    has_move = True
                    # Alice pulls at position i, eats the A at position i
                    # Everything before i is knocked away (indices 0 to i-1)
                    # Remaining state is from i+1 onwards
                    remaining = state[i+1:]
                    
                    # If this leads to a state where Bob loses, Alice wins
                    if not can_win(remaining, False):
                        memo[key] = True
                        return True
            
            # If Alice has no valid move or all moves lead to Bob winning
            memo[key] = False
            return False
        
        else:
            # Bob's turn - he wants to eat a 'B'
            has_move = False
            for i in range(len(state)):
                if state[i] == 'B':
                    has_move = True
                    # Bob pulls at position i, eats the B at position i
                    # Everything after i is knocked away (indices i+1 onwards)
                    # Remaining state is from 0 to i-1
                    remaining = state[:i]
                    
                    # If this leads to a state where Alice loses, Bob wins
                    if not can_win(remaining, True):
                        memo[key] = True
                        return True
            
            # If Bob has no valid move or all moves lead to Alice winning
            memo[key] = False
            return False
    
    # Alice goes first
    if can_win(s, True):
        return "Alice"
    else:
        return "Bob"


# Read from input.txt
with open('input.txt', 'r') as infile:
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

# Write to output.txt
with open('output.txt', 'w') as outfile:
    for result in results:
        outfile.write(result + '\n')