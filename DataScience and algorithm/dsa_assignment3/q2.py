class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def push(self, dist, point):
        # Insert negative distance to simulate max-heap behavior
        self.heap.append((-dist, point))
        self._sift_up(len(self.heap) - 1)
    
    def pop(self):
        if len(self.heap) == 0:
            return None
        self._swap(0, len(self.heap) - 1)
        max_value = self.heap.pop()
        self._sift_down(0)
        return max_value
    
    def top(self):
        if len(self.heap) > 0:
            return self.heap[0]
        return None
    
    def size(self):
        return len(self.heap)
    
    def _sift_up(self, idx):
        parent = (idx - 1) // 2
        if idx > 0 and self.heap[idx][0] < self.heap[parent][0]:
            self._swap(idx, parent)
            self._sift_up(parent)
    
    def _sift_down(self, idx):
        left = 2 * idx + 1
        right = 2 * idx + 2
        smallest = idx
        
        if left < len(self.heap) and self.heap[left][0] < self.heap[smallest][0]:
            smallest = left
        if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right
        
        if smallest != idx:
            self._swap(idx, smallest)
            self._sift_down(smallest)
    
    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

def euclidean_distance(point):
    x, y, z = point
    return (x*x + y*y + z*z)**(1/2)

def k_closest_points(points, K):
    max_heap = MaxHeap()
    
    for point in points:
        dist = euclidean_distance(point)
        
        if max_heap.size() < K:
            max_heap.push(dist, point)
        else:
            # If the current point is closer than the farthest point in the heap
            if dist < -max_heap.top()[0]:
                max_heap.pop()
                max_heap.push(dist, point)
    
    # Extract all points from the heap
    result = []
    while max_heap.size() > 0:
        result.append(max_heap.pop()[1])
    
    # Sort the result based on Euclidean distance to ensure correct order
    result.sort(key=lambda p: euclidean_distance(p))
    
    return result

# Input processing
N = int(input("Enter the number of 3D points: "))
K = int(input("Enter the number of closest points to find: "))
points = eval(input("Enter the list of 3D points: "))

# Find and print the K closest points
closest_points = k_closest_points(points, K)
print(closest_points)