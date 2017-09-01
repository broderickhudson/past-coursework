# Code by Broderick Hudson
# This code is all mine. I promise.
# Assignment 1

# Import statements
import math
import random

def main():
    ##################################
    # ALL VARIABLES ARE DEFINED HERE #
    R14int = 5
    R112sequence = [1,2,3,5,8,13,21]
    C114list = [1,2,3,4,5,6,7,8,9,10]
    C122array_1 = [5,4,3,2,1]
    C122array_2 = [6,7,8,9]
    C128vector = [5,18,4]
    P136word_list = ['i', 'am', 'a', 'banana', 'and', 'i', 'am', 'also', 'tired', 'of', 'thinking', 'of', 'words', 'to', 'write', 'in', 'this', 'list']
    
    # Run all the stuff
    R14(R14int)
    R111()
    R112(R112sequence)
    C114(C114list)
    C119()
    C121()
    C122(C122array_1, C122array_2)
    C123()
    C127()
    C128(C128vector)
    P136(P136word_list)
    
def R14(integer):
    print("\nThis is question: R1.4")
    try:
        integer = int(integer)
        if integer > 0:
            square_sum = 0
            for itr in range(1, integer):
                square_sum += math.sqrt(itr)
            print("The sum of the square of each integer between 1 and",integer,"is:",round(square_sum, 4))
        else:
            print(integer,"is not greater than 0.")
    except (ValueError, TypeError):
        print("The entry",integer,"is not an integer.")
    
def R111():
    print("\nThis is question: R1.11")
    answer = [2**itr for itr in range(0,9)]
    print("This list was created using list comprehension syntax:",answer)

def R112(sequence):
    print("\nThis is question: R1.12")
    if len(sequence) == 0:
        print("The sequence has been emptied. Fix that!")
    else:
        print("The sequence is defined in the code. Feel free to change it!")
        print("The sequence is currently:",sequence)
        rand_in_set = False
        while not rand_in_set:
            grabbed = random.randrange(min(sequence), max(sequence)+1)
            if grabbed in sequence:
                rand_in_set = True
        print("The produced number is:",grabbed)
        
def C114(input_list):
    print("\nThis is question: C1.14")
    answers = []
    for itr1 in range(0, len(input_list)):
        for itr2 in range(itr1 + 1, len(input_list)):
            if (input_list[itr1] * input_list[itr2]) % 2 == 1:
                answers.append(str(input_list[itr1]) + " and " + str(input_list[itr2]))
    if len(answers) > 0:
        for value in answers:
            print(value)
        
def C119():
    # ord takes strings and returns unicode numbers, chr takes unicode numbers and returns strings
    print("\nThis is question: C1.19")
    answer = [chr(itr) for itr in range(ord('a'), ord('z') + 1)]
    print("This list was created using list comprehension syntax:",answer)
    
def C121():
    print("\nThis is question: C1.21")
    print("Pressing ctrl+D ends the input and raises the needed error. You will need to do this at some point.")
    print('Just in case, enter "banana phone" to raise the EOFError.')
    answer = []
    try:
        while 1 == 1: # This is a tautology
            append_string = str(input("Enter something: "))
            if append_string == 'banana phone':
                raise EOFError
            else:
                answer.append(append_string)
    except EOFError:
        if len(answer) > 0:
            print("Error message receieved, now printing backwards.")
            itr = -1
            while itr > (len(answer) + 1) * -1:
                print(answer[itr])
                itr -= 1
        else:
            print("The list was empty.")
        
def C122(array1, array2):
    print("\nThis is question: C1.22")
    answer_array = []

    # The arrays need to be the same length. Use this flag to determine whether or not a special message should be printed
    modified = False
    
    # Ensure that the two arrays are the same length
    if len(array1) > 0 and len(array2) > 0:
        while len(array1) != len(array2):
            modified = True
            if len(array1) > len(array2):
                array2.append(1)
            else:
                array1.append(1)
    
        # Now that they are the same length, create the new array
        for itr in range(0, len(array1)):
            answer_array.append(array1[itr] * array2[itr])
        if modified:
            print("The given arrays were not the same length. They were made the same length by adding 1 to the end of the shorter one.")
        print("Array #1:",array1)
        print("Array #2:",array2)
        print("By multiplying these together, we get...")
        print("Array #3:",answer_array)
    
    else:
        print("One of those arrays was empty. That won't work.")
            
def C123():
    print("\nThis is question: C1.23")
    dark_souls_bosses = ['Asylum Demon','Taurus Demon','Bell Gargoyles','Capra Demon','Gaping Dragon','Moonlight Butterfly','Chaos Witch Quelaag','Sif, the Great White Wolf','Pinwheel','Iron Golem','Ornstein and Smough','Gwynevere','Seath the Scaleless','Gravelord Nito','Ceaseless Discharge','Centipede Demon','Demon Firesage','Bed of Izaleth','The Four Kings','The last boss?']
    # There are 20 bosses in Dark Souls. The last one is supposed to be Gwyn.
    gwyndex = eval(input("In the original Dark Souls, what is Gwyn's cardinality? I'm pretty sure it's 20. Enter the integer: "))
    try:
        dark_souls_bosses[gwyndex-1] = 'Gwyn, Lord of Cinder'
        print("You picked a number that doesn't cause an error! Yay!")
    except IndexError:
        dark_souls_bosses[19] = 'Gwyn, Lord of Cinder'
        print("This is the error that I'm supposed to demonstrate working around. Yay!")
    except ValueError:
        print("You didn't enter an integer.")
    
def C127Generator(n):
    # This one is based on something copied out of the book, as was the nature of the question
    k = 1
    while k <= n:
        if n % k == 0:
            yield k
        elif k * k == n:
            yield k
        k += 1
    
def C127():
    print("\nThis is question: C1.27")
    factor_me = input("Enter a number to factor: ")
    try:
        factor_me = int(factor_me)
        generator = C127Generator(factor_me)
        for value in generator:
            print(value)
    except (ValueError, TypeError):
        print("The entry",factor_me,"is not an integer.")

def norm(vector, p=2):
    try:
        squared_sum = 0
        p = int(p) # This is just to catch faulty input
        print(p)
        for value in vector:
            value = int(value) # This is also just for catching faulty input
            squared_sum += value**p
        return squared_sum**(1/p)
    except (ValueError, TypeError):
        print("The values passed were not both integers.")

def C128(vector):
    print("\nThis is question: C1.28")
    try:
        p = input("Enter a p-value, or press Enter for the default: ")
        answer = 0
        if p == '':
            answer = norm(vector)
        else:
            p = int(p)
            answer = norm(vector, p)
        print("The answer is:",round(answer, 3))
    except (ValueError, TypeError):
        print("An argument passed was not an integer.")

def P136(word_list):
    print("\nThis is question: P1.36")
    # Create a list containing each distinct element in word_list
    answer = []
    for word in word_list:
        if word not in answer:
            answer.append(word)
    
    # Now print the list
    for word in answer:
        print("%-15s: %i" % (word, word_list.count(word)))
                
main()