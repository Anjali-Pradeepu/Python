def print_msg():
    def wish_msg(msg):
        print("Your message is ",msg)
    return wish_msg
return_value=print_msg()
print(return_value)
print(type(print_msg))
return_value("hi how are you")
