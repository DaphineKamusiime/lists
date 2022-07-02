'''names=["tim","jim","trey","sam"]
del names[1]
names.append(input('add a name'))
names.sort()
print(names)

sport=["soccer","chess"]
sport.append(input('enter your favourite sport'))
print(sport)


subjects=['maths','physics','literature','chemistry','biology','economics']
print(subjects)
dislike=str(input('which of the subjects do you dislike'))
getrid=subjects.index(dislike)
del subjects[getrid]
print(subjects)


colour=['red','blue','yellow','green','purple','violet','indigo','white','black','grey']
num1=int(input('enter a number between 0 and 4'))
num2=int(input('enter a number between 5 and 9'))
print(colour[num1],colour[num2])


numb=[345,786,559]
for i in numb:
    print(i)
num=int(input('enter a three digit number '))
if num in numb:
    print('number is in list')
else:
    print('not in list')

from itertools import count


name1=input('enter names of the people you want to invite')
name2=input('enter names of the people you want to invite')
name3=input('enter names of the people you want to invite')
name=[name1,name2,name3]
choice=input('do you want to add anyone else')
if choice=='yes':
    name4=input('enter names of the people you want to invite')
else:
    print(name)

print('you have invited ',len(name), 'people')
print(name)
namme=input('enter a name in the list')
print(namme.index)


from turtle import position

shows=['spongebob','winx','icarly']
for i in shows:
    print(i)
print()
show=input('enter a show')
position=int(input('enter position you want to olacev it between 0 and 3'))
shows.insert(position,show)
for i in shows:
    print(i)

'''
nums=[]
count=0
while count<3:
    num=int(input('enter  number'))
    nums.append(num)
    print(nums)
    count=count+1
lastnum=int(input('do you want to save the last number y/n'))
if lastnum=="n":
    nums.remove(num)
print(nums)

 
    