from functools import reduce
num_list=list(range(0,11))
total=reduce(lambda x,y:x+y,num_list)
print(total)
