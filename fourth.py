lucky_number = [1, 2, 3, 4, 5, 6, 7]
friends = ["Deba", "Pritam", "hehe", "Suman", "Soumen", "hehe"]
print(friends[1:])
print(friends[1:4])
friends.extend(lucky_number)
print(friends)
friends.append("teet")
print(friends)
friends.insert(1, "popo")
print(friends)
friends.remove(5)
print(friends)
print(friends.index("teet"))
lucky_number.reverse()
friends.extend(lucky_number)
print(friends.count("hehe"))
lucky_number.sort()
print(friends)
friends.pop()
print(friends)
friends.clear()
print(friends)