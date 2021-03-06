#Question 1
# Recursive function to solve the tower of hanoi
print('-------------------------Question 1-------------------------')

def TowerOfHanoi(n , source, destination, auxiliary):
	if n==1:
		print ("Move disk 1 from source",source,"to destination",destination)
		return
	TowerOfHanoi(n-1, source, auxiliary, destination)
	print ("Move disk",n,"from source",source,"to destination",destination)
	TowerOfHanoi(n-1, auxiliary, destination, source)
n = 4
TowerOfHanoi(n,'A','B','C')  # A, C, B are the name of rods

#Question 2
#To print Pascal's Triangle
print('-------------------------Question 2-------------------------')
#Using Loop
rows = int(input("Enter number of rows: "))
coef = 1

for i in range(1, rows+1):
    for space in range(1, rows-i+1):
        print(" ",end="")
    for j in range(0, i):
        if j==0 or i==0:
            coef = 1
        else:
            coef = coef * (i - j)//j
        print(coef, end = " ")
    print()
#Using recursive function
def pascals_triangle(n):
    if n == 1:
        return [[1]] # Base case termination condition
    else:
        result = pascals_triangle(n-1) # Recursive call
        # Calculate current row using info from previous row
        current_row = [1]
        previous_row = result[-1] # Take from end of result
        for i in range(len(previous_row)-1):
            current_row.append(previous_row[i] + previous_row[i+1])
        current_row += [1]
        result.append(current_row)
        return result

rows=int(input('Enter rows: '))
triangle = pascals_triangle(rows)
for row in triangle:
   print(row)
   
#Question 3
#Built in functions
print('-------------------------Question 3-------------------------')

a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
tup = divmod(a,b)#to print quietiont and remainder
print(tup)
# code to find whether values are callable or not
print(callable(tup))
# code to find whether all elements are zero
if tup == (0,0):
    print ('All values are zeros')
else :
    print ('Values are nonzeros')
tup1= tup+(4,5,6)
#filter out the values which are greater than 4
numbers = filter(lambda n: n > 4, tup1)
list1=list(numbers)
print('values greater than 4 :',list1)
set1 = set(list1)
print(set1)
newset = frozenset(set1)
print('New immutable set ',newset)
print ('Maximum value in set is ',max(newset))
print('The hash value of set is ,',hash(newset))


#Question 4
#To create a class
print('-------------------------Question 4-------------------------')
class Student:
    def __init__(self,name,rollnumber):
        self.name = name
        self.rollnumber = rollnumber
    def object(self):
        print ('Name ='+self.name)
        print ('Rollnumber =',self.rollnumber)
c = Student("Naheed Anjum",21104002)
c.object()
del c  #Deleting object c

#Question 5
#Program to store details of three employees: name and salary using class.
print('-------------------------Question 5-------------------------')

class details :
    def __init__(self,Employee,Name,Salary):
        self.Employee = Employee
        self.Name = Name
        self.Salary = Salary
    def record(self):
        print(self.Employee,end=" ")
        print(self.Name,end=" ")
        print(self.Salary,end=" ")
        print()
p1 = details(1,'Mehak',40000)
p1.record()
p2 = details(2,'Ashok',50000)
p2.record()
p3 = details(3,'Viren',60000)
p3.record()
p1.Salary=70000
print('Updated details of Mehak:',end=" ")
p1.record()
del p3

#Question 6
#Friendship Test
print('-------------------------Question 6-------------------------')

def code(gword):
    print ('Word spoken by George:',gword)
    bword = input('Word formed by Barbie:')
    length = len(bword)
    count = 0
    for i in bword :
         if i in gword :
             count = count + 1
         else :
             break
    if count == length :
        print('Barbie is a good friend')
    else :
        print('Barbie is not a good friend')
        
George = input("Enter word said by George :")
code(George)
