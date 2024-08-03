def func_x(num):
    if num == 1:
        return a()
    elif num == 2:
        return b()
    elif num == 3:
        return c()
    elif num == 4:
        return d()
    elif num == 5:
        return e()
      
def func_x(is_chubby):
    if is_chubby is True:
        return a()
    elif is_chubby is False:
        return b()
def func_x(breeds, pet):
    for breed in breeds:
        if breed == pet:
            print("I have a dog.")
    else:
        print("I don't have a dog")


func_x(["chihuahua", "jack russell"], "chihuahua")
