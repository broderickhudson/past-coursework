# Homework 6
# IT310, Broderick Hudson
# I promise that all code contained herein is my own

# Make all imports

# Problem Numbers
probNum = ['7.2','7.3','7.8','7.13','7.15','7.26','7.29','7.34']

# Paste all classes from class used in this assignment
##############################################################################
class SLinkedList:
    """Non-circular Linked List with head, tail"""
    # ------------- nested _Node class ---------------
    class _Node:
        """Lightweight private class for storing a linked node"""
        __slots__ = '_element', '_link'   # memory efficiency, google it

        def __init__(self, element, link):
            self._element = element
            self._link = link

        def __repr__(self):
            return '[{0},{1}]'.format(self._element, self._link)
    # ------------------------------------------------
    # ------------- nested Error class ---------------
    class Empty(Exception):
        pass
    # ------------------------------------------------

    def __init__(self):
        self._head = None           # A node
        self._tail = self._head
        self._size = 0

    def __len__(self):
        return self._size

    def head(self):
        if self._size == 0:
            return None
        return self._head._element
    
    def headTru(self): # I added this!
        if self._size == 0:
            return None
        return self._head

    def tail(self): 
        if self._head is not None:
            return self._tail._element
        return None
    
    def tailTru(self): # I added this!
        if self._head is not None:
            return self._tail
        return None

    def is_empty(self):
        return len(self) == 0

    def insert_head(self, e):
        new_head = self._Node(e, self._head)
        self._head = new_head
        if self._size == 0:
            self._tail = new_head
        self._size += 1

    def insert_tail(self, e):
        new_tail = self._Node(e, None)
        if self._size == 0:
            self._head = new_tail
        else:
            self._tail._link = new_tail
        self._tail = new_tail
        self._size += 1

    def remove_head(self):   # :(
        if self.is_empty():
            raise self.Empty("Linked List is empty")
        temp = self._head
        self._head = self._head._link
        self._size -= 1
        element = temp._element
        temp._element = temp._link = None    # help garbage collection
        return element
    
    def reverse(self): # I made this!
        previousNode = None
        currentNode = self._head
        self._tail = self._head
        while currentNode is not None:
            nextNode = currentNode._link
            currentNode._link = previousNode
            previousNode = currentNode
            currentNode = nextNode
        self._head = previousNode
        return self
##############################################################################
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
##############################################################################
class PositionalList(_DoublyLinkedList):
    # --------- nested Position class -------
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same 
            node as the instance"""
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):   # !=
            """Return True if other does not represent the same location"""
            return not (self == other)

    # --- private method to create a position ------
    # self represents a doubly linked list
    def _make_position(self, node):
        """Return Position instance for given node, None if sentinel"""
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    # --- private method to validate a position ----
    # possible errors: p is not a Position, p is not in the current list,
    # p is no longer valid
    # purpose of method: return the node pointed to by p if p is a valid position
    # self in this scope is a doubly linked list

    def _validate(self, p):
        """Return position's node, ro raise exception"""
        if not isinstance(p, self.Position):
            raise TypeError("p must by of type Position")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._next is None:
            raise ValueError("p is no longer valid")
        return p._node
    # --------------------------------------------

    # ------ accessor methods --------------------
    def first(self):
        """Returns position of the first element"""
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._previous)

    def before(self, p):
        """Returns position before p"""
        node = self._validate(p)
        return self._make_position(node._previous)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """Forward iterator of list elements"""
        # Allows the use of next()
        # Allows embedding in for loops
        pointer = self.first()
        while pointer is not None:
            yield pointer.element()    # return element stored at this position
            pointer = self.after(pointer)
            
    def __reverse__(self): # I made this
        pointer = self.last()
        while pointer is not None:
            yield pointer.element()
            pointer = self.before(pointer)

    # ------ mutator methods -----------------
    # Override _insert_between() from parent to return a position instead of a node
    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer._previous, self._trailer)

    def add_before(self, p, e):
        valid_position = self._validate(p)
        return self._insert_between(e, valid_position._previous, valid_position)

    def add_after(self, p, e):
        valid_position = self._validate(p)
        return self._insert_between(e, valid_position, valid_position._next)

    def delete(self, p):
        """Remove and return element at position p.  Invalidate position."""
        valid_position = self._validate(p)
        return self._delete_node(valid_position)

    def replace(self, p, e):
        valid_position = self._validate(p)
        element_to_return = valid_position._element
        valid_position._element = e
        return element_to_return
    
    def find(self, e): # I made this!
        for element in self:
            if element._node._element == e:
                return element
        return None
    
    def swap(self, pos1, pos2): # I made this!
        
        # Validate the positions and set the node as a variable for readability
        pos1v = self._validate(pos1)
        pos2v = self._validate(pos2)
        pos1node = pos1v._node
        pos2node = pos2v._node
        
        # Update the node before the first position to be switch
        pos1prev = pos1node._previous
        pos1prev._next = pos2node
        
        # Update the node after the first position to be switch
        pos1next = pos1node._next
        pos1next._previous = pos2node
        
        # Update the node before the second position to be switch
        pos2prev = pos2node._previous
        pos2prev._next = pos1node

        # Update the node after the second position to be switch        
        pos2next = pos2node._next
        pos2next._previous = pos1node
##############################################################################
class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage"""

    # ----------- nested _Node class --------------
    class _Node:
        """Lightweight private class for storing a linked node"""
        __slots__ = '_element', '_next'  # memory efficiency

        def __init__(self, element, next):
            self._element = element
            self._next = next

        def __repr__(self):
            return '[{0},{1}]'.format(self._element, self._next)

    # ---------------------------------------------

    # ----------- nested Error class --------------
    class Empty(Exception):
        pass
    # ---------------------------------------------

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise self.Empty("Queue is empty")
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            raise self.Empty("Queue is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self,e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1
        
    def concatonate(self, Q2):
        self._tail._next = Q2._head
        self._tail = Q2._tail
        Q2._size = 0
##############################################################################

# Declare all variables
p3length = 15

def main():
    print("Enter a number to display the corresponding problem's output/answer.")
    print('0:  Exit the program.')
    print('1:  {0}'.format(probNum[0]))
    print('2:  {0}'.format(probNum[1]))
    print('3:  {0}'.format(probNum[2]))
    print('4:  {0}'.format(probNum[3]))
    print('5:  {0}'.format(probNum[4]))
    print('6:  {0}'.format(probNum[5]))
    print('7:  {0}'.format(probNum[6]))
    print('8:  {0}'.format(probNum[7]))
    continu = True
    while continu:
        inputVal = str(input('Enter a number: '))
        if inputVal == '0':
            continu = False
            print('Exiting the program.')
        elif inputVal == '1':
            print('\nProblem {0}'.format(probNum[0]))
            p2()
        elif inputVal == '2':
            print('\nProblem {0}'.format(probNum[1]))
            p3(p3length)
        elif inputVal == '3':
            print('\nProblem {0}'.format(probNum[2]))
            p8()
        elif inputVal == '4':
            print('\nProblem {0}'.format(probNum[3]))
            p13()
        elif inputVal == '5':
            print('\nProblem {0}'.format(probNum[4]))
            p15()
        elif inputVal == '6':
            print('\nProblem {0}'.format(probNum[5]))
            p26()
        elif inputVal == '7':
            print('\nProblem {0}'.format(probNum[6]))
            p29()
        elif inputVal == '8':
            print('\nProblem {0}'.format(probNum[7]))
            p34()
        else:
            print('{0} is not a valid input.'.format(inputVal))
            
def p2():
    ##### SUB-METHOD #####
    def _concatSLL(NL1,NL2): # NL1 stands for Node from List 1, to help remember
        returnMe = SLinkedList()
        currNode1 = NL1
        currNode2 = NL2
        while currNode1 is not None:
            nextNode = currNode1._link
            returnMe.insert_tail(currNode1._element)
            currNode1 = nextNode
        while currNode2 is not None:
            nextNode = currNode2._link
            returnMe.insert_tail(currNode2._element)
            currNode2 = nextNode
        return returnMe
    ##### END SUB_METHOD #####
    L1 = SLinkedList()
    L1.insert_tail("Somebody")
    L1.insert_tail("once")
    L1.insert_tail("told")
    L1.insert_tail("me")
    
    L2 = SLinkedList()
    L2.insert_tail('the')
    L2.insert_tail('world')
    L2.insert_tail('was')
    L2.insert_tail('gonna')
    L2.insert_tail('roll')
    L2.insert_tail('me.')
    
    concatList = _concatSLL(L1.headTru(), L2.headTru())
    
    print('If what prints below is by Smashmouth, then we are in business.\n')
    while not concatList.is_empty():
        print(concatList.remove_head())
        
def p3(length):
    ##### SUB-METHOD #####        
    def _SLLCount(SLL, count=0):
        if not SLL.is_empty():
            SLL.remove_head()
            return _SLLCount(SLL, count+1)
        else:
            return count
    ##### END SUB-METHOD #####
    countMe = SLinkedList()
    for i in range(length):
        countMe.insert_head(i)
    algoCount = _SLLCount(countMe)
    print('The algorithm counted: {0}'.format(algoCount))
    print('The actual length was: {0}'.format(length))
    print('Does it work: {0}'.format(algoCount == length))

def p8():
    def _findMid(DLL):
        ##### SUB-METHOD #####
        left = DLL._header._next
        right = DLL._trailer._previous
        prevLeft = left
        while left != DLL._trailer or right != DLL._header:
            if right == prevLeft:
                return right._element
            elif right == left:
                return right._element
            else:
                prevLeft = left
                left = left._next
                right = right._previous
        ##### END SUB-METHOD #####
    evDLL = _DoublyLinkedList()
    evDLL._insert_between('Last',evDLL._header,evDLL._trailer)
    evDLL._insert_between('Second Last',evDLL._header,evDLL._header._next)
    evDLL._insert_between('Middle',evDLL._header,evDLL._header._next)
    evDLL._insert_between('Second',evDLL._header,evDLL._header._next)
    evDLL._insert_between('First',evDLL._header,evDLL._header._next)
    
    odDLL = _DoublyLinkedList()
    odDLL._insert_between('Last',odDLL._header,odDLL._trailer)
    odDLL._insert_between('Middle right',odDLL._header,odDLL._header._next)
    odDLL._insert_between('Middle left',odDLL._header,odDLL._header._next)
    odDLL._insert_between('First',odDLL._header,odDLL._header._next)
    
    evMid = _findMid(evDLL)
    odMid = _findMid(odDLL)
    
    print('Middle of even-length list: {0}'.format(evMid))
    print('Middle of odd-length list:  {0}'.format(odMid))

def p13():
    print('The method is in the code, as the second to last method in the PositionList class.')
    
def p15():
    print('The method is in the code, right after __iter__, in the PositionalList class.')
    
def p26():
    print('The method is in the code, as the last method of LinkedQueue.')
    
def p29():
    testMe = SLinkedList()
    testMe.insert_head('Last')
    testMe.insert_head('Second Last')
    testMe.insert_head('Middle')
    testMe.insert_head('Second')
    testMe.insert_head('First')
    
    testMe = testMe.reverse()
    
    for i in range(len(testMe)):
        print(testMe.remove_head())
        
    print('\nIf the above is in the opposite order as expected, this worked.')
    
def p34():
    print('The method is in the code, as the last method of the PositionList class.')
            
main()