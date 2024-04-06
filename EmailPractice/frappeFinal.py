from datetime import datetime, timedelta
import pytz
import math


def calculate_next_mail_date():
    # compliances = frappe.db.sql("""SELECT name FROM `tabCompliance Master` WHERE docstatus = 1""",as_dict=True);
    compliances = [{'name': '2262456ea7'},
                    {'name': '24-04-0004'},
                    {'name': '337aa8d530'},
                    {'name': '535cd90300'},
                    {'name': '7223186a17'},
                    {'name': '73ef40b9b1'},
                    {'name': 'COM-24-04-0005'},
                    {'name': 'ec41135e60'}]
    
    # full_data = a = frappe.db.sql("""SELECT name, docstatus, compliance_name, frequency, buffer_days, selectday, lastdate_or_selectday, half_year_sel, year_sel, next_due_date FROM `tabCompliance Master` WHERE docstatus = 1""",as_dict=True);

    full_datas = [
        {'name': '2262456ea7','docstatus': 1,'compliance_name': 'GSTR-1','frequency': 'Monthly','buffer_days': '18','selectday': 'Monday','lastdate_or_selectday': '1','half_year_sel': None,'year_sel': None,'next_due_date': None},
        {'name': '24-04-0004','docstatus': 1,'compliance_name': 'Test 5','frequency': 'Annually','buffer_days': '10','selectday': 'Monday','lastdate_or_selectday': '16',               'half_year_sel': 'Jan-June, July-Dec','year_sel': 'April-March','next_due_date': 'Will be calculate later automatically.'},
        {'name': '337aa8d530','docstatus': 1,'compliance_name': 'test 3','frequency': 'Weekly','buffer_days': '3','selectday': 'Wednesday','lastdate_or_selectday': '1',                   'half_year_sel': 'Jan-June, July-Dec','year_sel': 'Jan-Dec','next_due_date': None},
        {'name': '535cd90300','docstatus': 1,'compliance_name': 'test 2','frequency': 'Quarterly','buffer_days': '9','selectday': 'Monday','lastdate_or_selectday': '16',
        'half_year_sel': 'Jan-June, July-Dec','year_sel': 'Jan-Dec','next_due_date': None},
                    {'name': '7223186a17',
                    'docstatus': 1,
                    'compliance_name': 'Test 5',
                    'frequency': 'Annually',
                    'buffer_days': '8',
                    'selectday': 'Monday',
                    'lastdate_or_selectday': '14',
                    'half_year_sel': 'Jan-June, July-Dec',
                    'year_sel': 'Jan-Dec',
                    'next_due_date': None},
                    {'name': '73ef40b9b1',
                    'docstatus': 1,
                    'compliance_name': 'test 4',
                    'frequency': 'Half Yearly',
                    'buffer_days': '12',
                    'selectday': 'Monday',
                    'lastdate_or_selectday': '23',
                    'half_year_sel': 'April-Sep, Oct-March',
                    'year_sel': 'Jan-Dec',
                    'next_due_date': None},
                    {'name': 'COM-24-04-0005',
                    'docstatus': 1,
                    'compliance_name': 'Test 6',
                    'frequency': 'Half Yearly',
                    'buffer_days': '8',
                    'selectday': 'Monday',
                    'lastdate_or_selectday': '20',
                    'half_year_sel': 'April-Sep, Oct-March',
                    'year_sel': 'Jan-Dec',
                    'next_due_date': 'Will be calculate later automatically.'},
                    {'name': 'ec41135e60',
                    'docstatus': 1,
                    'compliance_name': 'gdfgdfgsdfgdf',
                    'frequency': 'Monthly',
                    'buffer_days': '5',
                    'selectday': 'Monday',
                    'lastdate_or_selectday': '8',
                    'half_year_sel': 'Jan-June',
                    'year_sel': 'Jan-Dec',
                    'next_due_date': None}]
    
    # week_data = [week for week in full_datas if week['frequency'] == 'Weekly']
    weeks_data = filtered_data = [{key: d[key] for key in ('name', 'compliance_name', 'buffer_days', 'selectday')} for d in full_datas if d['frequency'] == 'Weekly']
    
    month_data = [{key: d[key] for key in ('name', 'compliance_name', 'buffer_days','lastdate_or_selectday')} for d in full_datas if d['frequency'] == 'Monthly']
    
    quater_data = [{key: d[key] for key in ('name', 'compliance_name', 'buffer_days','lastdate_or_selectday')} for d in full_datas if d['frequency'] == 'Quarterly']
    
    half_data_jan = [{key: d[key] for key in ('name', 'compliance_name', 'buffer_days','lastdate_or_selectday')} for d in full_datas if d['frequency'] == 'Half Yearly' and d['half_year_sel'] == 'Jan-June, July-Dec']
    
    half_data_april = [{key: d[key] for key in ('name', 'compliance_name', 'buffer_days','lastdate_or_selectday')} for d in full_datas if d['frequency'] == 'Half Yearly' and d['half_year_sel'] == 'April-Sep, Oct-March']
    
    annual_data_jan = [{key: d[key] for key in ('name', 'compliance_name', 'buffer_days','lastdate_or_selectday')} for d in full_datas if d['frequency'] == 'Annually' and d['year_sel'] == 'Jan-Dec']
    
    annual_data_april = [{key: d[key] for key in ('name', 'compliance_name', 'buffer_days','lastdate_or_selectday')} for d in full_datas if d['frequency'] == 'Annually' and d['year_sel'] == 'April-March']
    
    return month_data
    # print ('weeks_data is {a}'.format(a =weeks_data))
    # print('month_data is {}'.format(month_data))
    # print('quater_data is {}'.format(quater_data))
    # print('half_data_jan is {}'.format(half_data_jan))
    # print('half_data_april is {}'.format(half_data_april))
    # print('annual_data_jan is {}'.format(annual_data_jan))
    # print('annual_data_jan is {}'.format(annual_data_april))
    
def next_date_for_month(data):
    # Get the IST timezone
    IST = pytz.timezone('Asia/Kolkata')
    today = datetime.now(IST).date()
    datetime_ist = datetime.now(IST)

    current_month = datetime_ist.month
    current_date = datetime_ist.day
    current_day = datetime_ist.strftime("%A")
    current_year = datetime_ist.year 
    
    
    
    
    
# fun_calculate_next_mail_date_data = calculate_next_mail_date()
# print(last_data_for_month(fun_calculate_next_mail_date_data))
 

IST = pytz.timezone('Asia/Kolkata')
today = datetime.now(IST).date()
datetime_ist = datetime.now(IST)

current_month = datetime_ist.month
current_date = datetime_ist.day
current_day = datetime_ist.strftime("%A")
current_year = datetime_ist.year

today_datetime = datetime.combine(today, datetime.min.time(), tzinfo=IST)

month_data = [
    {'name': '2262456ea7', 'compliance_name': 'GSTR-1', 'buffer_days': '18', 'lastdate_or_selectday': '1'},
    {'name': 'ec41135e60', 'compliance_name': 'gdfgdfgsdfgdf', 'buffer_days': '5', 'lastdate_or_selectday': '8'}
]

# Initialize an empty list to store the results
results = []

# Iterate through each item in month_data
for item in month_data:
    item_results = {} # Initialize an empty list for this item
    last_date_or_selectday = int(item['lastdate_or_selectday'])
    buffer_days = int(item['buffer_days'])
    
    # Calculate the email sending date for each month of the current year
    for month in range(1, 13): # Loop through all months
        due_date = datetime(today.year, month, last_date_or_selectday, tzinfo=IST)
        
        if due_date > today_datetime: # Compare with today_datetime instead of today
            email_sending_date = due_date - timedelta(days=buffer_days)
            buffer_days_rp_2 = (0.5 * buffer_days)
            rounded_buffer_days_rp_2 = math.ceil(buffer_days_rp_2)
            email_sending_date_rp_2 = due_date - timedelta(days=rounded_buffer_days_rp_2)
            buffer_days_rp_3 = (0.2 * buffer_days)
            rounded_buffer_days_rp_3 = math.ceil(buffer_days_rp_3)
            email_sending_date_rp_3 = due_date - timedelta(days=rounded_buffer_days_rp_3)
            '''
            # Store the results for this item in a nested list
            item_results.append([
                f"For rp_1 {item['name']} - Due Date: {due_date.strftime('%Y-%m-%d')} - Email Sending Date: {email_sending_date.strftime('%Y-%m-%d')}",
                f"For rp_2 {item['name']} - Due Date: {due_date.strftime('%Y-%m-%d')} - Email Sending Date: {email_sending_date_rp_2.strftime('%Y-%m-%d')}",
                f"For rp_3 {item['name']} - Due Date: {due_date.strftime('%Y-%m-%d')} - Email Sending Date: {email_sending_date_rp_3.strftime('%Y-%m-%d')}"
            ])
            '''
             # Store the next relevant date for each RP if it's greater than today
            if email_sending_date > today_datetime and 'rp_1' not in item_results:
                item_results['rp_1'] = email_sending_date.strftime('%Y-%m-%d')
            if email_sending_date_rp_2 > today_datetime and 'rp_2' not in item_results:
                item_results['rp_2'] = email_sending_date_rp_2.strftime('%Y-%m-%d')
            if email_sending_date_rp_3 > today_datetime and 'rp_3' not in item_results:
                item_results['rp_3'] = email_sending_date_rp_3.strftime('%Y-%m-%d')
            
    # Add the item's results to the overall results list
    results.append({item['name']:item_results})
'''
# Print the results
for item_results in results:
    for rp_result in item_results:
        print(rp_result)
    print('*************')
print('++++++++++++++++++++++++++')
'''
Schedule_dates = []
for item_result in results:
    for item_name, rp_dates in item_result.items():
        Schedule_dates.append({item_name: rp_dates})
print(Schedule_dates)

# print(rounded_buffer_days_rp_2)