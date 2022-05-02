class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.storage = dict()
        self.hit_record = dict()

    def get(self, key):
        """
        Retrieve item from provided key.

        Return -1 if nonexistent.
        """
        if key in self.storage:
            self.hit_record[key] += 1
            return self.storage[key]

        return -1

    def set(self, key, value):
        """
        Set the value if the key is not present in the cache.
        If the cache is at capacity remove the oldest item. 
        """
        if self.capacity <= 0:
            return -1

        if len(self.storage) < self.capacity:
            self.storage[key] = value
            self.hit_record[key] = 0 #Initialize the hit record of a value
        else:
            least_used = min(self.hit_record, key=self.hit_record.get)
            del self.storage[least_used]
            del self.hit_record[least_used]
            self.storage[key] = value
            self.hit_record[key] = 0

# Test Case 1
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))     # returns 1
print(our_cache.get(2))     # returns 2
print(our_cache.get(9))     # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))     # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print(our_cache.get(6))     # returns 6 cause six was added   

# Test Case 2
our_cache = LRU_Cache(0)
our_cache.set(2,2)
our_cache.set(3,3)    

print(our_cache.get(2))     # retuen -1 because the memory is empty
print(our_cache.get(3))     # retuen -1 because the memory is empty

# Test Case 3
our_cache = LRU_Cache(1)

our_cache.set(2,2)            
our_cache.set(3,3)

print(our_cache.get(2))     # retuen -1 because the cache hit zero by default
print(our_cache.get(3))     # retuen 3


# Test Case 4
our_cache = LRU_Cache(1000)
for x in range(1000):
    our_cache.set(x, x)

print(our_cache.get(1000)) #return -1
our_cache.set(1000, 1000)
print(our_cache.get(1000))  #returns 1000
print(our_cache.get(0))     # returns -1 because the earliest cache entry was removed
