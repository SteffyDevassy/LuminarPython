students=[
    [100,"arun","bca",145],
    [101,"arjun","bca",125],
    [102,"varun","mca",150],
    [103,"tinu","bcom",140],
    [104,"jeena","bcom",120],

]

#print student names
for student in students:
    print((student[1]))


#print totalof all students
total=0
for student in students:
    total=total+student[3]
    print(total)

#print details of student whose course is mca
for student in students:
    if student[2]=="mca":
        print((student))

#no. of students in bca,mca,bcom
mtotal=bcatot=bcomtot=0
for student in students:
    if student[2]=="mca":
        mtotal+=1
    elif student[2]=="bca":
        bcatot+=1
    elif student[2]=="bcom":
        bcomtot+=1
print("no. of students in mca",mtotal)
print("no. of students in bca",bcatot)
print("no. of students in bcom",bcomtot)

#highest total
print("MAx total")
# for student in students:
# m=[max(student) for student in students]
# print(m)
m=max(students,key=lambda x: x[3])
print(m[3])