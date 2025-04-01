class ObjectPool:
    def __init__(self, create_func, size):
        self.pool = [create_func() for _ in range(size)]

    def acquire(self):
        return self.pool.pop() if self.pool else None

    def release(self, obj):
        self.pool.append(obj)

# Example object
class MyObject:
    pass

# Create a pool with 2 objects
pool = ObjectPool(MyObject, 2)

obj1 = pool.acquire()
obj2 = pool.acquire()
print(obj1, obj2)

pool.release(obj1)
obj3 = pool.acquire()
print(obj3 is obj1)