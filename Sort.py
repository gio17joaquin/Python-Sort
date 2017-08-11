def selection_sort(mylist):
   for slot in range(len(mylist)-1,0,-1):
       positionMax=0
       for location in range(1,slot+1):
           if mylist[location]>mylist[positionMax]:
               positionMax = location

       temp = mylist[slot]
       mylist[slot] = mylist[positionMax]
       mylist[positionMax] = temp

#Drill 1
mylist = [67, 45, 2, 13, 1, 998]
selection_sort(mylist)
print(mylist)

#Drill 2
mylist = [89, 23, 33, 45, 10, 12, 45, 45, 45]
selection_sort(mylist)
print(mylist)
