try:
    def add(n1,n2):
        print(n1 + n2)
    
        add(5,9)

    number1 = 10
    number2 = input("Please enter a value: ")
    a = add(number1, number2)
except:
    print("Hey it looks like you aren't adding correctly!")
else:
    print("Add went well")
    print(a)

print("==============")

try:
    f = open('testfile', 'r')
    f.write("Write a test line")
    print("No error")
except TypeError:
    print("There was a type error!")
except OSError:
    print("Hey you have an OS error") 
finally:
    print("I always run")
    
print("==============")

def ask_for_int():
    while True:
        try: 
            result = int(input("Please provide number: "))
        except:
            print("Whoops! That is not a number")
            # continue
        else:
            print("Yes thank you")
            break
        finally:
            print("End of try/except/finnaly")
            print("I will always run at the end")
ask_for_int()