'''
file = open('youtube.txt', 'w')
try:
    file.write('Aditya Bhadauriya.')
finally:
    file.close()
'''
 
with open('youtube.txt', 'w') as file:
    file.write('Aditya Singh') 
