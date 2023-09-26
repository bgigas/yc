import math


# Recursivly calculate a factorial.  Prints each step in the call stack.
def factorial(num):
   call_stack = []
   if num == 1:
       print('base case reached! Num is 1.')
       return 1
   else:
       call_stack.append({'input': num})
       print('call stack: ', call_stack)
       return num * factorial(num-1)
#print(factorial(20))


# Calculate dog years using a lambda
dog_years = lambda x: x * 7
#print(dog_years(7))


# Returns true if a number is evenly divisible by 10
def divby10(num1):
    return num1 % 10 == 0
#print(divby10(20))


# Iterates through a list of numbers and prints all that are divisible by a second input, then shows the count
def divBy(nums, div):
    count = 0
    for num in nums:
        if num % div == 0:
            count += 1
            print(num)
    print(f"There were {str(count)} items divisible by {div}")
#divBy([1,3,5,10,20,35,100,300], 3)


# Given a list of numbers, removes all the starting even nums until the first odd number
def removenums(nums):
    tempnums = []
    test = 0
    for num in nums:
        if num % 2 != 0:
            tempnums.append(num)
            test = 1
        elif test != 0:
            tempnums.append(num)
    print(tempnums)
#removenums([2,4,5,8,7,9])


# Given a list of numbers, prints only odd numbers
def odd(nums):
    tempnums = []
    for num in nums:
        if nums.index(num) % 2 == 0:
            tempnums.append(num)
    print(tempnums)
#odd([5,7,1,4,6,9,19])


# Print calculations on a list of bases and a list of exponents
def exps(nums, pows):
    tempnums = []
    for num in nums:
        for pow in pows:
            tempnums.append(num ** pow)
    print(tempnums)
#exps([4,2,3],[1,2,3])


# Adds each number in two lists and figures out which list's sum is higher.
def largersum(nums1, nums2):
    sum1 = 0
    sum2 = 0
    for num in nums1:
        sum1 += num
    for num in nums2:
        sum2 += num
    if sum1 > sum2:
        print(str(sum1))
    elif sum2 > sum1:
        print(str(sum2))
    else:
        print('Both equal: ' + str(sum1))
#largersum([2,2,3],[1,3,3])


# Prints the max number in a list
def findmax(nums):
    max = 0
    for num in nums:
        if num > max:
            max = num
    print(max)
#findmax([1,4,8,3,7,10])


# Given two lists of numbers, print the nums that repeat in both lists
def findrepeats(nums1, nums2):
    tempnums = []
    for num1 in nums1:
        for num2 in nums2:
            if (num1 == num2):
                tempnums.append(num1)
    print(tempnums)
#findrepeats([1,2,3,4],[1,7,3,5])


# Given two sets of number, returns true is set 2 is set 1 in reverse order
def arereversed(nums1, nums2):
    boolreversed = True
    max = len(nums2)
    y = 0

    for i in nums1:
        if i == nums2[max-y-1]:
            boolreversed == True
            y+=1
        else:
            boolreversed = False
            return False
    return True
#print(arereversed([1,2,3,4],[4,3,2,1]))

    
# Tests two numbers to see if a base and exponent are >= 5000
def testpow(base, exp):
    print(base ** exp)
    if base ** exp >= 5000:
        return True
    else:
        return False
#print(testpow(3,20))


# Tests if the budget is greater than three specified bills
def budget(buj, bill1, bill2, bill3):
    return buj >= (bill1 + bill2 + bill3)
#print(budget(10000, 1000, 2000, 5000))


# Extension of above, tests if budget is greater than a list of bills
def budget(buj, bills):
    billTotal = 0
    for bill in bills:
        billTotal += bill
    return buj >= billTotal
#print(budget(1000,[10,500,20]))


# Returns true if first number is twice the second
def twice(num1, num2):
    return num1 == num2 * 2
#print(twice(4,1))


# Returns true if the sum of two inputs is 10
def sum10(num1, num2):
    return num1 + num2 == 10
#print(sum10(2,8))


# Tests if a number is between two other numbers
def inRange(num1, num2, num3):
    return (num1 > num2) and (num1 < num3)
#print(inRange(2,1,3))


# Simple conditional based on an input.  Returns a review based on a rating number.
def rating(num):
    if num >= 0 and num <= 3:
        return "Bad, stay away!"
    elif num > 3 and num < 7:
        return "Meh"
    elif num >= 8 and num <= 10:
        return "Def see it"
    else:
        return "Nonsensical rating"
#print(rating(10))


# Returns the max number in a list
def maxNums(nums):
    currentMax = 0
    for num in nums:
        if num >= currentMax:
            currentMax = num
    return currentMax
#print(maxNums([1,4,64,2]))


# Returns a number to the 10th power
def tenthPow(num):
    return num ** 10
#print(tenthPow(3))


# Returns the square root of a number
def sqrt(num):
    return num ** 0.5
#print(sqrt(16))


# Returns a winrate given a number of wins and losses
def winloss(wins, losses):
    return int((wins / (wins + losses)) * 100)
#print(winloss(10,8), '%')


# Computes the average of two number
def ave(num1, num2):
    return (num1 + num2) / 2
#print(ave(3,2))


# Computes the average of a list of numbers
def ave(nums):
    numerator = 0
    for num in nums:
        numerator += num
    return numerator / len(nums)
#print(ave([2,2,5,8]))


# Prints the first three multiples of a number and returns the sum of those numbers
def threemults(num):
    print(num, num*2, num*3)
    return num + num*2 + num*3
#print(threemults(3))


# Calculates a tip based on a percentage
def tip(total, percentage):
    return total * (percentage / 100)
#print(tip(50,20))


# Given a list, append the addition of the last and second to last items three times
def listMod1(lst):
    i = 1
    while (i <= 3):
        lst.append(lst[-2] + lst[-1])
        i+=1
    return lst
#print(listMod1([1,2,3,4]))


# Given a list of numbers, return true if a (num) is present at least (occur) times
def convey(lst1, num, occur):
    return lst1.count(num) >= occur
#print(convey([1,2,2,3], 2, 2))


# Combine and sort two lists of numbers
def combineSort(lst1, lst2):
    lst1 =  lst1 + lst2
    lst1.sort()
    return lst1
#print(combineSort([5,2,3],[4,2,6]))


# Given a numerical input, return the set of numbers from x to 100, only displaying every third number
def everyThree(num):
    templst = []
    while (num <= 100):
        templst.append(num)
        num=num+3
    return templst
#print(everyThree(70))


# Does the same thing as above, just uses the range function built into python
def everyThree1(num):
    return list(range(num, 100, 3))
#print(everyThree1(50))


# Given a list of items, returns the list with the specified chunk removed
def removeMid(lst, start, end):
    return lst[:start] + lst[end:]
#print(removeMid([1,2,3,4,5,6,7,8,9,0], 2, 5))


# Given a list, return the item that appears most often
def frequentItem(lst, num1, num2):
    x = 0
    y = 0
    for i in lst:
        if i == num1:
            x += 1
        if i == num2:
            y += 1
    if x > y:
        return x
    if y > x:
        return y
    if y == x:
        return f"{num1} and {num2} both appear {x} times."
#print(frequentItem([1,2,2,3,3,4],2,3))


# Same as above but using the .count method in python
def frequentItem1(lst, num1, num2):
    x = lst.count(num1)
    y = lst.count(num2)
    return f"{num1}: {x}, {num2}: {y}"
#print(frequentItem1([1,2,2,3,3,4],1,3))


# Doubles the item at (index) and adds the total to the index+1 position in a list
def doubleIndex(lst, index):
    if index < 0:
        return lst
    elif index >= len(lst):
        return "Index out of bounds"
    else:
        lst.insert(index+1, lst[index]*2)
        return lst
#print(doubleIndex([1,2,3,4],2))


# Returns the middle element in a list.  If list has even number of elements, return average of middle two.
def returnMid(lst):
    if len(lst) % 2 == 1:
        return lst[int(len(lst)/2)]
    else: 
        return (lst[int((len(lst)-1)/2)] + lst[int(len(lst)/2)]) / 2
#print(returnMid([1,2,3,4,5,6]))
