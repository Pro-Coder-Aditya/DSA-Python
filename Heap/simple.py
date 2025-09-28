import heapq

# Create a min heap
heap = []

# Insert elements
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 20)
heapq.heappush(heap, 1)

print("Min Heap:", heap)

# Remove smallest element
print("Popped:", heapq.heappop(heap))
print("Heap after pop:", heap)