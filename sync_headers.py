import os
import re

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract global header precisely
header_match = re.search(r'(<header id="globalHeader".*?</header>)', index_content, re.DOTALL)
if not header_match:
    print("Could not find globalHeader in index.html")
    exit(1)
source_header = header_match.group(1)

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html']

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # If it has globalHeader, replace it
    if '<header id="globalHeader"' in content:
        content = re.sub(r'<header id="globalHeader".*?</header>', source_header, content, flags=re.DOTALL)
        
        # Now fix the active links
        # First remove active from Home (desktop)
        content = content.replace('class="nav-link text-gray-900 dark:text-gray-100 py-2 active"', 'class="nav-link text-gray-900 dark:text-gray-100 py-2"')
        
        # First remove active from Home (mobile)
        content = content.replace('class="block px-3 py-3 rounded-md text-base font-semibold text-brandRed bg-brandRed/10"', 'class="block px-3 py-3 rounded-md text-base font-medium text-gray-900 dark:text-gray-100 hover:bg-gray-50 dark:hover:bg-gray-800"')
        
        # Add active class to current file's nav-link (desktop)
        link_pattern_desktop = f'<a href="{filename}" class="nav-link text-gray-900 dark:text-gray-100 py-2">'
        link_active_desktop = f'<a href="{filename}" class="nav-link text-gray-900 dark:text-gray-100 py-2 active">'
        content = content.replace(link_pattern_desktop, link_active_desktop)
        
        # Add active class to current file's nav-link (mobile)
        link_pattern_mobile = f'<a href="{filename}"\n                    class="block px-3 py-3 rounded-md text-base font-medium text-gray-900 dark:text-gray-100 hover:bg-gray-50 dark:hover:bg-gray-800">'
        link_active_mobile = f'<a href="{filename}"\n                    class="block px-3 py-3 rounded-md text-base font-semibold text-brandRed bg-brandRed/10">'
        # We need to handle potential whitespace variations
        content = re.sub(fr'<a href="{filename}"\s+class="block px-3 py-3 rounded-md text-base font-medium text-gray-900 dark:text-gray-100 hover:bg-gray-50 dark:hover:bg-gray-800">', 
                         fr'<a href="{filename}" class="block px-3 py-3 rounded-md text-base font-semibold text-brandRed bg-brandRed/10">', content)


        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated header in {filename}")
    else:
        print(f"No globalHeader in {filename}")

