# This is straight from the book
def inplace_quick_sort_book(S, a, b):
    if a >= b: return
    pivot = S[b]
    left = a
    right = b-1
    while left <= right:
        while left <= right and S[left] < pivot:
            left += 1
        while left <= right and pivot < S[right]:
            right -= 1
        if left <= right:
            S[left], S[right] = S[right], S[left]
            left, right = left + 1, right - 1
    S[left], S[b] = S[b], S[left]
    inplace_quick_sort_book(S, a, left-1)
    inplace_quick_sort_book(S, left + 1, b)

# This is for problem 12
def inplace_quick_sort_p12(S, a, b):
    if a >= b: return
    pivot = S[b]
    left = a
    right = b-1
    while left < right:
        while left <= right and S[left] < pivot:
            left += 1
        while left <= right and pivot < S[right]:
            right -= 1
        if left <= right:
            S[left], S[right] = S[right], S[left]
            left, right = left + 1, right - 1
    S[left], S[b] = S[b], S[left]
    inplace_quick_sort_p12(S, a, left-1)
    inplace_quick_sort_p12(S, left + 1, b)
    
def inplace_quick_sort_p13(S, a, b):
    if a >= b: return
    pivot = S[b]
    left = a
    right = b-1
    while left <= right:
        while left <= right and S[left] < pivot:
            left += 1
        while left <= right and pivot < S[right]:
            right -= 1
        if left < right:
            S[left], S[right] = S[right], S[left]
            left, right = left + 1, right - 1
    S[left], S[b] = S[b], S[left]
    inplace_quick_sort_p13(S, a, left-1)
    inplace_quick_sort_p13(S, left + 1, b)
    
def is_sorted(L):
    itr = 0
    while itr < len(L)-1:
        if L[itr] > L[itr+1]:
            return False
        itr += 1
    return True

######################################
### THESE CLASSES ARE FROM LECTURE ###
######################################
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
#------------------------------------------------------------------------------
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
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """Return the position immediately before p"""
        node = self._validate(p)
        return self._make_position(node._prev)

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
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """Insert new element e just before p, return position"""
        valid_position = self._validate(p)   # recall _validate returns the node to which p points
        return self._insert_between(e, valid_position._prev, valid_position)

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
    
    def add_first_node(self, node):
        prev_header = self._header._next
        self._header._next = node
        prev_header._previous = node
        node._previous = self._header
        node._next = prev_header
        
    def add_last_node(self, node):
        prev_trailer = self._trailer._previous
        self._trailer._previous = node
        prev_trailer._next = node
        node._next = self._trailer
        node._previous = prev_trailer
        
    def add_node_before(self, previous_node, new_node):
        new_prev = previous_node._previous
        new_prev._next = new_node
        new_node._previous = new_prev
        previous_node._previous = new_node
        new_node._next = previous_node
    
    def merge(self,pl2):
        for element in pl2:
            checkMe = self.first()
            while checkMe is not None:
                if element.element() <= checkMe.element(): # If element is less than checkMe, add it before checkMe
                    if checkMe.element() == self.first().element(): # If checkMe is the header, make element the new header
                        self.add_first_node(element._node)
                        pl2._size -= 1
                    else: # If checkMe isn't the header, add element before it
                        self.add_node_before(checkMe._node, element._node)
                        pl2._size -= 1
                elif checkMe.element() == self.last().element(): # Otherwise, if element is greater than the last element, add it as the new trailer
                    self.add_last_node(element._node)
                    pl2._size -= 1
                else: # If neither of those are true, it has a spot in the list somewhere, so get the next checkMe
                    checkMe = checkMe.next()
            
#------------------------------------------------------------------------------    
myList1 = [7,6,5,4,3,2,1]
myList2 = [7,6,5,4,3,2,1]

inplace_quick_sort_book(myList1, 0, len(myList1)-1)
inplace_quick_sort_p12(myList2, 0, len(myList2)-1)

print('Method as listed:',myList1)
print()
print('Altered method  :',myList2)
print()
print()

myList3 = [1,1,2,3,4,5]
#myList4 = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
myList4 = [1,1,2,3,4,5]

inplace_quick_sort_book(myList3, 0, len(myList3)-1)
print('Method as listed:',myList3)
print()
inplace_quick_sort_p13(myList4, 0, len(myList4)-1)
print('Altered method  :',myList4)

sortedList = [1,2,3,4,5,6,7,8,9]
unsortedList = [1,9,2,8,3,7,4,6,5]
print(is_sorted(sortedList))
print(is_sorted(unsortedList))
