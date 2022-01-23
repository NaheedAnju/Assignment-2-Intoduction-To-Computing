#Question 1
#String operations
print('-------------------------Question 1-------------------------')

str = 'Python is a case sensitive language'
length = len(str)
print('Length of string = ',length)

str_rev = str[::-1]
print('Reverse string : ',str_rev)

str_slice = str[10:26:1]
print(str_slice)

str_replace = str.replace('a case sensitive','object oriented')
print(str_replace)

print('Index of a ', str.index('a'))

new_str = str.replace(' ','')
print(new_str)

#Question 2
#String Formating
print('-------------------------Question 2-------------------------')

Name = input('Enter your name - ')
sid = input('Enter your SID - ')
Department = input('Enter your Department - ')
CGPA = float(input('Enter your CGPA - '))
print('Hey ', Name ," here!")
print('My SID is ', sid )
print('I am from ', Department , ' department and my CGPA is ', CGPA)


#Question 3
#Bitwise operators
print('-------------------------Question 3-------------------------')
a = 56
b = 10
print('a&b= ',a&b)
print('a|b =',a|b)
print('a^b =',a^b)
print('Left shift of a with 2 bits = ',a<<2)
print('Left shift of b with 2 bits = ',b<<2)
print('Right shift of a with 2 bits = ',a>>2)
print('Right shift of b with 4 bits = ',b>>4)

#Question 4
#To find Greatest of three numbers
print('-------------------------Question 4-------------------------')

num1 = int(input('Enter 1st Number - '))
num2 = int(input('Enter 2nd Number - '))
num3 = int(input('Enter 3rd Number - '))
if num1>num2 :
    if num1>num3 :
        print(num1, 'is greatest number')
    else :
        print(num3 ,'is greatest number')
else :
    if num2>num3 :
        print(num2, 'is greatest number')
    else :
        print(num3 ,'is greatest number')

#Question 5
print('-------------------------Question 5-------------------------')

str1 = input("Enter a string - ")
if 'name' in str1:
    print("Yes")
else :
    print("No")

#Question 6
#Triangle Test
print('-------------------------Question 6-------------------------')

side1 = int(input('Enter length of 1st side - '))
side2 = int(input('Enter length of 2nd side - '))
side3 = int(input('Enter length of 3rd side - '))
if side1 + side2 < side3:
    print('No')
elif side3 + side2 < side1:
    print('No')
elif side1 + side3 < side2:
    print('No')
else :
    print('Yes')

