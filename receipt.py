from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
from random import randint
import os
""" note - before running this code make sure to install reportlab
        to install it 
            open cmd  and write "pip install report lab" 
            for any other query about pip visit (https://pip.pypa.io/en/stable/)"""

def create_receipt(transaction_id, amount, date, customer_name, items):
    # Get the path to the user's Downloads folder
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    
    # Defining the file name and full path
    file_name = f"receipt_{transaction_id}.pdf"
    file_path = os.path.join(downloads_folder, file_name)
    
    # Creating the canvas object
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 20)
    c.drawString(200, height - 50, "Payment Receipt")

    c.setFont("Helvetica", 12)
    c.drawString(450, height - 80, f"Date: {date}")

    c.drawString(50, height - 120, f"Transaction ID: {transaction_id}")
    c.drawString(50, height - 140, f"Customer Name: {customer_name}")

    c.drawString(50, height - 180, "Item")
    c.drawString(300, height - 180, "Price")

    y = height - 200
    for item, price in items:
        c.drawString(50, y, item)
        c.drawString(300, y, f"${price:.2f}")
        y -= 20

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y - 20, f"Total Amount: ${amount:.2f}")

    # Footer
    c.setFont("Helvetica", 10)
    c.drawString(50, 50, "Thank you for your purchase!")

    # Save the PDF
    c.save()
    print(f"Receipt saved as {file_path}")

def generate_random_number():
    return randint(100000, 999999)

transaction_id = generate_random_number()
amount = 250.75
date = datetime.now().strftime("%Y-%m-%d")
customer_name = input("Enter your name (ex John Doe): ")
items = [("Item 1", 100.00), ("Item 2", 50.00), ("Item 3", 100.75)]

create_receipt(transaction_id, amount, date, customer_name, items)
