from datetime import date, datetime, timedelta
import sched
import time

class ComplianceEmail:
    def __init__(self, compliance_name, frequency, due_date=None, half_year=None, buffer_days=None):
        self.compliance_name = compliance_name
        self.frequency = frequency
        self.due_date = due_date
        self.half_year = half_year
        self.buffer_days = buffer_days
        self.today_date = date.today()
        self.day = self.today_date.day
        self.month = self.today_date.month
        self.year = self.today_date.year

    def make_list_of_dates(self):
        match self.frequency:
            case 'Weekly':
                return self.weekly()
            case 'Monthly':
                return self.monthly()
            case 'Quarterly':
                return self.quarterly()
            case 'Half Yearly':
                if self.half_year == 'Jan-June, July-Dec':
                    return self.half_yearly_jan_june_july_dec()
                elif self.half_year == 'April-Sep, Oct-March':
                    return self.half_yearly_april_sep_oct_march()
            case 'Annually':
                return self.annually()
            case _:
                print("Invalid frequency selected.")
                return []


    def weekly(self):
        print("Weekly frequency selected.")
        # Implement logic for weekly frequency
        pass

    def monthly(self):
        print("Monthly frequency selected.")
        email_sending_month_list = [1,2,3,4,5,6,7,8,9,10,11,12]
        return email_sending_month_list

    def quarterly(self):
        print("Quarterly frequency selected.")
        email_sending_month_list = [3,6,9,12]
        return email_sending_month_list

    def half_yearly(self):
        print("Half Yearly selected.")
        if self.half_year == 'Jan-June, July-Dec':
            email_sending_month_list = [6,12]
        elif self.half_year == 'April-Sep, Oct-March':
            email_sending_month_list = [9,3]
        return email_sending_month_list

    def annually(self):
        print("Annually frequency selected.")
        email_sending_month_list = [3,12]
        return email_sending_month_list

    def calculate_email_start_date(self, email_sending_month_list):
        today = datetime.today()
        for month in email_sending_month_list:
            due_date_obj = datetime(today.year, month, self.due_date)
            start_date = due_date_obj - timedelta(days=self.buffer_days)
            yield start_date

    def generate_email_dates(self, start_date, email_sending_month):
        email_dates = []
        current_date = start_date
        while current_date.month == email_sending_month:
            email_dates.append(current_date)
            current_date += timedelta(days=1)
        return email_dates

    def schedule_emails(self, email_dates):
        scheduler = sched.scheduler(time.time, time.sleep)
        for email_date in email_dates:
            scheduler.enterabs(time.mktime(email_date.timetuple()), 1, self.send_email, argument=(email_date,))
        scheduler.run()

    def send_email(self, email_date):
        print(f"Sending email on {email_date.strftime('%d-%m-%Y')}")

# Example usage
compliance_name = "Compliance Example"
frequency = "Half Yearly"
due_date = 5
half_year = "Jan-June, July-Dec"
buffer_days = 15

compliance_email_instance = ComplianceEmail(compliance_name, frequency, due_date, half_year, buffer_days)
email_sending_month_list = compliance_email_instance.make_list_of_dates()

for start_date in compliance_email_instance.calculate_email_start_date(email_sending_month_list):
    email_dates = compliance_email_instance.generate_email_dates(start_date, start_date.month)
    compliance_email_instance.schedule_emails(email_dates)
