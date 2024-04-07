from datetime import datetime, timedelta
import pytz
import math


def next_date_for_quater():
    # Get the IST timezone
    IST = pytz.timezone('Asia/Kolkata')
    today = datetime.now(IST).date()
    datetime_ist = datetime.now(IST)

    current_month = datetime_ist.month
    current_date = datetime_ist.day
    current_day = datetime_ist.strftime("%A")
    current_year = datetime_ist.year 
    
    today_datetime = datetime.combine(today, datetime.min.time(), tzinfo=IST)
    
    data = calculate_next_mail_date()
    quater_data = data['quater_data']

    
    # Initialize an empty list to store the results
    results = []    
    for item in quater_data:
        item_results = {} # Initialize an empty list for this item
        last_date_or_selectday = int(item['lastdate_or_selectday'])
        buffer_days = int(item['buffer_days'])
        
        # Calculate the email sending date for each quater of the current year
        for month in (3,6,9, 12): # Loop through all quater
            due_date = datetime(today.year, month, last_date_or_selectday, tzinfo=IST)
            print(due_date)
            
            if due_date > today_datetime: # Compare with today_datetime instead of today
                email_sending_date = due_date - timedelta(days=buffer_days)
                # print("email_sending_date" + str(email_sending_date))
                buffer_days_rp_2 = (0.5 * buffer_days)
                rounded_buffer_days_rp_2 = math.ceil(buffer_days_rp_2)
                email_sending_date_rp_2 = due_date - timedelta(days=rounded_buffer_days_rp_2)
                # print('buffer_days_rp_2' + str(email_sending_date_rp_2))
                buffer_days_rp_3 = (0.2 * buffer_days)
                rounded_buffer_days_rp_3 = math.ceil(buffer_days_rp_3)
                email_sending_date_rp_3 = due_date - timedelta(days=rounded_buffer_days_rp_3)
                # print("buffer_days_rp_3" + str(email_sending_date_rp_3))
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
    Schedule_dates_quater = []
    for item_result in results:
        for item_name, rp_dates in item_result.items():
            Schedule_dates_quater.append({item_name: rp_dates})
    print("Quater")
    print(Schedule_dates_quater)  
next_date_for_quater()
