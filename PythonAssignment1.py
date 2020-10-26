
#Numbers divislble by 7 but not 5 between 2000 and 3200
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        print(i,end=",")
        
#Reversing First and Last name
first=input()
last=input()
print(last[::-1]+' '+first[::-1])  



#volume of Sphere with Diameter 12cm
#for getting diameter fron user
#d=int(input())

d=12
print("{:.2f} cubic cm".format(4/3 * 3.14 * (d/2)**3))
