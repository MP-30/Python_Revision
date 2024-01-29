a = [{'owner': 'everest@moneybloom.in',
  'item_name': 'WIRING HARNESS FOR SLIC-432 & IC-510',
  'rate': 400.0,
  'amount': 400.0},
 {'owner': 'shrisai@moneybloom.in',
  'item_name': 'WIRING HARNESS FOR SLIC-432 & IC-510',
  'rate': 401.0,
  'amount': 401.0},
 {'owner': 'blackstone@moneybloom.in',
  'item_name': 'WIRING HARNESS FOR SLIC-432 & IC-510',
  'rate': 500.0,
  'amount': 500.0},
 {'owner': 'everest@moneybloom.in',
  'item_name': 'WIRING HARNESS FOR SLIC-432 & IC-510',
  'rate': 501.0,
  'amount': 501.0},
 {'owner': 'shrisai@moneybloom.in',
  'item_name': 'Copper pipe',
  'rate': 532.0,
  'amount': 532.0},
 {'owner': 'everest@moneybloom.in',
  'item_name': '456',
  'rate': 548.0,
  'amount': 548.0},
 {'owner': 'shrisai@moneybloom.in',
  'item_name': '456',
  'rate': 549.0,
  'amount': 549.0},
 {'owner': 'blackstone@moneybloom.in',
  'item_name': '456',
  'rate': 550.0,
  'amount': 550.0},
 {'owner': 'everest@moneybloom.in',
  'item_name': '456',
  'rate': 551.0,
  'amount': 551.0},
 {'owner': 'shrisai@moneybloom.in',
  'item_name': 'Copper pipe',
  'rate': 587.0,
  'amount': 587.0},
 {'owner': 'shrisai@moneybloom.in',
  'item_name': 'WIRING HARNESS FOR SLIC-432 & IC-510',
  'rate': 589.0,
  'amount': 589.0},
 {'owner': 'blackstone@moneybloom.in',
  'item_name': 'Copper pipe',
  'rate': 600.0,
  'amount': 600.0},
 {'owner': 'everest@moneybloom.in',
  'item_name': 'Copper pipe',
  'rate': 601.0,
  'amount': 601.0},
 {'owner': 'shrisai@moneybloom.in',
  'item_name': '456',
  'rate': 750.0,
  'amount': 750.0},
 {'owner': 'shrisai@moneybloom.in',
  'item_name': 'WIRING HARNESS FOR SLIC-432 & IC-510',
  'rate': 856.0,
  'amount': 856.0},
 {'owner': 'shrisai@moneybloom.in',
  'item_name': '456',
  'rate': 874.0,
  'amount': 874.0},
 {'owner': 'shrisai@moneybloom.in',
  'item_name': 'Copper pipe',
  'rate': 895.0,
  'amount': 895.0},
 {'owner': 'everest@moneybloom.in',
  'item_name': 'Copper pipe',
  'rate': 1500.0,
  'amount': 1500.0}]



session_user = 'everest@moneybloom.in'
user_item = {}
for i in a:
    if user_item.get(i['item_name'], None):
        if user_item[i['item_name']].get(i['owner'], None):
            user_item[i['item_name']][i['owner']] = min(user_item[i['item_name']][i['owner']], i['rate'])
        else:
            user_item[i['item_name']][i['owner']] = i['rate']
    else:
        user_item[i['item_name']] = {i['owner']: i['rate']}

print("i"+str(i))
print("user_item"+ str(user_item))
table = []
for item_key, users in user_item.items():
    sorted_users = sorted(users.items(), key=lambda kv: kv[1])
    rank = 1
    for ui in sorted_users:
        if ui[0] == session_user:
            table.append((item_key, ui[0], rank, ui[1]))
        else:
            rank += 1
    print("****")
    print(ui)            
print(table)