names = {}

 

sumfeed = 0

for i in range (5) :

 

    name = input ("enter the name")

    feed = int(input("enter the feedback"))

    names[name]=feed

    sumfeed = sumfeed + feed 

 

avg_feed = sumfeed / len (names)

 

print (avg_feed)

 

 

print(names)