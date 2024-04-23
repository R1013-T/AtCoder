def solve(N, A):
    # pos will store the correct position for each value 1 to N
    pos = [0] * (N + 1)
    for index, value in enumerate(A):
        pos[value] = index
    
    visited = [False] * N
    operations = []
    
    # Find cycles
    for i in range(N):
        if not visited[i]:
            # Start a new cycle
            cycle = []
            x = i
            while not visited[x]:
                visited[x] = True
                cycle.append(x)
                x = pos[x + 1]  # Move to the position where the next number should be
            # Now we have a cycle in `cycle`
            if len(cycle) > 1:
                # To solve a cycle, perform the swaps to order it
                for j in range(len(cycle) - 1):
                    operations.append((cycle[j] + 1, cycle[-1] + 1))  # +1 for 1-based index
    
    return operations

# Read input
N = int(input())
A = list(map(int, input().split()))

# Get the operations
operations = solve(N, A)

# Print the number of operations
print(len(operations))
# Print each operation
for op in operations:
    print(op[0], op[1])
