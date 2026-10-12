#Grade Checker
ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4]) #1st 2nd 3rd prefix

Units = []
Grades = []
UxG = []

def getSubjects(): # get all subjects from user

    print()
    Subjects = int(input("How many subjects you have: "))
    i = 0
    print()
    for i in range(Subjects):
        order = ordinal(i + 1)
        
        grade = float(input(f"Enter {order} Subject Grade: "))
        
        unit = float(input(f"Enter {order} Subject Units: "))
        print()
        Grades.append(grade)
        Units.append(unit)
        i = i + 1  
    return Subjects   

def getWeightedAverage(a =[], b=[]):
    
    for i in range(Subjects):
        uxg = a[i] * b[i]
        UxG.append(uxg)
        
    totalUxG = sum (UxG)
    
    totalUnits = sum(Units)
    Average = totalUxG / totalUnits
    print("Total Units this semester:", totalUnits)
    print("Your General Weighted Average this semester:", f"{Average:.2f}\n")
    '''
    ignore this, its just debug stuff
    totalGrades = sum(Grades)
    print(UxG)
    print(totalUxG)
    print(totalGrades)  
    print(totalUnits)
    '''
    return Average

def MockorPraise(average):
    if average <= 1.45:
        print("Congratulations! you're a Presidents lister!")
    elif average <= 1.75:
        print("Congratulations! you're a Deans lister!")
    elif average <= 3.00:
        print("Congratulations! you Survived! Ready for the next round?")
    elif average <= 4.00:
        print("Well, better luck next semester..")
    elif average >= 5.00:
        print("HAHAHAHAHHAHAHAHHAHAHHAHAHHA, what the hell did you do?")
        
        
Subjects = getSubjects()
'''
print (Grades)
print (Units)
print(f"{average:.2f}")
'''
average = getWeightedAverage(Grades, Units)
MockorPraise(average)
