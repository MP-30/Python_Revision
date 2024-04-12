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

    full_datas = [{'name': '2262456ea7',
                    'docstatus': 1,
                    'compliance_name': 'GSTR-1',
                    'frequency': 'Monthly',
                    'buffer_days': '18',
                    'selectday': 'Monday',
                    'lastdate_or_selectday': '1',
                    'half_year_sel': None,
                    'year_sel': None,
                    'next_due_date': None},
                    {'name': '24-04-0004',
                    'docstatus': 1,
                    'compliance_name': 'Test 5',
                    'frequency': 'Annually',
                    'buffer_days': '10',
                    'selectday': 'Monday',
                    'lastdate_or_selectday': '16',
                    'half_year_sel': 'Jan-June, July-Dec',
                    'year_sel': 'April-March',
                    'next_due_date': 'Will be calculate later automatically.'},
                    {'name': '337aa8d530',
                    'docstatus': 1,
                    'compliance_name': 'test 3',
                    'frequency': 'Weekly',
                    'buffer_days': '3',
                    'selectday': 'Wednesday',
                    'lastdate_or_selectday': '1',
                    'half_year_sel': 'Jan-June, July-Dec',
                    'year_sel': 'Jan-Dec',
                    'next_due_date': None},
                    {'name': '535cd90300',
                    'docstatus': 1,
                    'compliance_name': 'test 2',
                    'frequency': 'Quarterly',
                    'buffer_days': '9',
                    'selectday': 'Monday',
                    'lastdate_or_selectday': '16',
                    'half_year_sel': 'Jan-June, July-Dec',
                    'year_sel': 'Jan-Dec',
                    'next_due_date': None},
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
                    {'name': 'COM-24-04-0007',
                    'docstatus': 1,
                    'compliance_name': 'Test 7',
                    'frequency': 'Half Yearly',
                    'buffer_days': '12',
                    'selectday': 'Monday',
                    'lastdate_or_selectday': '7',
                    'half_year_sel': 'Jan-June, July-Dec',
                    'year_sel': 'Jan-Dec',
                    'next_due_date': 'Will be calculate later automatically.'},
                    {'name': 'COM-24-04-0008',
                    'docstatus': 1,
                    'compliance_name': 'Test 9',
                    'frequency': 'Quarterly',
                    'buffer_days': '18',
                    'selectday': 'Monday',
                    'lastdate_or_selectday': '22',
                    'half_year_sel': 'Jan-June, July-Dec',
                    'year_sel': 'Jan-Dec',
                    'next_due_date': 'Will be calculate later automatically.'},
                    {'name': 'COM-24-04-0009',
                    'docstatus': 1,
                    'compliance_name': 'Test 8',
                    'frequency': 'Quarterly',
                    'buffer_days': '10',
                    'selectday': 'Monday',
                    'lastdate_or_selectday': '8',
                    'half_year_sel': 'Jan-June, July-Dec',
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
    
    return {
        'month_data': month_data,
        'quater_data': quater_data,
        'half_data_jan': half_data_jan,
        'half_data_april': half_data_april,
        'annual_data_jan': annual_data_jan,
        'annual_data_april': annual_data_april
    }

    # print ('weeks_data is {a}'.format(a =weeks_data))
    # print('month_data is {}'.format(month_data))
    # print('quater_data is {}'.format(quater_data))
    # print('half_data_jan is {}'.format(half_data_jan))
    # print('half_data_april is {}'.format(half_data_april))
    # print('annual_data_jan is {}'.format(annual_data_jan))
    # print('annual_data_jan is {}'.format(annual_data_april))