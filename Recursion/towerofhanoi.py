def toh(n,source, destination, helper):
    count = 0
    if n == 1:
        print("move disk", n, "from rod", source, "to rod", destination)
        return 1
    count += toh(n-1, source, helper, destination)
    print("move disk", n, "from rod", source, "to rod", destination)
    count += 1  # Increment count for the current move
    count += toh(n-1, helper, destination, source)
    return count
source = 'A'
destination = 'C'
helper = 'B'
k=toh(3,source,destination,helper)
print(k)