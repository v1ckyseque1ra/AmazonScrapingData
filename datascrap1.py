from bs4 import BeautifulSoup
import openpyxl

# Function to read HTML content from a file
def read_html_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Function to parse HTML content and extract product information
def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    products = []

    # Find all divs with class "sg-col-inner"
    divs = soup.find_all('div', class_='sg-col-inner')

    for div in divs:
        product_name = div.find('span', class_="a-size-medium a-color-base a-text-normal")
        product_price = div.find('span', class_="a-price")
        product_reviews = div.find('span', class_="a-icon-alt")
        previous_price = div.find('span', class_="a-price a-text-price puis-light-weight-text") 

        # Extract text content or set default values if not found
        name = product_name.text.strip() if product_name else " "
        price = product_price.text.strip() if product_price else " "
        reviews = product_reviews.text.strip() if product_reviews else " "
        earlierprice = previous_price.text.strip() if previous_price else " "

        products.append((name, price, reviews, earlierprice))

    return products

# Function to write data to Excel file
def write_to_excel(data, output_file):
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Write header
    sheet.append(['Product Name', 'Product Price', 'Product Reviews', 'Previous Price'])

    # Write data
    for row in data:
        sheet.append(row)

    # Save Excel file
    workbook.save(output_file)

# File path of the HTML file
html_file_path = r'amazon.html'

# Read HTML content from the file
html_content = read_html_from_file(html_file_path)

# Parse HTML and extract product information
product_data = parse_html(html_content)

# Specify the output Excel file
output_file = 'amazon_products1.xlsx'

# Write data to Excel file
write_to_excel(product_data, output_file)

print(f'Data has been written to {output_file}')
