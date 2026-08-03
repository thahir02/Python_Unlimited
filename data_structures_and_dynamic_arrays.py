'''
Data Structures :-
  Python provides four core built-in data structures—Lists, Tuples, Sets, and Dictionaries.

1. Built-in Data Structures
  Python’s built-in data structures are optimized for general use cases and form the foundation of most Python scripts.

| Data Structure | Purpose                                                | Syntax                | Properties                            | Example             |
| -------------- | ------------------------------------------------------ | --------------------- | ------------------------------------- | ------------------- |
| `List`         | Storing dynamic, sequential records.                   | `[item1, item2, ...]` | Ordered, Mutable, Allows Duplicates   | `[1, "apple", 3.5]` |
| `Tuple`        | Storing read-only data or ensuring data integrity.     | `(item1, item2, ...)` | Ordered, Immutable, Allows Duplicates | `(10, 20, 30)`      |
| `Set`          | Removing duplicates and performing membership testing. | `{item1, item2, ...}` | Unordered, Mutable, No Duplicates     | `{"cat", "dog"}`    |
| `Dictionary`   | Fast lookup using key-value pairs.                     | `{key: value, ...}`   | Ordered*, Mutable, Unique Keys        | `{"id": 101}`       |

*Note: Python dictionaries maintain insertion order starting from Python 3.7+.

2. Specialized Standard Library Collections
  When built-in objects fall short on performance requirements, the Python Standard Library provides optimized alternatives.
    collections.deque: A double-ended queue designed for fast O(1) appends and pops from both ends. Ideal for building custom Stacks and Queues.
    collections.Counter: A dictionary subclass tailored for tracking frequencies and counting occurrences of hashable items.
    heapq: A list-based implementation of the binary heap algorithm. It is heavily utilized to construct min-priority queues.
    array.array: A space-efficient, typed alternative to standard lists. It restricts contents to homogeneous basic types (such as integers or floats).

3. User-Defined & Advanced Data Structures
  Complex, non-linear algorithms rely on custom structures built using Python classes and references.
    Linked Lists: Sequence of nodes where each node points to the next element via memory references, allowing quick insertion and deletions.
    Stacks & Queues: Linear rulesets (Last-In-First-Out for Stacks; First-In-First-Out for Queues) managed cleanly via collections.deque.
    Trees (e.g., Binary Trees, BSTs): Hierarchical data patterns utilizing nodes and edges. Often used to construct file directories or HTML DOM parsers.
    Graphs: Networks consisting of vertices joined by edges. Typically modeled in Python via an adjacency list represented by a dictionary mapping.

_______________________________________ THE DIFFERENCE ARRAY AND REFERNTIAL ARRAY ______________________________________

Compact Array (Primitive Array): 
  Stores the actual, raw data values directly next to each other in a continuous block of memory. Every element must be of the exact same data type and size.
  Examples include Python's array module, NumPy arrays, and standard arrays in C/C++.
Referential Array: 
  Stores a continuous block of memory pointers (addresses) rather than the actual values. Each pointer references an independent object stored elsewhere in memory.
  This allows elements to be completely different data types and varying sizes.A standard Python List is the most prominent example of a referential array.

[Compact Array: Contiguous Values]
Memory: | 45 | 12 | 89 | 23 |

[Referential Array: Contiguous Memory Pointers]
Memory: | 0x001 | 0x008 | 0x004 | 0x002 |
            │       │       │       │
            ▼       ▼       ▼       ▼

          |45|   |"hi"|  |3.14|  |[1,2]|  <-- Objects scattered in memory


| Feature               | Compact Array                                               | Referential Array                                |
| --------------------- | ----------------------------------------------------------- | ------------------------------------------------ |
| **What is Stored?**   | Raw binary values (`45`, `12`, `89`)                        | Memory addresses/pointers (`0x7fff...`)          |
| **Data Types**        | Strictly homogeneous (all elements must have the same type) | Heterogeneous (mixed data types allowed)         |
| **Memory Efficiency** | High (no pointer overhead or object wrappers)               | Low (stores pointers along with object metadata) |
| **Cache Performance** | Excellent (CPU reads neighboring values efficiently)        | Poor (pointer chasing leads to cache misses)     |
| **Python Examples**   | `array.array('i', [1, 2, 3])`, `numpy.array()`              | Standard Python list: `[45, "hello", 3.14]`      |

_________________________________________ DYNAMIC ARRAY ____________________________________

A dynamic array is a random-access, sequential data structure that automatically grows or shrinks in size as elements are added or removed. 
1. How a Dynamic Array Works (Under the Hood)
  Because computer memory requires data structures to claim space in consecutive blocks, an array cannot simply expand into neighboring memory spaces that might already be occupied by other variables.
  To overcome this, a dynamic array automates a resize and copy strategy:
    Initial Allocation: The array initializes with a small, hidden starting capacity (e.g., room for 4 elements).
    Pushing Elements: Elements are added normally until the array reaches 100% capacity. This point is called saturation.
    The Resize Trigger: When you attempt to append to a saturated array, the structure requests a brand-new, larger block of contiguous memory from the operating system.
    Growth Factor: Python typically uses a geometric growth factor (roughly 1.125× to 1.5× the old size, plus a small constant padding) to ensure it does not request memory too frequently.
    The Data Copy: The array copies all existing elements from the old memory block into the new memory block, deletes the old block, and inserts the new item.
'''
