import pandas as pd
import pdfkit

# Sample DataFrame (Replace this with your actual DataFrame)
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32],
        'City': ['New York', 'Paris', 'Berlin', 'London']}
df = pd.DataFrame(data)

# Additional data (could be text, lists, or any other HTML content)
additional_data = """
<h1>Report Summary</h1>
<p>This report contains the details of various individuals, including their name, age, and city of residence.</p>
<ul>
    <li><strong>Total Records:</strong> 4</li>
    <li><strong>Average Age:</strong> 29.75</li>
    <li><strong>Cities Covered:</strong> New York, Paris, Berlin, London</li>
</ul>
<hr>
<h2>Data Table</h2>
"""

# Convert the DataFrame to an HTML table
html_table = df.to_html(index=False)

# Combine the additional data with the DataFrame HTML
html_template = f"""
<html>
<head>
    <meta charset="utf-8">
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
        }}
        table, th, td {{
            border: 1px solid black;
            border-collapse: collapse;
            padding: 8px;
            text-align: left;
        }}
        th {{
            background-color: #f2f2f2;
        }}
        h1, h2 {{
            color: #333;
        }}
    </style>
</head>
<body>
    {additional_data}
    {html_table}
</body>
</html>
"""

# Save the combined HTML content to a file (optional)
with open("combined_report.html", "w") as file:
    file.write(html_template)

# Generate PDF using pdfkit
pdfkit.from_string(html_template, "combined_report.pdf")

print("PDF generated successfully.")
