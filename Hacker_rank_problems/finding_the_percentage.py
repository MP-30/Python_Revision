dic = {'Malika':[52,56,60], 'Krishna':[ 67, 68, 69], 'Arjun': [70, 98, 63]}

for key,values in dic.items():
    if key == 'Malika':
        avg = round(sum(values)/len(values),2)
        new_avg = "{:.2f}".format(avg)
        print(new_avg)
        