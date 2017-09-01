# Homework 4
# IT310, Broderick Hudson
# I promise that all of the code within is my own.

# Make all important imports
import webbrowser

# Define all elements used in the functions
P41List = [0,1,2,3,4,50000,6,7,8,9000]
P46n = 5
P47str = '12345678'
P412m = -5
P412n = -6
P416str = 'Join the Navy'
P420list = [6,10,8,2,5,1,4,7,11,3,9]
P420point = 6
P421list = [5,6,7,8,9,10,11,12,13,14,15,16]
P421desiredSum = 20
P422m = -5
P422n = -6

def main():
    print("Enter a number to display the corresponding problem's output/answer.")
    print('0:  Exit the program.')
    print('1:  4.1')
    print('2:  4.3')
    print('3:  4.6')
    print('4:  4.7')
    print('5:  4.12')
    print('6:  4.13')
    print('7:  4.16')
    print('8:  4.20')
    print('9:  4.21')
    print('10: 4.22')
    continu = True
    while continu:
        inputVal = str(input('Enter a number: '))
        if inputVal == '0':
            continu = False
            print('Exiting the program.')
        elif inputVal == '1':
            print('\nProblem 4.1')
            print('Largest Number:',P41(P41List, P41List[-1]))
            print('Running time  : O(n)')
            print('Space usage   : n')
        elif inputVal == '2':
            print('\nProblem 4.3')
            openWeb = str(input('This problem opens an Imgur page that displays the answer. Do you want to do this? Y/N: ')).lower()
            if openWeb == 'y':
                webbrowser.open('http://i.imgur.com/KX7UrfF.jpg', new=1, autoraise=True)
                print('The recursive trace has opened.')
            elif openWeb == 'n':
                print('The window is not being opened. I put the image at "http://i.imgur.com/KX7UrfF.jpg"')
            else:
                print('Command not recognized. Returning to main menu.')
        elif inputVal == '3':
            print('\nProblem 4.6')
            print('The harmonic number with input =',P46n,'is:')
            print(round(P46(P46n), 5))
        elif inputVal == '4':
            print('\nProblem 4.7')
            print('With input = ' + P47str + ':')
            print(P47(P47str))
        elif inputVal == '5':
            print('\nProblem 4.12')
            print('With inputs',P412m,'and',str(P412n)+':')
            print(P412(P412m,P412n))
        elif inputVal == '6':
            print('\nProblem 4.13')
            openWeb = str(input('This problem opens an Imgur page that displays the answer. Do you want to do this? Y/N: ')).lower()
            if openWeb == 'y':
                webbrowser.open('http://i.imgur.com/V0wKKc2.jpg', new=1, autoraise=True)
                print('An image of the proof has opened.')
            elif openWeb == 'n':
                print('The window is not being opened. I put the image at "http://i.imgur.com/V0wKKc2.jpg"')
            else:
                print('Command not recognized. Returning to main menu.')
        elif inputVal == '7':
            print('\nProblem 4.16')
            print('With input = ' + P416str + ':')
            print(P416(P416str))
        elif inputVal == '8':
            print('\nProblem 4.20')
            print('With inputs',P420list,'and',str(P420point)+':')
            print(P420(P420list,P420point))
            print('It has a running time of O(n)')
        elif inputVal == '9':
            print('\nProblem 4.21')
            print('With inputs',P421list,'and',str(P421desiredSum)+':')
            print(P421(P421list,P421desiredSum))
            print('It has a running time of O(n^2)')
        elif inputVal == '10':
            print('\nProblem 4.22')
            print('With inputs',P422m,'and',str(P422n)+':')
            print(P422(P422m,P422n))
        else:
            print(inputVal,'is not a valid input. Try again.')
            
def P41(inList, largest):
    if len(inList) == 1:
        return largest
    elif inList[-1] > largest:
        return P41(inList[:-1], inList[-1])
    else:
        return P41(inList[:-1], largest)
    
def P46(n):
    if n == 1:
        return 1
    else:
        return 1/n + P46(n-1)
    
def P47(string):
    if len(string) < 4:
        return string
    else:
        return P47(string[:-3]) + ',' + string[-3:]
    
def P412(m,n):
    if n > 0:
        return m + P412(m, n-1)
    elif n < 0:
        return - (m - P412(m, n+1))
    elif n == 0:
        return 0
    
def P416(string):
    if len(string) == 1:
        return string
    else:
        return P416(string[1:]) + string[0]
    
def P420(array, point, shortList = [], longList = []):
    if len(array) == 1:
        return shortList + longList
    if array[0] <= point:
        shortList.append(array[0])
        return P420(array[1:], point, shortList, longList)
    else:
        longList.append(array[0])
        return P420(array[1:], point, shortList, longList)

def P421(array, desiredSum):
    if len(array) == 1:
        return False
    else:
        first = array[0]
        for element in array[1:]:
            if element == desiredSum - first:
                return first,element
        # If it made it here, try again
        return P421(array[1:], desiredSum)
    
def P422(m,n):
    total = 0
    if n == 0:
        return 0
    elif n > 0:
        while n > 0:
            total += m
            n -= 1
        return total
    elif n < 0:
        while n < 0:
            total -= m
            n += 1
        return total
    

main()
    