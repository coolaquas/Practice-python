# reading a file
months = open("Months_Demo.txt", "r+")
print("is", months.name, "readable? ", months.readable())
# print(months.read())
# print(months.readlines()[1])
for month in months.readlines():
    print(month)
months.close()

# # Append a file //Append where the curson in the file
# months = open("Months_Demo.txt", "a")
# months.write("Dec - December")
# months.close()

# # Modify a file //Completely remove and add. Or create a new file.
# months = open("Months_Demo1.txt", "w")
# months.write("Dec - December")
# months.close()

# # Demo for creating a html
# months = open("Demo.html", "w")
# months.write("<html><body><h1>Test</h1></body></html>")
# months.close()
