import frappe
from frappe.utils import nowdate, add_days
from frappe.utils.scheduler import schedule_job

def check_and_send_email():
    # Get all compliance master documents
    compliance_masters = frappe.get_all("Compliance Master", filters={"docstatus": 1})

    for compliance_master in compliance_masters:
        doc = frappe.get_doc("Compliance Master", compliance_master.name)
        # Check if it's time to send an email for this document
        if should_send_email(doc):
            # Send the email
            send_email(doc)

def should_send_email(doc):
    # Implement the logic to check if it's time to send an email for this document
    # This is a placeholder. You'll need to implement the actual logic based on your requirements.
    return True

def send_email(doc):
    # Implement the logic to send an email
    # This is a placeholder. You'll need to implement the actual logic based on your requirements.
    frappe.msgprint("Sending email...")

# Schedule the job to run daily
schedule_job(check_and_send_email, "00:00", repeat=True, repeat_every='1 day')


# in hooks
# scheduler_events = {
#     "daily": [
#         "your_app_name.compliance_master.check_and_send_email"
#     ]
# }
