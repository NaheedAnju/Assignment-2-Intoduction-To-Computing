#Question 1
#To count the number of occurrences of each character in the string entered by the user.
print('-------------------------Question 1-------------------------')
word = input('Enter a single word - ')
count_a=0
count_b=0
count_c=0
count_d=0
count_e=0
count_f=0
count_g=0
count_h=0
count_i=0
count_j=0
count_k=0
count_l=0
count_m=0
count_n=0
count_o=0
count_p=0
count_q=0
count_r=0
count_s=0
count_t=0
count_u=0
count_v=0
count_w=0
count_x=0
count_y=0
count_z=0
for i in word:
    if i=='a' or i=='A':
        count_a += 1
    elif i=='b' or i=='B':
        count_b += 1
    elif i=='c' or i=='C':
        count_c += 1
    elif i=='d' or i=='D':
        count_d += 1
    elif i=='e' or i=='E':
        count_e += 1
    elif i=='f' or i=='F':
        count_f += 1
    elif i=='g' or i=='G':
        count_g += 1
    elif i=='h'  or i=='H':
        count_h += 1
    elif i=='i' or i=='I':
        count_i += 1
    elif i=='j' or i=='J':
        count_k += 1
    elif i=='l' or i=='L':
        count_l += 1
    elif i=='m' or i=='M':
        count_m += 1
    elif i=='n' or i=='N':
        count_n += 1
    elif i=='o' or i=='O':
        count_o += 1
    elif i=='p'  or i=='P':
        count_p += 1
    elif i=='r' or i=='R':
        count_r += 1
    elif i=='s' or i=='S':
        count_s += 1
    elif i=='t' or i=='T' :
        count_t += 1
    elif i=='u' or i=='U':
        count_u += 1
    elif i=='v' or i=='V':
        count_v += 1
    elif i=='x' or i=='X':
        count_x += 1
    elif i=='w' or i=='W':
        count_w += 1
    elif i=='y' or i=='Y':
        count_y += 1
    elif i=='z' or i=='Z':
        count_z += 1
print('No. of a = ', count_a)
print('No. of b = ', count_b)
print('No. of c = ', count_c)
print('No. of d = ', count_d)
print('No. of e = ', count_e)
print('No. of f = ', count_f)
print('No. of g = ', count_g)
print('No. of h = ', count_h)
print('No. of i = ', count_i)
print('No. of j = ', count_j)
print('No. of k = ', count_k)
print('No. of l = ', count_l)
print('No. of m = ', count_m)
print('No. of n = ', count_n)
print('No. of o = ', count_o)
print('No. of p = ', count_p)
print('No. of q = ', count_q)
print('No. of r = ', count_r)
print('No. of s = ', count_s)
print('No. of t = ', count_t)
print('No. of u = ', count_u)
print('No. of v = ', count_v)
print('No. of w = ', count_w)
print('No. of x = ', count_x)
print('No. of y = ', count_y)
print('No. of z = ', count_z)

#Question 2
#To print next date of input date
print('-------------------------Question 2-------------------------')
day = int(input('Enter  DAY - '))
month = int(input('Enter MONTH - '))
year = int(input('Enter YEAR - '))
if month in [1,3,5,7,8,10]:
    if day == 31:
          next_month = month+1
          next_day = 1
          next_year = year
    elif day <31:
        next_month = month
        next_day = day + 1
        next_year = year
elif month in [4,6,9,11]:
    if day == 30:
        next_month = month+1
        next_day = 1
        next_year = year
    elif day < 30:
        next_month = month
        next_day = day + 1
        next_year = year
elif month == 12:
    if day == 31:
        next_month = 1
        next_day = 1
        next_year = year + 1
    if day < 31:
        next_month = month
        next_day = day + 1
        next_year = year
elif month == 2:
    if year%4==0:
        if day ==28:
            next_month = month
            next_day = 29
            next_year = year
        elif day == 29 :
            next_month = month+1
            next_day = 1
            next_year = year
        elif day < 28 :
            next_month = month
            next_day = day + 1
            next_year = year
    else :
        if day ==28:
            next_month = month+1
            next_day = 1
            next_year = year
        elif day < 28:
            next_month = month
            next_day = day + 1
            next_year = year
print('Next date is : ',next_day,'/',next_month,'/',next_year)

#Question 3
#To create a list of tuples with the first element as the number and Second element as the square of the number.
print('-------------------------Question 3-------------------------')

n=int(input('Enter number of values to input in list- '))
list_0 = []
list1 = []
for i in range (n) :
    value = int(input('Enter Value- '))
    list_0 = list_0 + [value]
for i in list_0 :
    k = i*i
    list1 = list1 + [(i,k)]
print (list1)

#Question 4
#To prompt the user for a grade between 4 and 10.
print('-------------------------Question 4-------------------------')

grade_point = int(input('Enter grade points - '))
if grade_point == 10:
    print('Your Grade is \�A+\' and Outstanding Performance')
elif grade_point == 9:
    print('Your Grade is \'A\' and Excellent Performance')
elif grade_point == 8:
    print('Your Grade is \'B+\' and Very Good Performance')
elif grade_point == 7:
    print('Your Grade is \'B\' and Good Performance')
elif grade_point == 6:
    print('Your Grade is \'C+\' and Average Performance')
elif grade_point == 5:
    print('Your Grade is \'C\' and Below Average Performance')
elif grade_point == 4 :
    print('Your Grade is \'D\' and Poor Performance')
else:
    print('Grade Point out of range')

#Question 5
#Inverese Pyramid Pattern
print('-------------------------Question 5-------------------------')

n = int(input('Enter no. of rows - '))
for i in range(n,0,-1):
    for j in range(n-i ):#To print spaces
        print(' ', end='')
    for k in range(2 * i - 1):#To print alphabet
        print(chr(65 + k), end='')
    print()

#Question 6
#Opetations on Dictionary
print('-------------------------Question 6-------------------------')

dictionary = {}
answer = 'Y'
while answer == 'Y' or answer == 'y' :
    s_sid = input('Enter student\'s SID - ')
    s_name = input('Enter student\' name - ')
    dictionary[s_sid] = s_name
    answer = input('Do you want to add more name (Y/N)?')
#Printing students details stored in the dictionary
print('Student Details - ',dictionary)


#Sorting Dictinary using student's name
list_1 = []
for i,k in dictionary.items() :
    tup = (k,i)#adds sid and name in (name,sid) format so that list can be sorted by name
    list_1.append(tup)

sort_dict = {}
list_1 = sorted(list_1)
for j in list_1 :
    sort_dict[j[1]] = j[0]
print('sorted dictiionary on the basis of name - ' , sort_dict)
    
#Sorting Dictionary by SID

list_2 = []
for x,y in dictionary.items() :
    tup = (x,y)#adds sid and name in (sid,name) format so that list can be sorted by sid
    list_2.append(tup)

sort_dict_1 = {}
list_2 = sorted(list_2)
for z in list_2 :
    sort_dict_1[z[0]] = z[1]
print('sorted dictiionary on the basis of SID - ' , sort_dict_1)

#Searching a student's name and printing its name
search = input('Enter SID of student to search name - ')
for a,b in dictionary.items() :
    if search == a :
        print('Student\'s name with sid',search,'is',b)

#Question 7
#Fiboncci series
print('-------------------------Question 7-------------------------')

limit = int(input('Enter limit - '))
x=0
y=1
z=1
list_1 = [0,1,]
print(x,y,end=' ')
while z <= limit :
    print(z,end=' ')
    list_1.append(z)
    x=y 
    y=z
    z=x+y
print()
print(list_1)
sum = 0
for c in list_1 :
    sum = sum + c
average = sum/len(list_1)
print ("Average of Fiboncci Series - ", average)
#Question 8
#Operations on sets
print('-------------------------Question 8-------------------------')


set1= {1, 2, 3, 4, 5}
set2= {2, 4, 6, 8}
set3= {1, 5, 9, 13, 17}
# To create a new set of all elements that are in Set1 and Set2 but not both
print("New set of all elements that are in Set1 and Set2 but not both",set1.symmetric_difference(set2))
inter1_2 = set1.symmetric_difference(set2)
# To create a new set of all elements that are in Set2 and Set3 but not both
inter2_3 = set2.symmetric_difference(set3)
# Elements in intersction of set1 and set2 and intersction of set2 and set 3 but not in both intersctions
inter1_3 = inter1_2.symmetric_difference(inter2_3)
#set of all elements that are in only one of the three sets Set1, Set2 and Set3
inter = inter1_2.symmetric_difference(set3)
print('New set of all elements that are in only one of the three sets Set1, Set2 and Set3',inter)


union1 = set1.intersection(set2)
union2 = set2.intersection(set3)
union3 = set1.intersection(set3)
# new set of elements that are exactly two of the sets Set1, Set2 and Set3
print('New set of elements that are exactly two of the sets Set1, Set2 and Set3',(union1.union(union2)).union(union3))

# New set of all integers in the range 1 to 10 that are not in Set1
set4 = set()
for i in range (1,11):
    if i in set1 :
        continue
    else :
        set4.add(i)
print('New set of all integers in the range 1 to 10 that are not in Set1',set4)


# New set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3
set_123 = (set1.union(set2)).union(set3)
set5 = set()
for x in range (1,11):
    if x in set_123 :
        continue
    else :
        set5.add(x)
print('New set of all integers in the range 1 to 10 that are not in Set1 , Set2 , Set3',set5)
