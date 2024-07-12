# Sales Report Automation

This project automates the process of generating a daily sales report from a spreadsheet and emailing it to the management team. The agent can handle user interactions to either send the report immediately or schedule it to be sent at a specified time.

## Features
- Extracts data from a sales spreadsheet.
- Generates a daily sales report in PDF format.
- Emails the report to the management team.
- Interacts with users to send or schedule the report.

## Project Structure
sales_report_automation/
│
├── data/
│ └── sales_data.xlsx
│
├── templates/
│ └── report_template.html
│
├── reports/
│
├── scripts/
│ ├── extract_data.py
│ ├── generate_report.py
│ ├── send_email.py
│ └── conversational_agent.py
│
└── main.py

## Dependencies

The following Python libraries are required:
- `pandas`
- `pdfkit`
- `jinja2`
- `openpyxl`

Additionally, `pdfkit` requires `wkhtmltopdf` to be installed on your system.

## Installation

### Step 1: Clone the Repository
```bash
git clone <your-repo-url>
cd sales_report_automation
Step 2: Install Python Libraries
bash
pip install pandas pdfkit jinja2 openpyxl
Step 3: Install wkhtmltopdf
On Ubuntu/Debian:
bash
sudo apt-get install wkhtmltopdf
On macOS using Homebrew:
brew install wkhtmltopdf
On Windows:
Download the installer from wkhtmltopdf downloads page.
Run the installer and follow the installation instructions.
Add the path to wkhtmltopdf.exe to your system's PATH environment variable.
Configuration
Email Server Settings
In main.py, update the smtp_config dictionary with your email server setting
smtp_config = {
    'server': 'smtp.example.com',
    'port': 587,
    'sender_email': 'your_email@example.com',
    'sender_password': 'your_password'
}
Recipient Emails
In main.py, update the recipient_emails list with the email addresses of the recipients:
recipient_emails = ['manager1@example.com', 'manager2@example.com']
Usage
Running the Script
Navigate to your project directory and run the main.py script:
python main.py
Interacting with the Agent
After running main.py, you can interact with the agent using the following commands:

Send the report immediately:
How can I assist you? send report
Schedule the report to be sent at a specific time (e.g., 9 PM):
How can I assist you? schedule report at 9PM
Exit the program:
How can I assist you? exit
