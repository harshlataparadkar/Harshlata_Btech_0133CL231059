f = open("report.txt","w")
f.write("Name : Rahul , Marks : 58")
f.write("Name : Khushi , Marks : 75")
f.write("Name : Harshita , Marks : 60")
f.write("Name : Harsha , Marks : 59")
f.write("Name : Reena , Marks : 78")

f.close()
print("file created")

f = open("report.txt","r")
const = f.read()
if Marks > 75:
    print(const)


f.close()

