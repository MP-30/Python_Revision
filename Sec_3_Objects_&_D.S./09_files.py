myfile = open('09_1myfile.txt')
print(myfile.read())
myfile.seek(0)
print(myfile.read())
myfile.seek(0)
print(myfile.readlines())
myfileLocal = open('/home/aditya/myFile.txt')
print(myfileLocal.read())
myfileLocal1 = open('/home/aditya/myFile.txt')
print(myfileLocal1.read()) 
with open('09_1myfile.txt') as my_new_file:
  content = my_new_file.read()
print(content)

with open('09_1myfile.txt', mode='r') as my_new_file:
  content1 = my_new_file.read()
print(content1)

with open('09_1myfile.txt', mode='a') as my_new_file:
  content2 = my_new_file.write('appended text')

with open('09_1myfile.txt', mode='r') as my_new_file:
  content2 = my_new_file.read()
print(content2)

with open('demo.txt', mode='w') as my_new_file:
  content2 = my_new_file.write('I created this file')

with open('demo.txt', mode='r') as my_new_file:
  content2 = my_new_file.read()
print(content2)
