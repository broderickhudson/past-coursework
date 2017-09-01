# Code by Broderick Hudson
# This code is all mine. I promise.
# Assignment 2
# Problems included: R-2.4, R-2.13, R-2.14, R-2.16, R-2.19, C-2.28, C-2.31, C-2.32, P-2.33 [Use tuples], P-2.39 [Ignore last sentence, include inheritence diagram]

# Import statements
from abc import ABCMeta, abstractmethod

# ALL VARIABLES DEFINED HERE #
R4name = 'Tarantula'
R4petals = 8
R4price = 3.5
C31start = 0
C31previous1 = 200
C31previous2 = 2
C32start = 65536
P33string = '3x^3 + 2x^2 - 9x + 10'

# This is the main function
def main():
    done = False
    print('Problems:')
    print('1.  R-2.4')
    print('2.  R-2.13')
    print('3.  R-2.14')
    print('4.  R-2.16')
    print('5.  R-2.19')
    print('6.  C-2.28')
    print('7.  C-2.31')
    print('8.  C-2.32')
    print('9.  P-2.33')
    print('10. P-2.39')
    print('\nEnter the number of a problem to execute it, or 0 to end the program.')
    # Use user-input inside of a loop to create a selection menu
    while not done:
        try:
            selection = int(input('Enter a number: '))
            # Exit the function
            if selection == 0:
                done = True
                print('Exiting the function.')
            elif selection == 1:
                print()
                print('Problem R-2.4:')
                R4(R4name, R4petals, R4price)
            elif selection == 2:
                print()
                print('Problem R-2.13:')
                R13()
            elif selection == 3:
                print()
                print('Problem R-2.14:')
                R14()
            elif selection == 4:
                print()
                print('Problem R-2.16:')
                R16()
            elif selection == 5:
                print()
                print('Problem R-2.19:')
                R19()
            elif selection == 6:
                print()
                print('Problem C-2.28:')
                C28()
            elif selection == 7:
                print()
                print('Problem C-2.31:')
                C31(C31start, C31previous1, C31previous2)
            elif selection == 8:
                print()
                print('Problem C-2.32:')
                C32(C32start)
            elif selection == 9:
                print()
                print('Problem P-2.33:')
                P33(P33string)
            elif selection == 10:
                print()
                print('Problem P-2.39:')
                ###
            else:
                print('{0} is not a valid option.'.format(selection))
        except ValueError:
            print('You must enter an integer.')
            
# THIS CLASS IS FOR 2.4 #
class Flower(object):
    def __init__(self, name, petals, price):
        # Set the values inside of try/except statements so that it can give specific error messages
        try:
            self._name = str(name)
        except ValueError:
            print('{0} is not a valid name.'.format(name))
            
        try:
            self._petals = int(petals)
        except ValueError:
            print('{0} is not a valid number of petals.'.format(petals))
            
        try:
            self._price = float('{0:.2f}'.format(round(price, 2)))
        except ValueError:
            print('{0} is not a valid price.'.format(price))
            
    def setName(self, name):
        # Set the name of the flower
        try:
            name = str(name)    # Not sure what error this would catch, but it's here to catch errors
            print('Old name: {0}'.format(self._name))
            self._name = name
            print('New name: {0}'.format(self._name))
        except ValueError:
            print('{0} is not a valid name.'.format(name))
            
    def setPetals(self, petals):
        # Set the number of petals on the flower
        try:
            petals = int(petals)    # This is here to catch bad input
            print('Old number of petals: {0}'.format(self._petals))
            self._petals = petals
            print('New number of petals: {0}'.format(self._petals))
        except ValueError:
            print('{0} is not a valid number of petals.'.format(petals))
            
    def setPrice(self, price):
        # Set the price of the flower
        try:
            price = float(price)   # This is here to catch bad input
            print('Old price: {0}'.format(self._price))
            self._price = float('{0:.2f}'.format(round(price, 2)))
            print('New price: {0}'.format(self._price))
        except ValueError:
            print('{0} is not a valid price.'.format(price))
            
    def getName(self):
        # Return the name
        return str(self._name)
            
    def getPetals(self):
        # Return the petals
        return int(self._petals)
        
    def getPrice(self):
        # Return the price
        return float(round(self._price, 2))
        
def R4(name, petals, price):
    # This is a test driver of the Flower class
    print('Test of all functions:')
    testFlower = Flower('Test', 4, 3.50)
    
    print('Name:',testFlower.getName())
    print('Petals:',testFlower.getPetals())
    print('Price:',testFlower.getPrice())
    print()
    testFlower.setName('Banana')
    testFlower.setPetals('Spaghetti')
    testFlower.setPetals(6)
    testFlower.setPrice('Meatball')
    testFlower.setPrice(5)
    print()
    print('Test of user input:')
    userFlower = Flower(R4name, R4petals, R4price)
    print('Name:',userFlower.getName())
    print('Petals:',userFlower.getPetals())
    print('Price:',userFlower.getPrice())

class Vector:
    # Most of this class is copied verbatim from the textbook, as is the nature of the question
    """Represent a vector in a multidimensional space."""
    
    def __init__ (self,d):
        """Create d-dimensional vector of zeros."""
        self._coords = [0] * d

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)
        
    def __getitem__(self,j):
        """Return jth coordinate of vector."""
        return self._coords[j]

    def __setitem__(self,j,val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self,other):
        """Return sum of two vectors."""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __eq__(self,other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords
        
    def __ne__(self,other):
        """Return True if vector differs from other.""" 
        return not self == other
        
    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>'
        
    # This is the one that R-2.13 calls for me to create
    def __rmul__(self, num):
        """Allows for multiplication with the vector as the second value in the expression"""
        result = Vector(len(self))
        for itr in range(len(self)):
            result[itr] = self[itr] * num
        return result
        
    # This is the one that R-2.14 calls for me to create
    # It is based heavily upon the __add__ method established by the textbook
    def __mul__(self, other):
        """Return the scalar sum of two vectors."""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = 0
        for j in range(len(self)):
            result += self[j] * other[j]
        return result
    
def R13():    
    # This is a test driver for the __rmul__ method of the Vector class
    testVector = Vector(4)
    testVector[0] = 1
    testVector[1] = 2
    testVector[2] = 3
    testVector[3] = 4
    print(3 * testVector)
    
def R14():
    # This is a test driver for the __mul__ method of the Vector class
    testVector1 = Vector(4)
    testVector1[0] = 1
    testVector1[1] = 2
    testVector1[2] = 3
    testVector1[3] = 4

    testVector2 = Vector(4)
    testVector2[0] = 4
    testVector2[1] = 3
    testVector2[2] = 2
    testVector2[3] = 1

    print(testVector1 * testVector2)
    
def R16():
    print('The function returns whichever of these is bigger: zero, or the output of ((stop - start + step - 1) // step).')
    print('If it is zero, the function is done.')
    print('Stop is the integer that the function quits on. Start is the integer that the function begins on.')
    print('Step is how many numbers you "move" at a time.')
    print('The function works by calculating the amount of numbers in the range, and divides it by how many numbers it bites off at a time.')
    print('This means that the output is the number of "bites" that the function needs to take.')
    
def R19():
    print('This question can be boiled down to this equation: 2**63 / 2**7')
    print('The answer is:',2**63 / 2**7)
    print('This is over 72 quadrillion.')
    
class CreditCard(object):
    # This is copied verbatim from the textbook, as was the nature of the question
    
    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
        
    def getCustomer(self):
        return self._customer
        
    def getBank(self):
        return self._bank
        
    def getAccount(self):
        return self._account
        
    def getLimit(self):
        return self._limit
        
    def getBalance(self):
        return self._balance
        
    def charge(self, price):
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
    
    def makePayment(self, amount):
        self._balance -= amount
    
class PredatoryCreditCard(CreditCard):
    # This one is also taken from the textbook, as is the nature of the question
    
    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
        self._monthlyCharges = 0 # This is a new one!
        
    def charge(self, price):
        success = super().charge(price)
        if not success:
            self._balance += 5
        else:   # This is new!
            self._monthlyCharges += 1   # This is new!
            if self._monthlyCharges > 10:   #This is new!
                self._balance += 10   # This is new!
        return success
        
    def processMonth(self):
        self._monthlyCharges = 0    # This is new!
        if self._balance > 0:
            monthly_factor = pow(1+ self._apr, 1/12)
            self._balance *= monthly_factor
    
def C28():
    # This is a test driver of the PredatoryCreditCard class' ability to reset every month and charge a fee after 10 charges
    test = PredatoryCreditCard('Jeff', 'First National Bank', '60000', 500000, .14)
    test.charge(500)
    test.charge(500)
    test.charge(500)
    test.charge(500)
    test.charge(500)
    test.charge(500)
    test.charge(500)
    test.charge(500)
    test.charge(500)
    test.charge(500)
    value = round(test.getBalance(), 2)
    print(value)
    print('That value should have been 5000.')
    test.charge(500)
    value = round(test.getBalance(), 2)
    print(value)
    print('That value should have been 5510.')
    test.processMonth()
    value = round(test.getBalance(), 2)
    print(value)
    print('That value should have been more than 5570.49.')
    test.makePayment(5571)
    test.charge(500)
    value = round(test.getBalance(), 2)
    print(value)
    print('That value should have been around 500.')

class Progression:
    # This class is copied from the book, as it the nature of the question
    
    def __init__(self, start=0):
        self._current = start
    
    def _advance(self):
        self._current += 1
        
    def __next__(self):
        if self._current is None:
            raise StopIteration()
        answer = self._current
        self._advance()
        return answer
        
    def __iter__(self):
        return self
        
    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))

class AbsoluteProgression(Progression):
    # This is the class that is asked for in C-2.31
    
    def __init__(self, start=0, previous1=200, previous2=2):
        super().__init__(start)
        self._previous1 = previous1
        self._previous2 = previous2
        
    def _advance(self):
        self._current = abs(self._previous1 - self._previous2)
        self._previous2 = self._previous1
        self._previous1 = self._current
        
def C31(start, previous1, previous2):
    print('Test the defaults: 0, 2, and 200.')
    abs2_200 = AbsoluteProgression()
    abs2_200._advance() # This gets a fresh value into ._current
    for i in range(10):
        print(next(abs2_200), end=' ')
    print('\n')
    print('Test the user input: ' + str(start) + ', ' + str(previous1) + ', and ' + str(previous2) + '.')
    abs_user = AbsoluteProgression(start, previous1, previous2)
    abs2_200._advance() # This gets a fresh value into ._current
    for i in range(10):
        print(next(abs_user), end=' ')
    print()

class RootProgression(Progression):
    # This is the class that is asked for in C-2.32
    
    def __init__(self, start=65536):
        super().__init__(start)
        
    def _advance(self):
        self._current = self._current**(1/2)
        
def C32(start):
    print('Test the default: 65536.')
    root65536 = RootProgression()
    for i in range(10):
        print(next(root65536), end=' ')
    print('\n')
    print('Test the user input: ' + str(start) + '.')
    root_user = RootProgression(start)
    for i in range(10):
        print(next(root_user), end=' ')
    print()
        
def P33(input_string):
    # First, split the input into a list on + and -
    print('This function operates on the assumption that each term is seperated by spaces and denotes exponents with ^.')
    print('It also only supports one variable, and it needs to be "x".')
    input_string = input_string.replace(' - ', ' + -')
    function_list = input_string.split()
    # We now have an array of all of the seperated terms
    
    # The next step is to go element by element and further break them down based upon if they contain an exponent
    true_function_list = []
    for element in function_list:
        if 'x^' in element:
            true_function_list.append(element.split('x^'))
        elif 'x' in element:
            true_function_list.append([element.replace('x', ''), 1])
    
    # Now start building a string containing the answer!
    # Remember that all of the exponents as they currently appear are not yet derived!
    answer = ''
    for piece in true_function_list:
        if str(piece[1]) == '1':
            answer += str(piece[0]) + ' + '
        else:
            answer += str(int(piece[1]) * int(piece[0])) + 'x^' + str(int(piece[1]) - 1) + ' + '
    answer = answer[:-3]
    print('\nThe answer is:',answer)
    
class Polygon(object):
    # This is the base class for P-3.39
    @abstractmethod
    def area():
        return False
        
    @abstractmethod
    def perimeter():
        return False
        
class Triangle(Polygon):
    def __init__(self, side1, side2, side3):
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3
        
    def area(self):
        # This uses Heron's formula
        return (self._side1 + self._side2 + self._side3)/2
        
    def perimeter(self):
        return self._side1 + self._side2 + self._side3
        
class Quadrilateral(Polygon):
    def __init__(self, side1, side2, side3, side4):
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3
        self._side4 = side4
        
    def area(self):
        return 0    # We can't know the area of a quadrilateral without two angles, but implementing those will mess up the subclasses
        
    def perimeter(self):
        return self._side1 + self._side2 + self._side3 + self._side4
        
class Hexagon(Polygon):
    def __init__(self, side):
        # I am assuming that all 6 sides are the same.
        self._side = side
        
    def area(self):
        return ((3 * (3**.5))/2) * self._side**2

    def perimeter(self):
        return self._side * 6
        
class Octagon(Polygon):
    def __init__(self, side):
        # I am assuming that all 8 sides are the same.
        self._side = side
        
    def area(self):
        return 2 * (1 + 2**.5) * self._side**2

    def perimeter(self):
        return self._side * 8
        
class IsoscelesTriangle(Polygon):
    def __init__(self, shared_side, solo_side):
        super().__init__(shared_side, shared_side, solo_side)
        
    def area(self):
        # This uses Heron's formula
        return (self._side1 + self._side2 + self._side3)/2
        
    def perimeter(self):
        return self._side1 + self._side2 + self._side3
        
class EquilateralTriangle(Polygon):
    def __init__(self, side):
        super().__init__(side, side, side)
        
    def area(self):
        # This uses Heron's formula
        return (self._side1 + self._side2 + self._side3)/2
        
    def perimeter(self):
        return self._side1 + self._side2 + self._side3
        
class Rectangle(Quadrilateral):
    def __init__(self, side1, side2):
        super().__init__(side1, side1, side2, side2)
        # This means that side1 and side2 are equal, as are side3 and side4
    
    def area(self):
        return self._side1 * self._side3
        
    def perimeter(self):
        return self._side1 * 2 + self._side3 * 2
        
class Square(Quadrilateral):
    def __init__(self, side):
        super().__init__(side, side, side, side)
    
    def area(self):
        return self._side1 * self._side1
        
    def perimeter(self):
        return self._side1 * 4

def P39():
    print('The code for these classes is found starting on line 453.')
    print('The diagram was submitted to the proper dropbox.')
    
main()