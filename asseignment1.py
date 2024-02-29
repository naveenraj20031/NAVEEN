'''#eligible age for voting
age=25
if age>=18:
    print("eligible")
else:
    print("not eligible")
'''
'''#even or odd
a=5
if(a%2==0):
    print("even")
else:
    print("odd")
'''
'''#fine amount
days=17
if(days>=1 and days<=5):
    print("fine amount 5",days*5)
elif(days>=6 and days<=15):
    print("fine amount 10",days*10)
elif(days>=16 and days<=30):
    print("fine amount 15",days*15)
elif(days>30):
    print("membership cancel")
else:
   print("no fine")
   '''
#nested forabcd

for i in range(65,70):

    for j in range(65,i+1):
        print(chr(j),end="")
        
    print("")