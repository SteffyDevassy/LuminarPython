#Binary Search in list
lst=[21,20,18,22,7,2,25]
lst.sort()
low=0
upp=len(lst)-1
flag=0
ele=int(input("Enter element to be searched"))
while(low<=upp):
    mid=(low+upp)//2
    if(ele>lst[mid]):
        low=mid+1
    elif(ele<lst[mid]):
        upp=mid-1
    elif(ele==lst[mid]):
        flag+=1
        break
if(flag==0):
    print("Element  not found")
else:
    print("Element found")

#[10,20,30,40,50,60,70]
# l          m        u
#ele=60

#case1 if(ele>lst(mid):60>40:
#low=mid+1

#case2  elif(ele<lst(mid))  :
#upp=mid-1

#case3 :elif(ele==lst(mid)
#ele found
