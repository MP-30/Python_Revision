from datetime import date, datetime, timedelta
import frappe

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

    # Other methods remain the same...

    def calculate_email_start_dates(self, email_sending_month_list):
        today = datetime.today()
        for month in email_sending_month_list:
            due_date_obj = datetime(today.year, month, self.due_date)
            start_date_rp_1 = due_date_obj - timedelta(days=self.buffer_days)
            start_date_rp_2 = due_date_obj - timedelta(days=int(self.buffer_days * 0.5))
            start_date_rp_3 = due_date_obj - timedelta(days=int(self.buffer_days * 0.2))
            yield start_date_rp_1, start_date_rp_2, start_date_rp_3

    def schedule_emails(self, start_dates):
        for start_date_rp_1, start_date_rp_2, start_date_rp_3 in start_dates:
            # Schedule emails for rp_1, rp_2, and rp_3
            # This is a placeholder for scheduling logic in Frappe
            # You would replace this with actual Frappe scheduling logic
            print(f"Scheduling emails for rp_1 starting from {start_date_rp_1.strftime('%d-%m-%Y')}")
            print(f"Scheduling emails for rp_2 starting from {start_date_rp_2.strftime('%d-%m-%Y')}")
            print(f"Scheduling emails for rp_3 starting from {start_date_rp_3.strftime('%d-%m-%Y')}")

# Example usage
compliance_name = "Compliance Example"
frequency = "Half Yearly"
due_date = 5
half_year = "Jan-June, July-Dec"
buffer_days = 15

compliance_email_instance = ComplianceEmail(compliance_name, frequency, due_date, half_year, buffer_days)
email_sending_month_list = compliance_email_instance.make_list_of_dates()

for start_dates in compliance_email_instance.calculate_email_start_dates(email_sending_month_list):
    compliance_email_instance.schedule_emails(start_dates)
