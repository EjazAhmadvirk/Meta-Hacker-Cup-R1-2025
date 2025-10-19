def can_visit_all(heights, h):
    """Check if all platforms can be visited with ladder height h"""
    n = len(heights)
    reachable = [False] * n
    
    # Mark platforms reachable directly from ground
    for i in range(n):
        if heights[i] <= h:
            reachable[i] = True
    
    # Propagate reachability between adjacent platforms
    changed = True
    while changed:
        changed = False
        for i in range(n):
            if reachable[i]:
                # Check left neighbor
                if i > 0 and not reachable[i-1]:
                    if abs(heights[i] - heights[i-1]) <= h:
                        reachable[i-1] = True
                        changed = True
                # Check right neighbor
                if i < n-1 and not reachable[i+1]:
                    if abs(heights[i] - heights[i+1]) <= h:
                        reachable[i+1] = True
                        changed = True
    
    return all(reachable)


def solve_case(heights):
    """Binary search for minimum ladder height"""
    if not heights:
        return 0
    
    left = 0
    right = max(heights)
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        if can_visit_all(heights, mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer


def main():
    # Read from input.txt
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
        
        answer = solve_case(heights)
        result = f"Case #{case_num}: {answer}"
        results.append(result)
        print(result)
    
    # Write to output.txt
    with open('output.txt', 'w') as f:
        for result in results:
            f.write(result + '\n')
    
    print(f"\n✓ Results written to output.txt")
    print(f"✓ Processed {T} test cases successfully!")


if __name__ == "__main__":
    main()