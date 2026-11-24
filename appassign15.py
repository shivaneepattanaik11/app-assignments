
import gc
import sys

# Create a class
class Demo:
    def __init__(self, name):
        self.name = name

# Check garbage collection status
print("Garbage Collection Enabled:", gc.isenabled())

# Create objects
obj1 = Demo("Object 1")
obj2 = Demo("Object 2")

print("\nObjects Created")
print("Object 1:", obj1.name)
print("Object 2:", obj2.name)

# Check memory usage
print("\nMemory Usage:")
print("Object 1:", sys.getsizeof(obj1), "bytes")
print("Object 2:", sys.getsizeof(obj2), "bytes")

# Delete objects
del obj1
del obj2

print("\nObjects Deleted")

# Perform manual garbage collection
collected = gc.collect()

print("Garbage Collection Completed")
print("Objects Collected:", collected)

# Display garbage collection statistics
print("\nGarbage Collection Statistics:")
print(gc.get_stats())

print("\nProgram Completed!")
