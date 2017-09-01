# Broderick Hudson
# I promise that all code contained herein is my own, unless otherwise stated

# These classes are all from the book/lecture
###############################################################################
class _DoublyLinkedList:
    """Base class for a doubly linked list with header and trailer sentinels"""
    """Non-circular Linked List with head, tail"""

    # ------------- nested _Node class ---------------
    class _Node:
        """Lightweight private class for storing a linked node"""
        __slots__ = '_element', '_previous', '_next'  # memory efficiency, google it

        def __init__(self, element, previous, next):
            self._element = element
            self._previous = previous
            self._next = next

    # ------------------------------------------------
    # ------------- nested Error class ---------------
    class Empty(Exception):
        pass
    # ------------------------------------------------

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._previous = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        new_node = self._Node(e, predecessor, successor)
        predecessor._next = new_node
        successor._previous = new_node
        self._size += 1
        return new_node

    def _delete_node(self, anode):
        """Should not delete sentinel nodes."""
        prev_ = anode._previous
        next_ = anode._next
        prev_._next = next_
        next_._previous = prev_
        self._size -= 1
        temp = anode._element
        anode._previous = anode._next = anode._element = None
        return temp
###############################################################################
class PositionalList(_DoublyLinkedList):
    # ----------- nested Position class --------------
    class Position:

        def __init__(self, container, node):
            self._container = container             # reference to linked list that contains node at this position
            self._node = node                       # reference to node pointed to by this position

        def element(self):
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location"""
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """Return True if other does not represent the same location"""
            return not (self == other)

    # ----- private position Vaditation method -------
    # possible errors: p is not a Position, p is not in the current list, p is no longer valid
    # purpose of method: return the node pointed to by p if p is a valid position
    # self in this scope represents a doubly linked list... why?
    def _validate(self, p):
        """Return position's node, or raise exception"""
        if not isinstance(p, self.Position):
            raise TypeError("p must be of type Position")
        # If the list that contains p is not in the current list raise ValueError
        if p._container is not self:                # self is a doubly linked list and p is a Position
            raise ValueError("p does not belong to this container")
        if p._node._next is None:                   # underlying Node has been invalidated
            raise ValueError("p is no longer valid")
        return p._node

    # ----- private method to create a position ------
    # self represents a doubly linked list
    def _make_position(self, node):
        """Return Position instance for given node, None if sentinel"""
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)
    # ------------------------------------------------

    # ---------------- accessors ---------------------
    # methods to get information from the positional list

    def first(self):
        """Return position of first element"""
        return self._make_position(self._header._next)

    def last(self):
        """Return position of last element"""
        return self._make_position(self._trailer._previous)

    def before(self, p):
        """Return the position immediately before p"""
        node = self._validate(p)
        return self._make_position(node._previous)

    def after(self, p):
        """"Return the position immediately after p"""
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """Forward iterator of list elements."""
        #  Allows the use of next().
        #  Allows embed in for loops.
        pointer = self.first()
        while pointer is not None:
            yield pointer.element()         # return element stored at this position
            pointer = self.after(pointer)   # update the pointer

    # ---------------- mutators ----------------------
    # methods to change information in the positional list

    # Private method to return position rather than node
    # Overrides _insert_between() from parent _DoublyLinkedList class
    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """Insert new element in front and return position"""
        return self._insert_between(e, self._header, self._header._next)  # returns position thanks to overridden method

    def add_last(self, e):
        """Insert new element in back and return position"""
        return self._insert_between(e, self._trailer._previous, self._trailer)

    def add_before(self, p, e):
        """Insert new element e just before p, return position"""
        valid_position = self._validate(p)   # recall _validate returns the node to which p points
        return self._insert_between(e, valid_position._previous, valid_position)

    def add_after(self, p, e):
        """Insert new element e just after p, return position"""
        valid_position = self._validate(p)
        return self._insert_between(e, valid_position, valid_position._next)

    def delete(self, p):
        """Remove and return element at position p.  Invalidates position."""
        # Invalidation takes place due to the inherited method setting underlying node to None
        valid_position = self._validate(p)
        return self._delete_node(valid_position)

    def replace(self, p, e):
        """Replace and return element replaced"""
        valid_position = self._validate(p)
        element_to_return = valid_position._element
        valid_position._element = e
        return element_to_return

# Insertion Sort using Positional List
# Uses m marker for right most element of sorted list
# p marker for next element to sort
# w marker to traverse list from right to left

def insertion_sort(PL):
    """Sort Positional List of comparable elements in a non-decreasing order"""
    if len(PL) > 1:             # at least two elements
        m = PL.first()
        w = m
        while m != PL.last():
            p = PL.after(m)
            # CASE: element is correctly sorted
            if p.element() >= m.element():
                w = m = p
                continue

            # CASE: w reached the beginning of list
            if w == PL.first():
                # delete p and place p at beginning
                PL.add_first(PL.delete(p))
                continue

            w = PL.before(w)                # move w to the left
            if p.element() > w.element():
                # delete p and place p after w
                PL.add_after(w, PL.delete(p))
                # reset w
                w = m
###############################################################################
class Empty(Exception):
    pass

class PriorityQueueBase:
    # --- Nested class to store priority queue items
    # --- in a compositional way
    class _Item:
        __slots__ = "_key", "_value"

        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __lt__(self, other):
            return self._key < other._key

    def is_empty(self):
        return len(self) == 0

# Implementation of Priority Queue with Unsorted List
# Idea: Store key-value pair _Item instances in a PositionalList
# Since PositionalList will be implemented with a doubly-linked list
# all operations on doubly-linked list cost O(1)
# To remove a minimum element (or to find the minimum element), we must
# traverse the underlying list until we find the position of the item with the
# minimum key
# Thus, in the worst case scenario, we must check all elements witch means
# min() and remove_min() run O(n)

class UnsortedPriorityQueue(PriorityQueueBase):
    def _find_min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty')

        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        self._data.add_last(self._Item(key, value))

    def min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty')
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)


# Implementation of Priority Queue with Sorted List
# Idea: Use Positional List, make sure you add elements
# so that the relative positions before and after are
# smaller and larger respectively
# Thus, the the remove_min() and min() operations will be
# O(1), but adding elements will require O(n) in the
# worst case

class SortedPriorityQueue(PriorityQueueBase):
    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty')
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty')
        item = self._data.delete(self._data.first())
        return (item._key, item._value)

    def add(self, key, value):
        newest = self._Item(key, value)
        walk = self._data.last()   # walking backwards
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)
        else:
            self._data.add_after(walk, newest)
###############################################################################
class HeapPriorityQueue(PriorityQueueBase): # base class defines _Item
  """A min-oriented priority queue implemented with a binary heap."""

  #------------------------------ nonpublic behaviors ------------------------------
  def _parent(self, j):
    return (j-1) // 2

  def _left(self, j):
    return 2*j + 1
  
  def _right(self, j):
    return 2*j + 2

  def _has_left(self, j):
    return self._left(j) < len(self._data)     # index beyond end of list?
  
  def _has_right(self, j):
    return self._right(j) < len(self._data)    # index beyond end of list?
  
  def _swap(self, i, j):
    """Swap the elements at indices i and j of array."""
    self._data[i], self._data[j] = self._data[j], self._data[i]

  def _upheap(self, j):
    parent = self._parent(j)
    if j > 0 and self._data[j] < self._data[parent]:
      self._swap(j, parent)
      self._upheap(parent)             # recur at position of parent
  
  def _downheap(self, j):
    if self._has_left(j):
      left = self._left(j)
      small_child = left               # although right may be smaller
      if self._has_right(j):
        right = self._right(j)
        if self._data[right] < self._data[left]:
          small_child = right
      if self._data[small_child] < self._data[j]:
        self._swap(j, small_child)
        self._downheap(small_child)    # recur at position of small child

  #------------------------------ public behaviors ------------------------------
  def __init__(self):
    """Create a new empty Priority Queue."""
    self._data = []

  def __len__(self):
    """Return the number of items in the priority queue."""
    return len(self._data)

  def add(self, key, value):
    """Add a key-value pair to the priority queue."""
    self._data.append(self._Item(key, value))
    self._upheap(len(self._data) - 1)            # upheap newly added position
  
  def min(self):
    """Return but do not remove (k,v) tuple with minimum key.

    Raise Empty exception if empty.
    """
    if self.is_empty():
      raise Empty('Priority queue is empty.')
    item = self._data[0]
    return (item._key, item._value)

  def remove_min(self):
    """Remove and return (k,v) tuple with minimum key.

    Raise Empty exception if empty.
    """
    if self.is_empty():
      raise Empty('Priority queue is empty.')
    self._swap(0, len(self._data) - 1)           # put minimum item at the end
    item = self._data.pop()                      # and remove it from the list;
    self._downheap(0)                            # then fix new root
    return (item._key, item._value)
###############################################################################
############## THIS ENDS THE CLASSES THAT I COPIED FROM LECTURE ###############
###############################################################################
def problem3():
    prioQ = UnsortedPriorityQueue()
    prioQ.add(5,'A')
    print('Added: (5,A)')
    prioQ.add(4,'B')
    print('Added: (4,B)')
    prioQ.add(7,'F')
    print('Added: (7,F)')
    prioQ.add(1,'D')
    print('Added: (1,D)')
    print('Removed: {0}'.format(prioQ.remove_min()))
    prioQ.add(3,'J')
    print('Added: (3,J)')
    prioQ.add(6,'L')
    print('Added: (6,L)')
    print('Removed: {0}'.format(prioQ.remove_min()))
    print('Removed: {0}'.format(prioQ.remove_min()))
    prioQ.add(8,'G')
    print('Added: (8,G)')
    print('Removed: {0}'.format(prioQ.remove_min()))
    prioQ.add(2,'H')
    print('Added: (2,H)')
    print('Removed: {0}'.format(prioQ.remove_min()))
    print('Removed: {0}'.format(prioQ.remove_min()))
    
    print('\nElements remaining:')
    while not prioQ.is_empty():
        print(prioQ.remove_min())
        
def hardwick_heapq_sort_problem():
    # Using methods from pg. 384 of textbook, implement a heap-based sort
    # Use this sequence: (7,4,8,2,5,3,9)
    # Add them all to it, take them all out
    # How would I implement standby flyers, auctions, and stock markets with heapq?
    import heapq
    sortArray = [7,4,8,2,5,3,9]
    sortHeap = []
    for i in range(len(sortArray)):
        heapq.heappush(sortHeap,sortArray[i])
    sortArray = []
    for i in range(len(sortHeap)):
        heapq.heappush(sortArray,heapq.heappop(sortHeap))
    return sortArray
    
###############################################################################
class PQStack:
    def __init__(self):
        self._data = HeapPriorityQueue()
        self._key_start_value = 0 # Arbitrary value to use as key, decreases as elements are added
        
    def __len__(self):
        return len(self._data)
        
    def is_empty(self):
        return len(self._data) == 0
        
    def push(self, element):
        self._data.add(self._key_start_value, element)
        self._key_start_value -= 1 # This makes is so the next element added is the highest priority
        
    def pop(self):
        if self._data.is_empty():
            raise Empty('The stack is empty!')
        return self._data.remove_min()
        
    def top(self):
        if self._data.is_empty():
            raise Empty('The stack is empty!')
        return self._data.min()
###############################################################################
class PQFifoQueue:
    def __init__(self):
        self._data = HeapPriorityQueue()
        self._key_start_value = 0 # Arbitrary value to use as key, increases as elements are added
        
    def __len__(self):
        return len(self.__data)

    def is_empty(self):
        return len(self._data) == 0
    
    def first(self):
        if self._data.is_empty():
            raise Empty('The stack is empty!')
        return self._data.min()
    
    def enqueue(self, element):
        self._data.add(self._key_start_value, element)
        self._key_start_value += 1 # This makes it so the next element added is the lowest priority
        
    def dequeue(self):
        if self._data.is_empty():
            raise Empty('The stack is empty!')
        return self._data.remove_min()
###############################################################################
def merge_PQs(PQ1, PQ2): # Where PQ1 and PQ2 are both HeapPriorityQueue objects
    baseTree = 0
    addTree = 0
    if len(PQ1) >= len(PQ2): # Adding more elements into a smaller tree seems like it'd be more efficient due to upheap
        baseTree = PQ2
        addTree = PQ1
    else:
        baseTree = PQ1
        addTree = PQ2
    while not addTree.is_empty():
        addMe = addTree.remove_min()
        baseTree.add(addMe[0], addMe[1])
    return baseTree
###############################################################################
PQ1 = HeapPriorityQueue()
PQ1.add(1,5)
PQ1.add(2,10)
PQ1.add(3,15)
PQ1.add(4,20)

PQ2 = HeapPriorityQueue()
PQ2.add(10,50)
PQ2.add(20,100)
PQ2.add(30,150)
PQ2.add(40,200)

problem3()
print('\nProf. Hardwick challenged us to do this on Friday. I included it in here because it seemed like a fitting spot for it.')
print(hardwick_heapq_sort_problem())
print('\nThis is a test of the merge_PQs method. These should be in descending order, starting with (1,5) and ending with (40,200).')
printMe = merge_PQs(PQ1,PQ2)
while not printMe.is_empty():
    print(printMe.remove_min())