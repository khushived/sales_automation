import pdfkit
from jinja2 import Environment, FileSystemLoader

def generate_report(data, template_path, output_path):
    try:
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template(template_path)
        html_out = template.render(data=data.to_dict(orient='records'))
        
        pdfkit.from_string(html_out, output_path)
        return True
    except Exception as e:
        print(f"Error generating the PDF report: {e}")
        return False
