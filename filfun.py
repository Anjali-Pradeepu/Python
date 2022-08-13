num_list=list(range(0,11))
def is_even(num):
    if num%2==0:
        return True
new=tuple(filter(is_even,num_list))
print(new)
