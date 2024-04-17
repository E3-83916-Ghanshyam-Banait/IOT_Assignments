"""
Write a program to accept a 4 digit number and
a. Display face value of each decimal digit
b. Display place value of each decimal digit
c. Display no in reverse order by changing decimal place values If user enters a 4 digit number 9361 output should be
a. 9 3 6 1
b. 9361 = 9 000 + 300 + 60 + 1
c. 1639 

"""
num= int(input("Enter a 4 digit number:"))
d=num%10
num=int (num/10)

c= num%10
num= int (num/10)

b= num%10
num= int(num/10)

a= num

print(a,b,c,d)
print(a*1000, b*100, c*10,d)
print(d,c,b,a)