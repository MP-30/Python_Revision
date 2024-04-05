import frappe
from frappe.utils import nowdate, add_days
from frappe.utils.scheduler import schedule_job

class ComplianceEmail:
    def __init__(self, doc):
        self.doc = doc

    def schedule_emails(self):
        # Calculate start dates for rp_1, rp_2, and rp_3
        start_date_rp_1 = self.calculate_start_date(self.doc.buffer_days)
        start_date_rp_2 = self.calculate_start_date(int(self.doc.buffer_days * 0.5))
        start_date_rp_3 = self.calculate_start_date(int(self.doc.buffer_days * 0.2))

        # Schedule emails for rp_1, rp_2, and rp_3
        schedule_job(self.send_email, start_date_rp_1, repeat=True, repeat_every='1 day')
        schedule_job(self.send_email, start_date_rp_2, repeat=True, repeat_every='1 day')
        schedule_job(self.send_email, start_date_rp_3, repeat=True, repeat_every='1 day')

    def calculate_start_date(self, buffer_days):
        # Calculate the start date based on the buffer days
        # This is a simplified example. You'll need to adjust it based on your specific requirements.
        return add_days(nowdate(), buffer_days)

    def send_email(self):
        # Placeholder for the email sending logic
        frappe.msgprint("Sending email...")

# Hook into the Compliance Master doctype
def on_update(doc, method):
    if doc.doctype == "Compliance Master":
        compliance_email = ComplianceEmail(doc)
        compliance_email.schedule_emails()

# Add this function to your hooks.py file to ensure it's called on document update
