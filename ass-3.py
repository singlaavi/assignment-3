#SOLUTION 1
a=[]
#no. of inputs are not specified so we take 2 inputs
b=input('Enter first value:')
c=input('Enter the second value:')
a.append(b)
a.append(c)
print(a)

#SOLUTION 2
z=['google','apple','facebook','microsoft','tesla']
a.extend(z)
print(a)

#SOLUTION 3
#THE OBJECT IS NOT SPECIFIED TO BE COUNTED SO I TAKE GOOGLE THE OBJECT
cou=a.count('google')
print(cou)

#SOLUTION 4
list=[]
#lets take 5 inputs
list.append(int(input('Enter first no.:')))
list.append(int(input('Enter second no.:')))
list.append(int(input('Enter third no.:')))
list.append(int(input('Enter fourth no.:')))
list.append(int(input('Enter fifth no.:')))
list.sort()
print(list)


#SOLUTION 5
#WE NEED TWO LIST
#LETS TAKE LIST=B(FROM SOLUTION 4) & CAN MAKE A NEW LIST A
A=[]
#lets take 5 inputs
A.append(int(input('Enter first no.:')))
A.append(int(input('Enter second no.:')))
A.append(int(input('Enter third no.:')))
A.append(int(input('Enter fourth no.:')))
A.append(int(input('Enter fifth no.:')))
A.sort()
print(list)
print(A)
A.extend(list)
A.sort()
print(A)

#SOLUTION 6



#OPTIONAL QUESTION
#lets count even & odd no. from the list used in solution 5
even=0
odd=0
for i in A:
    if(i%2==0):
        even=even+1
    else:
        odd=odd+1
print('Even count =',even)
print('Odd count =',odd)
