=from scripts.conversational_agent import SalesReportAgent

smtp_config = {
    'server': 'smtp.example.com',
    'port': 587,
    'sender_email': 'your_email@example.com',
    'sender_password': 'your_password'
}

recipient_emails = ['manager1@example.com', 'manager2@example.com']

agent = SalesReportAgent(
    data_path='data/sales_data.xlsx',
    template_path='templates/report_template.html',
    output_path='reports/daily_sales_report.pdf',
    smtp_config=smtp_config,
    recipient_emails=recipient_emails
)

def main():
    while True:
        user_request = input("How can I assist you? ")
        agent.process_request(user_request)
        if 'exit' in user_request.lower().strip():
            break

if __name__ == "__main__":
    main()
