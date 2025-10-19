def solve():
    # Read from input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    
    line_idx = 0
    T = int(lines[line_idx].strip())
    line_idx += 1
    
    results = []
    
    for case_num in range(1, T + 1):
        N = int(lines[line_idx].strip())
        line_idx += 1
        
        heights = list(map(int, lines[line_idx].strip().split()))
        line_idx += 1
        
        # Find maximum difference between consecutive platforms
        max_ladder = 0
        for i in range(N - 1):
            diff = abs(heights[i] - heights[i + 1])
            max_ladder = max(max_ladder, diff)
        
        result = f"Case #{case_num}: {max_ladder}"
        results.append(result)
        print(result)  # Print each result immediately
    
    # Write all results to output.txt
    with open('output.txt', 'w') as f:
        for result in results:
            f.write(result + '\n')
    
    print("\n✓ Results written to output.txt")
    print(f"✓ Processed {T} test cases successfully!")

if __name__ == "__main__":
    solve()

if __name__ == "__main__":
    solve()