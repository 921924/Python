#range(stop), range(start, stop), range(start, stop, stop)
#list is mutable, dynamic.
list_ = [1,'hi',[3,["bye", 5],6],7]
print(list_[2][1][0][1])
print(1,2,3,4,sep='--')
print(5,6,7,8)
for ele in list_:
   print(ele)
for i in range(len(list_)):
    print(list_[i])