"""Structured-english
start
We need to decide which form of payment is higher, Option1 or Option2
Option1 is 100 dollars a day for ten days
Option2 is 1 dollar the first day then doubles each day (1,2,4,8, etc)
First we need to calulate the total pay for each option
Option1 = 100 * 10
Option2 = (1+2+4+8, etc) till list indexs reachs 9
If option1 == option2, then print "Option1 and Option2 pays the same"
Then, if option one is higher print "Option1 is better" to the console
Else print "Option2 is better"
end
"""
"""Pseudo-code
start
option1(100)
option2(1)
define option1(option1)
    option1 * 10
    return option1
define option2(option2)
    count = 0
    indexTotal = 10
    while count is less than index total
        option2 *=2
        count += 1
    subtract 1 from total option2-1
    return option2
var1 = option1(100)
var2 = option2(1)
define compairTotals()
    if option1 is equal to option two
        print "Option1 and option2 pays the same"
    If option1 is greater than option2
        print "Option1 is better"
    Else
        print "Option2 is better"
compairTotals()
end
"""

def option1(option1):
    option1 *= 10
    return option1
def option2(option2):
    count = 0
    total = 10
    while count < total:
        option2 *= 2
        count += 1
    option2 -=1
    return option2
var1 = option1(100)
var2 = option2(1)
def compairTotals():
    if var1==var2:
        print("Option 1 and Option 2 pays the same")
    if var1 > var2:
        difference = var1 - var2
        print("Option 1 is better")
    else:
        difference = var2 - var1
        print("Option 2 is better")
compairTotals()