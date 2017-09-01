# Homework 6
# IT310, Broderick Hudson
# I promise that all code contained herein is my own

probNum = ['6.2','6.3','6.5','6.13','6.14','6.15','6.18','6.29']

# Make all imports
from random import randint
from collections import deque

#   
# This is taken from a lecture to be used for the homework problems
#    
class Empty(Exception):
    """Simple Exception extension"""
    pass

class ArrayStack:
    """LIFO Stack"""
    def __init__(self):
        self._data = []            # meant as a non-public instance

    def __len__(self):             # allows the natural use of len()
        return len(self._data)

    def is_empty(self):
        return self._data == []

    def push(self, e):
        self._data.append(e)       # push/"append" to top of the stack

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]
    
    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()

##############################################################################

class ArrayQueue:
    """Circular FIFO Queue"""
    def __init__(self, capacity):
        self._data = [None] * capacity
        self._size = 0 # This is the number of elements, not the size of the list
        self._front = 0 # index of the first element in queue
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty!')
        return self._data[self._front]
    
    def _resize(self, capacity):
        temp = self._data
        self._data = [None] * capacity
        step = self._front
        for k in range(self._size):
            self._data[k] = temp[step]
            step = (step+1) % len(temp)
        self._front = 0
    
    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty!')
        element_to_dequeue = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        # If size of queue is less than 1/4 capacity, reduce queue size to half
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data)//2)
        return element_to_dequeue
    
    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        idx_to_enqueue = (self._front + self._size) % len(self._data)
        self._data[idx_to_enqueue] = e
        self._size += 1
    
#
# This is the end of the code copied from lecture
#

    def rotate(self):
        if self.is_empty():
            raise Empty('You can\'t rotate nothing!')
        self._front = (self._front + 1) % len(self._data)

# Declare all variables
p2pushed = 25
p2popAttempts = 10
p2popErrors = 3
# start of p3startStack
p3startStack = ArrayStack()
p3startStack.push('Bread #2')
p3startStack.push('Mayo')
p3startStack.push('Lettuce')
p3startStack.push('Roast Beef')
p3startStack.push('Bread #1')
# end of p3startStack
p3endStack = ArrayStack()
p5list = ['Palindromes','don\'t','work','like','this']
p15test_quant = 100000
# start of p18stack
p18stack = ArrayStack()
p18stack.push('Inky')
p18stack.push('Pinky')
p18stack.push('Blinky')
p18stack.push('Clyde')
# end of p18stack

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
            p2(p2pushed,p2popAttempts,p2popErrors)
        elif inputVal == '2':
            print('\nProblem {0}'.format(probNum[1]))
            p3(p3startStack, p3endStack)
        elif inputVal == '3':
            print('\nProblem {0}'.format(probNum[2]))
            p5(p5list)
        elif inputVal == '4':
            print('\nProblem {0}'.format(probNum[3]))
            p13()
        elif inputVal == '5':
            print('\nProblem {0}'.format(probNum[4]))
            p14()
        elif inputVal == '6':
            print('\nProblem {0}'.format(probNum[5]))
            p15(p15test_quant)
        elif inputVal == '7':
            print('\nProblem {0}'.format(probNum[6]))
            p18(p18stack)
        elif inputVal == '8':
            print('\nProblem {0}'.format(probNum[7]))
            p29()
        else:
            print('{0} is not a valid input.'.format(inputVal))
        
def p2(pushed, popAttempts, popErrors):
    print('The stack has executed {0} pushes and {1} pops, {2} of which didn\'t remove anything.'.format(pushed,popAttempts,popErrors))
    print('This means that {0} were pushed, and {1} were popped.'.format(pushed,(popAttempts-popErrors)))
    print('There are --{0}-- elements on the stack.'.format(pushed - (popAttempts-popErrors)))

# The book calls for this to be called transer, but I wanted to follow my naming convention
def p3(start, end):
    print('NOTE: The book calls for this to be called transer(S,T), but I wanted to follow my naming convention.')
    print('I\'ll use sandwiches to make this clear.')
    print('The stack is ordered as follows: Bread #1, Roast Beef, Lettuce, Mayo, and Bread #2. Delicious.\n')
    
    # Move the objects to the other stack
    while not start.is_empty():
        end.push(start.pop())
    
    itr = 1    
    while not end.is_empty():
        print('{0}: {1}'.format(itr,end.pop()))
        itr += 1
        
    # Check the top of end
    print('\nThis shows that the sandwich is now Bread #2, Mayo, Lettuce, Roast Beef, then Bread #1. This is an abomination. It is also upside-down, as desired.')

def p5(input_list):
    # Initialize a stack
    stack = ArrayStack()
    print('The list at the beginning:')
    print(input_list)
    # Add things to the stack
    for itr in range(len(input_list)):
        stack.push(input_list[itr])
        input_list[itr] = None
    # Add things back to the list
    for itr in range(len(input_list)):
        input_list[itr] = stack.pop()
    print('\nThe list at the end:')
    print(input_list)
    
def p13():
    # Create the Deque
    Deque = deque()
    for i in range(1,9):
        Deque.append(i)

    # Create the Queue and move stuff into it
    Queue = ArrayQueue(8)
    Queue.enqueue(Deque.popleft()) # 1
    Queue.enqueue(Deque.popleft()) # 2
    Queue.enqueue(Deque.popleft()) # 3

    # Rotate one back back into the deque
    Deque.append(Deque.popleft())

    # Add some more to the queue
    Queue.enqueue(Deque.popleft())
    Queue.enqueue(Deque.pop())
    Queue.enqueue(Deque.popleft())
    Queue.enqueue(Deque.popleft())
    Queue.enqueue(Deque.popleft())

    # Move them back to the deque
    Deque.append(Queue.dequeue())
    Deque.append(Queue.dequeue())
    Deque.append(Queue.dequeue())
    Deque.append(Queue.dequeue())
    Deque.append(Queue.dequeue())
    Deque.append(Queue.dequeue())
    Deque.append(Queue.dequeue())
    Deque.append(Queue.dequeue())

    # Get it into a printable list
    printMe = [Deque.popleft() for i in range(8)]

    # Prove that it is in the desired order
    print('Desired order:  [1, 2, 3, 5, 4, 6, 7, 8]')
    print('Observed order:',printMe)

def p14():
    # Create the Deque
    Deque = deque()
    for i in range(1,9):
        Deque.append(i)

    # Create the stack and move everything to it
    Stack = ArrayStack()
    Stack.push(Deque.popleft()) # 1
    Stack.push(Deque.pop()) # 8
    Stack.push(Deque.popleft()) # 2
    Stack.push(Deque.pop()) # 7
    Stack.push(Deque.popleft()) # 3
    Stack.push(Deque.pop()) # 6
    Stack.push(Deque.pop()) # 5
    Stack.push(Deque.popleft()) # 4

    # Move everything back to the deque
    Deque.appendleft(Stack.pop()) # 4
    Deque.appendleft(Stack.pop()) # 5
    Deque.append(Stack.pop()) # 6
    Deque.appendleft(Stack.pop()) # 3
    Deque.append(Stack.pop()) # 7
    Deque.appendleft(Stack.pop()) # 2
    Deque.append(Stack.pop()) # 8
    Deque.appendleft(Stack.pop()) # 1

    # Get it into a printable list
    printMe = [Deque.popleft() for i in range(8)]

    # Prove that it is in the desired order
    print('Desired order:  [1, 2, 3, 5, 4, 6, 7, 8]')
    print('Observed order:',printMe)

def p15(number_of_tests):
    def _findLargest():
        # Make a stack and generate three random, distinct numbers
        Stack = ArrayStack()
        addMe1 = randint(0, 50)
        addMe2 = randint(0, 50)
        addMe3 = randint(0, 50)
        while (addMe1 == addMe2) or (addMe1 == addMe3) or (addMe2 == addMe3): # If any of them are equal, make new ones
            addMe1 = randint(0, 50)
            addMe2 = randint(0, 50)
            addMe3 = randint(0, 50)

        # For testing purposes, keep track of the actual largest value
        actualLargest = max(addMe1,addMe2,addMe3)

        # Add the 3 integers to the stack
        Stack.push(addMe1)
        Stack.push(addMe2)
        Stack.push(addMe3)

        # Now begins the actual algorithm
        # Pop the first one into the garbage
        Stack.pop()

        # Pop the next one and set it to x
        x = Stack.pop() # This is my one variable

        # Top the last one and return whichever is larger, x or the top value, as well as the actual largest value
        return [max(x,Stack.top()), actualLargest] # The first element of the return value is my one comparison

    print('My algorithm can be seen in the code. My justification is as follows:')
    print('There is a 1/3 chance that the discarded value was the largest one, assuming a truly random generation.')
    print('The largest of the remaining 2/3 of the integers will always be correctly identified.')
    print('If the largest is always found for 2/3 of the integers, then the largest is always found 2/3 of the time.')
    print()

    # Write a test that proves that this works
    accurate_results = 0
    for i in range(number_of_tests):
        test_instance = _findLargest()
        if test_instance[0] == test_instance[1]:
            accurate_results += 1
    print('In this round of {0} tests, the accuracy of this algorithm was: {1:.1%}'.format(number_of_tests, (accurate_results/number_of_tests)))

def p18(stack):
    print('The start of the stack at the beginning is: {0}'.format(stack.top()))
    middle = ArrayStack()
    final = ArrayStack()
    # This is the only real code from transfer/p3()
    while not stack.is_empty():
        middle.push(stack.pop())
    # This is the only real code from transfer/p3()
    while not middle.is_empty():
        final.push(middle.pop())
    # This is the only real code from transfer/p3()
    while not final.is_empty():
        stack.push(final.pop())
    itr = 1

    # Print the contents of the stack to demonstrate that it works.
    print('Contents of the stack:')
    while not stack.is_empty():
        print('{0}: {1}'.format(itr,stack.pop()))
        itr += 1
    print('This should be the opposite of how it started.')

def p29():
    print('This is a test of the rotate() method added to the ArrayQueue class.')
    # Initialize a queue
    Queue = ArrayQueue(3)
    Queue.enqueue('The Joker')
    Queue.enqueue('Mr. Freeze')
    Queue.enqueue('Calendar Man')

    print('The Joker is at the front of the queue, followed by Mr. Freeze, followed by Calendar Man.')

    # Begin rotating through and printing the results
    print('\nThis loop uses my rotate() method:')
    for i in range(1,10):
        print('Rotation #{0} --- Current front of the queue: {1}'.format(i,Queue.first()))
        Queue.rotate()
        
    print('\nThis loop uses the enqueue(dequeue) that accomplishes the same task less efficiently:')
    for i in range(1,10):
        print('Rotation #{0} --- Current front of the queue: {1}'.format(i,Queue.first()))
        Queue.enqueue(Queue.dequeue())
        
    print('\nYou can see that the front of the queue cycles between those three villains as they come up for parole and are released from Arkham.')

main()