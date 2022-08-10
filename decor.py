#use of decorator function
def dec_function(in_function):
    def inner():
        print("#"*10)
        print("Decoration with flowers")
        in_function()
        print("#"*10)
    return inner

@dec_function
def old_function():
    print("No decoration")
old_function()


#######################
#another method without using decorators
def dec_function():
    def inner(in_function):
        print("#"*10)
        print("Decoration with flowers")
        in_function()
        print("#"*10)
    return inner

#@dec_function
def old_function():
    print("No decoration")
r_fun=dec_function()
r_fun(old_function)
