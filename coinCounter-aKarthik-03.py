"""
Program : Coin Counter 
Author : Arun Karthik
Description : This program will produce a coin report once the user enters the string  
Revisions:
        00 - Annoucement of the program  
        01 - User will input the string  
        02 - Storing the coin value 
        03 - Printing the coin report 
"""

#Annoucement

print("Program which will count coins and calculate the values")

#User will input the string

coins = input("Enter a string:")

#The value of the coin is stored 
p=0
for i in coins:
    if(i=='p'): p+=1
n = 0
for i in coins:
    if (i=='n'): n+=1
d=0
for i in coins:
    if(i=='d'): d+=1
q=0
for i in coins:
    if(i=='q'): q+=1
h=0
for i in coins:
    if(i=='h'): h+=1

# Printing the result

print(40* '=')
print("\t\t Coin Counter Report")
print(40* '=')
print("Coin \t   Value   Number  Amount" )
print("==== \t   ====    =====  =====")
print("Pennies\t $0.01    ",p," \t  $",0.01*p)
print("Nickles\t $0.05    ",n," \t  $",0.05*n)
print("Dimes  \t $0.10    ",d," \t  $",0.10*d)
print("Pennies\t $0.25    ",q," \t  $",0.25*q)
print("Pennies\t $0.50    ",h," \t  $",0.50*h)
print(" \t \t Total Amount : $",(p*0.01)++ (0.05 * n) + (0.10 * d) + (0.25 * q) + (0.5 * h))
