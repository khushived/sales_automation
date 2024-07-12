import datetime
import time
from threading import Timer
from scripts.extract_data import extract_data
from scripts.generate_report import generate_report
from scripts.send_email import send_email

class SalesReportAgent:
    def __init__(self, data_path, template_path, output_path, smtp_config, recipient_emails):
        self.data_path = data_path
        self.template_path = template_path
        self.output_path = output_path
        self.smtp_config = smtp_config
        self.recipient_emails = recipient_emails

    def process_request(self, request):
        if 'send report' in request:
            self.send_report()
        elif 'schedule report' in request:
            self.schedule_report(request)
        else:
            print("Sorry, I didn't understand your request.")

    def send_report(self):
        data = extract_data(self.data_path)
        if data is not None:
            if generate_report(data, self.template_path, self.output_path):
                if send_email(
                    self.smtp_config['server'], 
                    self.smtp_config['port'], 
                    self.smtp_config['sender_email'], 
                    self.smtp_config['sender_password'], 
                    self.recipient_emails, 
                    "Daily Sales Report", 
                    "Please find the attached daily sales report.", 
                    self.output_path
                ):
                    print("Report sent successfully.")
                else:
                    print("Failed to send the report.")
            else:
                print("Failed to generate the report.")
        else:
            print("Failed to extract data from the spreadsheet.")

    def schedule_report(self, request):
        time_info = request.split('at')[-1].strip()
        try:
            schedule_time = datetime.datetime.strptime(time_info, '%I%p')
            now = datetime.datetime.now()
            delay = (schedule_time - now).total_seconds()
            Timer(delay, self.send_report).start()
            print(f"Report scheduled to be sent at {schedule_time}.")
        except Exception as e:
            print(f"Error scheduling the report: {e}")
