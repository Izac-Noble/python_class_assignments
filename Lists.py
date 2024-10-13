list_name = [87.0,89.9,34.0,100.0]
list_name[3] = 99.0
inventory =["staff","hat","bread","shoes","Potion"]
movie = ["The Holy Grail", 1975,9.99]
test_scores =[]

inventory.pop() #removes objects from the list.
#inventory.remove("shoes")
#inventory.index("shoes") #gives you the index of the item in the list.
#inventory.insert(3,"robe")
#inv1 = inventory[-1]

#print(inv1)
#print(list_name)
#print(inventory)
#print(movie)

scores = [70,80,90,100]
total = 0
i= 0
while i < len(scores):
    total += scores[i]
    i += 1
for score in scores:
    total += score


#len(scores)
#print(len(scores))
#print(total)

#students = [["Joel",85,95,70],["Anne", 95, 100,100],["Mike",77,70,85] ] #three items in the list
#print(students[1][0]) #to pull up a specific piece of information form the list


numlist = [5,15,84,3,14,2,8,10,14,25,14]
#numlist.sort() # sorts them inorder careful though it can change your data
#count = numlist.count(14) # counts the number of values in the list.
#print(numlist)
#maximum = max(numlist) #getting the maximum
#minimum = min(numlist) #getting the minimum
#print(maximum)
#print(minimum)

import random
#choice = random.choice(numlist)
#print(choice)

#random.shuffle(numlist)
#print(numlist)


#foodlist = ["apple","Pear","orange","banana"]
#foodlist.sort(key=str.lower)
#print(foodlist)
#foodlist_sorted = sorted(foodlist)

#list_one = [1,2,3,4,5]
#list_two = [1,2,3,4,5]
#list_two[1]=4
#print(list_two)

#import copy
#list_two= copy.deepcopy(list_one)
#print(list_one)

#numbers = [52,54,56,58,60,62]
#numbers[0:2]
#numbers[:2]
#numbers[4:]
#numbers[0:4:2]
#print(numbers)

#adding stuff to a list
inventory = ["staff","robe"]
chest = ["scroll","pestle"]
inventory += chest
print(inventory)