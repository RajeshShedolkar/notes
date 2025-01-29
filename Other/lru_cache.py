LRU (Least Recently Used) cache is a way to store and quickly access frequently used data while automatically removing old or less-used data to save space.  

### Imagine this:  
You have a small bag that can only hold **3 books**. You always keep the books you read most often in the bag.  

1. If you add a new book but the bag is full, you remove the **least recently read** book to make space.  
2. If you read a book that’s already in the bag, it stays there and moves to the **top of the stack** (most recently used).  
3. This way, the books you use the most stay in the bag, and the ones you don’t use often get removed.  

### In Python:  
The `functools.lru_cache` decorator helps store results of function calls so that if the same function is called again with the same input, it returns the stored result instead of recalculating.  

```python
from functools import lru_cache

@lru_cache(maxsize=3)  # Store up to 3 results
def slow_function(n):
    print(f"Computing for {n}...")
    return n * n  # Just an example

print(slow_function(2))  # Computes and stores result
print(slow_function(3))  # Computes and stores result
print(slow_function(4))  # Computes and stores result
print(slow_function(2))  # Fetches from cache (no computation)
print(slow_function(5))  # Computes new result, removes least recently used one
```

### Why use it?  
- **Speeds up programs** by avoiding repeated calculations.  
- **Saves processing power** by reusing previous results.  
- **Automatically manages memory** by removing old data when needed.  
