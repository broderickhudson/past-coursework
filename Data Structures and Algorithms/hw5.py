# Homework 5
# IT310, Broderick Hudson
# I promise that all code contained herein is my own

# Make all imports
import sys
import ctypes
from time import time

# Declare all variables
p2quant = 200
p7array = [1,2,3,4,5,6,7,8,5]
p12array = [[3,4,5],[8,7,6],[1,2,9]]
p26array = [1,1,2,2,3,3,4,4,4]

def main():
    print("Enter a number to display the corresponding problem's output/answer.")
    print('0:  Exit the program.')
    print('1:  5.2')
    print('2:  5.4')
    print('3:  5.6')
    print('4:  5.7')
    print('5:  5.12')
    print('6:  5.16')
    print('7:  5.24')
    print('8:  5.26')
    continu = True
    while continu:
        inputVal = str(input('Enter a number: '))
        if inputVal == '0':
            continu = False
            print('Exiting the program.')
        elif inputVal == '1':
            print('\nProblem 5.2')
            p2(p2quant)
        elif inputVal == '2':
            print('\nProblem 5.4')
            p4()
        elif inputVal == '3':
            print('\nProblem 5.6')
            p6()
        elif inputVal == '4':
            print('\nProblem 5.7')
            p7(p7array)
        elif inputVal == '5':
            print('\nProblem 5.12')
            p12(p12array)
        elif inputVal == '6':
            print('\nProblem 5.16')
            p16()
        elif inputVal == '7':
            print('\nProblem 5.24')
            p24()
        elif inputVal == '8':
            print('\nProblem 5.26')
            p26(p26array)
        else:
            print('{0} is not a valid input.'.format(inputVal))
            
def p2(quant):
    data = []
    prev = -100 # This is an impossible sentinel value
    for k in range(quant):
        a = len(data)
        b = sys.getsizeof(data)
        if b != prev:
            print("Length: {0:3d} - Size in bytes: {1:4d}".format(a,b))
        prev = b
        data.append(None)
        
# This class is copied from the book/lecture, as is the nature of the question
class DynamicArray(object):
    
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)
        
    def _make_array(self, c):
        return (c * ctypes.py_object)()
    
    def __len__(self):
        return self._n
    
    # This is the method changed for problem 5.4
    def __getitem__(self, index):
        if index < 0: # If the index is negative, make reset it to the positive version of that location
            index = (self._n + index)
        if not(0 <= index < self._n) or (index < 0):
            raise IndexError('Invalid index!')
        return self._A[index]
    
    # Grow the array dynamically
    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c
        
    def append(self, obj):
        if self._n == self._capacity: # List is full
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1
    
    # This is the method required by problem 5.6
    # It is based on code taken from the book, as is the nature of the question
    def insert(self, k, value):
        if self._n == self._capacity:
            B = self._make_array(2 * self._capacity)
            for val in range(k):
                B[val] = self._A[val]
            for val in range(k, self._n):
                B[val+1] = self._A[val]
            B[k] = value
            self._A = B
            self._capacity = 2 * self._capacity
            self._n += 1
        else:
            for j in range(self._n, k, -1):
                self._A[j] = self._A[j-1]
            self._A[k] = value
            self._n += 1
    
    # This is the method required by problem 5.16        
    def pop(self):
        self._A[self._n - 1] = None
        self._n -= 1
        if self._n <= self._capacity/4:
            self._resize(self._capacity//2)
            
    # This is the method to be tested for problem 5.24
    def remove(self, value):
        for k in range(self._n):
            if self._A[k] == value:
                for j in range(k, self._n - 1):
                    self._A[j] = self._A[j+1]
                self._A[self._n-1] = None
                self._n -= 1
                return
        raise ValueError('Value not found!')
        
def p4():
    testarray = DynamicArray() # Populate a DynamicArray
    n = 30
    for i in range(n):
        testarray.append(i)
    print('Element found using [25]:',testarray[25])
    print('Element found using [-5]:',testarray[-5])
    print('They are equivalent, which proves that my changes work!')
    try:
        print(testarray[-33])
    except IndexError:
        print('This error message was printed because I tried using [-33], which proves that the changes work!')
    
def p6():
    testarray = DynamicArray() # Populate a DynamicArray
    for i in range(10):
        testarray.append(i)
    inserts = 30
    for i in range(inserts):
        testarray.insert(3, i)
    for i in range(testarray._n):
        print("Index: {0:3d}  ~  Value: {1:3d}".format(i,testarray[i]))
    print('The array starts with values 1 through 10. This array shows that values 0 through 30 interrupt it starting at index 3, as intended. This proves that it works!')
    
def p7(array):
    appeared = set()
    duplicate = -1 # This is a sentinel value
    notfound = True
    iterator = 0
    while notfound:
        if array[iterator] not in appeared:
            appeared.add(array[iterator])
            iterator += 1
        else:
            duplicate = array[iterator]
            notfound = False
    if duplicate == -1:
        print('There were no duplicate values.')
    else:
        print('The duplicated value is: {0:<4}'.format(duplicate))
        
def p12(array):
    totalsarray = [sum(array[i]) for i in range(len(array))]
    total = sum(totalsarray)
    print('The sum of the given array is: {0:3d}'.format(total))
    
def p16():
    appendRan = 60
    popRan = 40
    testarray = DynamicArray() # Populate a DynamicArray
    for i in range(appendRan):
        testarray.append(i)
    for i in range(popRan):
        testarray.pop()
    for i in range(testarray._n):
        print("Index: {0:>3d}  ~  Value: {1:>3d}  ~  Capacity: {2:>3d}".format(i,testarray[i],testarray._capacity))
    print('The array starts with {0} elements, and then removes {1} of them from the end.'.format(appendRan, popRan))
    print('The remaining values are the first {0}, and {0} is not less than {1}/4, so it does not resize. This proves that this works.'.format(appendRan - popRan, testarray._capacity))
        
def p24():
    print('This one takes a few seconds.')
    sizes = [100,1000,10000]
    beginning_times = []
    middle_times = []
    end_times = []
    # Do the beginning times
    for size in sizes:
        data = DynamicArray()
        for i in range(size):
            data.append(i)
        start = time()
        for i in range(size//3):
            data.remove(i)
        beginning_times.append(time()-start)
    # Do the middle times
    for size in sizes:
        data = DynamicArray()
        for i in range(size):
            data.append(i)
        start = time()
        for i in range(size//3, len(data)-size//3):
            data.remove(i)
        middle_times.append(time()-start)
    # Do the end times
    for size in sizes:
        data = DynamicArray()
        for i in range(size):
            data.append(i)
        start = time()
        for i in range(len(data)-size//3, len(data)):
            data.remove(i)
        end_times.append(time()-start)
    
    # Start printing the times
    itr = 0    
    for size in sizes:
        print('\nSize:', size)
        print('Beginning Time: {0:5f}'.format(beginning_times[itr]))
        print('Middle Time:    {0:5f}'.format(middle_times[itr]))
        print('End Time:       {0:5f}'.format(end_times[itr]))
        itr += 1
    
def p26(array):
    unique = set()
    repeated = []
    for i in range(len(array)):
        if array[i] not in unique:
            unique.add(array[i])
        else:
            repeated.append([i, array[i]])
    # Print the repeated values
    for element in repeated:
        print('The value {0} that appears at index = {1} is a repeat.'.format(element[1],element[0]))
    
    
main()