def cube(num):
    return num*num*num


# num = input("Please enter a number. : ")
# result = cube(int(num))
result = cube(5)
print(result)


is_male = True
is_tall = True
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")

if is_male and is_tall:
    print("You are a tall male")
else:
    print("You are neither not male or not tall or both")

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif is_tall and not(is_male):
    print("You are a tall but not male")

else:
    print("You are neither not male or not tall or both")
