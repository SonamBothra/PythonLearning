
""" use if at the end if you want to pass the else condition i.e. if you dont have an else condition
    multipliers_of_seven_comprehension COMPUTES ALL THE MULTIPLES OF SEVEN IN THE RANGE 1 TO 100
"""
def multipliers_of_seven_comprehension():
    return[num for num in range(1,100) if(num%7==0)]

#get a list of True or False for multipliers of 3
def multipliers_of_three_comprehension():
    return[True if(num%3==0) else False for num in range(1,11)]


#Given a list names, return only those names which have second letter as 'a'
def second_character_a(in_list):
    return [name for name in in_list if(name[1]=='a')]


#Given a list names, return the list of names in title case.
def title_case_name(in_list):
    return[name.capitalize() for name in in_list]


#Given a string, return only the digits in it
def find_digits(in_list):
    return [name for name in in_list if(name.isdigit())]


#list comprehensions for multiple if conditions. In range of 1-10, list numbers if divisible by 2, if yes, check if divisible by 4.
def multiple_list_comprehension():
    return [num for num in range(1,11) if(num%2==0) if(num%4==0)]



#Doubles the elements present inside the list and returns the empty list if the variable passed is not of list type
def double_list(in_list):
    if type(in_list)== type([]):
        outlist=[]
        for element in in_list:
            outlist.append(element*2)
        return outlist
    else:
        return []

#Return double of the element but implemented using comprehensions
def double_list_comprehension(in_list):
    return [element*2 for element in list]


#Find the even elements in the range of 1 to 100
def find_even():
    outlist=[]
    for e in range(1,100):
        if(e % 2) == 0:
            outlist.append(e)
    return outlist



def find_even_comprehension():
        return [e if e%2==0 else None for e in range(1,100)]

if __name__== '__main__':
    print(double_list([1,2,3,4]))
    print(double_list(123))
    print(find_even())
    print(find_even_comprehension())
    print(multipliers_of_seven_comprehension())
    print(multipliers_of_three_comprehension())
    print(second_character_a(["sonam", "pavani", "sindhu", "madhu", "Savita", "Sujana", "neha"]))
    print(title_case_name(["sonam", "pavani", "sindhu", "madhu", "Savita", "Sujana", "neha"]))
    print(find_digits("My WWID is 11721155. How about yours?"))
    print(multiple_list_comprehension())