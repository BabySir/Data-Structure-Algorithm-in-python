class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def push(self, value):
        # Insert negative to simulate max-heap
        self.heap.append(-value)
        self._sift_up(len(self.heap) - 1)
    
    def pop(self):
        if len(self.heap) == 0:
            return None
        self._swap(0, len(self.heap) - 1)
        max_value = -self.heap.pop()
        self._sift_down(0)
        return max_value
    
    def _sift_up(self, idx):
        parent = (idx - 1) // 2
        if idx > 0 and self.heap[idx] < self.heap[parent]:
            self._swap(idx, parent)
            self._sift_up(parent)
    
    def _sift_down(self, idx):
        left = 2 * idx + 1
        right = 2 * idx + 2
        smallest = idx
        
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        if smallest != idx:
            self._swap(idx, smallest)
            self._sift_down(smallest)
    
    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

def min_stops_to_reach_destination(destination, initial_dust, wells):
    # Max-heap for collecting the most dust when needed
    max_heap = MaxHeap()
    
    current_dust = initial_dust
    stops = 0
    previous_location = 0
    
    for location, dust in wells + [[destination, 0]]:

        print ("location, dust ", location, " ", dust)
        # Check how far we need to go
        distance_to_next = location - previous_location
        print("distance_to_next = location - previous_location", distance_to_next ,"::", location,  " ::",previous_location)
        
        # Try to reach the next well or destination
        while current_dust < distance_to_next:
            # If we can't make it and the heap is empty, return -1
            if len(max_heap.heap) == 0:
                return -1
            
            # Collect dust from the most profitable well
            current_dust += max_heap.pop()
            stops += 1
        
        # Deduct the distance to the next well from the current dust
        current_dust -= distance_to_next
        print('current_dust -= distance_to_next ::' ,current_dust )
        # Now we are at this well, add its dust to the heap
        max_heap.push(dust)
        
        # Update the previous location
        previous_location = location
    
    return stops

# Example input:
destination = 34
initial_dust = 5
wells = [[5, 10], [10, 6], [12, 100]]

# Get the result
result = min_stops_to_reach_destination(destination, initial_dust, wells)
print(result)  # Output should be 2




# destination = int(input("Enter the distance to the destination (in fairy miles): "))
# initial_dust = int(input("Enter the initial amount of fairy dust: "))

# # Input the number of wells
# n = int(input("Enter the number of wells: "))
# wells = []
# print("Enter the wells as space-separated values (location fairy_dust): ")
# for _ in range(n):
#     location, dust = map(int, input().split())
#     wells.append([location, dust])

# # Calculate and print the minimum number of stops
# result = min_stops_to_reach_destination(destination, initial_dust, wells)