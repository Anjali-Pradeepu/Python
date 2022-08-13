#i/p as list of elements return a dictionary which will contain key as number
# and value is number of occurences that key ie number....

num_list=list(input("Enter the list elements"))
print(num_list)
def num_count(num_list):
    dict_count={}
    for i in num_list:
        dict_count[i]=dict_count.get(1,0)+1
    return dict_count
final_count=num_count(num_list)
print(final_count)


#####

