import os
import re

# Read index.html to extract the source header and footer
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract header (including mobile menu)
header_match = re.search(r'(<header.*?</header>)', index_content, re.DOTALL)
if not header_match:
    print("Could not find header in index.html")
    exit(1)
source_header = header_match.group(1)

# Extract footer
footer_match = re.search(r'(<footer.*?</footer>)', index_content, re.DOTALL)
if not footer_match:
    print("Could not find footer in index.html")
    exit(1)
source_footer = footer_match.group(1)

# List of all html files
html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html']

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace header
    content = re.sub(r'<header.*?</header>', source_header, content, flags=re.DOTALL)
    
    # Replace footer (some files might not have a footer, so only replace if it exists)
    if '<footer' in content:
        content = re.sub(r'<footer.*?</footer>', source_footer, content, flags=re.DOTALL)
    else:
        # If no footer, insert it before </body>
        content = content.replace('</body>', f'{source_footer}\n</body>')

    # Now, fix the "active" states in the newly pasted header
    # Remove active class from Home
    content = content.replace('class="nav-link text-gray-900 dark:text-gray-100 py-2 active"', 'class="nav-link text-gray-900 dark:text-gray-100 py-2"')
    content = content.replace('class="block px-3 py-3 rounded-md text-base font-semibold text-brandRed bg-brandRed/10"', 'class="block px-3 py-3 rounded-md text-base font-medium text-gray-900 dark:text-gray-100 hover:bg-gray-50 dark:hover:bg-gray-800"')
    
    # Add active class to current file
    if filename == 'home-2.html':
        content = content.replace('<a href="home-2.html" class="nav-link text-gray-900 dark:text-gray-100 py-2">Home 2</a>', '<a href="home-2.html" class="nav-link text-gray-900 dark:text-gray-100 py-2 active">Home 2</a>')
        content = content.replace('<a href="home-2.html" class="block px-3 py-3 rounded-md text-base font-medium text-gray-900 dark:text-gray-100 hover:bg-gray-50 dark:hover:bg-gray-800">Home 2</a>', '<a href="home-2.html" class="block px-3 py-3 rounded-md text-base font-semibold text-brandRed bg-brandRed/10">Home 2</a>')
    elif filename == 'about.html':
        content = content.replace('<a href="about.html" class="nav-link text-gray-900 dark:text-gray-100 py-2">About</a>', '<a href="about.html" class="nav-link text-gray-900 dark:text-gray-100 py-2 active">About</a>')
        content = content.replace('<a href="about.html" class="block px-3 py-3 rounded-md text-base font-medium text-gray-900 dark:text-gray-100 hover:bg-gray-50 dark:hover:bg-gray-800">About</a>', '<a href="about.html" class="block px-3 py-3 rounded-md text-base font-semibold text-brandRed bg-brandRed/10">About</a>')
    elif filename == 'products.html':
        content = content.replace('<a href="products.html" class="nav-link text-gray-900 dark:text-gray-100 py-2">Products</a>', '<a href="products.html" class="nav-link text-gray-900 dark:text-gray-100 py-2 active">Products</a>')
        content = content.replace('<a href="products.html" class="block px-3 py-3 rounded-md text-base font-medium text-gray-900 dark:text-gray-100 hover:bg-gray-50 dark:hover:bg-gray-800">Products</a>', '<a href="products.html" class="block px-3 py-3 rounded-md text-base font-semibold text-brandRed bg-brandRed/10">Products</a>')
    elif filename == 'recipes.html':
        content = content.replace('<a href="recipes.html" class="nav-link text-gray-900 dark:text-gray-100 py-2">Recipes</a>', '<a href="recipes.html" class="nav-link text-gray-900 dark:text-gray-100 py-2 active">Recipes</a>')
        content = content.replace('<a href="recipes.html" class="block px-3 py-3 rounded-md text-base font-medium text-gray-900 dark:text-gray-100 hover:bg-gray-50 dark:hover:bg-gray-800">Recipes</a>', '<a href="recipes.html" class="block px-3 py-3 rounded-md text-base font-semibold text-brandRed bg-brandRed/10">Recipes</a>')
    elif filename == 'wholesale.html':
        content = content.replace('<a href="wholesale.html" class="nav-link text-gray-900 dark:text-gray-100 py-2">Wholesale</a>', '<a href="wholesale.html" class="nav-link text-gray-900 dark:text-gray-100 py-2 active">Wholesale</a>')
        content = content.replace('<a href="wholesale.html" class="block px-3 py-3 rounded-md text-base font-medium text-gray-900 dark:text-gray-100 hover:bg-gray-50 dark:hover:bg-gray-800">Wholesale</a>', '<a href="wholesale.html" class="block px-3 py-3 rounded-md text-base font-semibold text-brandRed bg-brandRed/10">Wholesale</a>')
    elif filename == 'contact.html':
        content = content.replace('<a href="contact.html" class="nav-link text-gray-900 dark:text-gray-100 py-2">Contact</a>', '<a href="contact.html" class="nav-link text-gray-900 dark:text-gray-100 py-2 active">Contact</a>')
        content = content.replace('<a href="contact.html" class="block px-3 py-3 rounded-md text-base font-medium text-gray-900 dark:text-gray-100 hover:bg-gray-50 dark:hover:bg-gray-800">Contact</a>', '<a href="contact.html" class="block px-3 py-3 rounded-md text-base font-semibold text-brandRed bg-brandRed/10">Contact</a>')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Headers and footers synced successfully across all pages.")
