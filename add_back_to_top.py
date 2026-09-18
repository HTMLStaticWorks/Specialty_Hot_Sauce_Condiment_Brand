import os
import re

button_html = """                <button onclick="window.scrollTo({top: 0, behavior: 'smooth'})" class="ml-2 w-10 h-10 rounded-full bg-gray-100 dark:bg-gray-800 text-gray-600 dark:text-gray-400 flex items-center justify-center hover:bg-brandRed dark:hover:bg-brandRed hover:text-white dark:hover:text-white transition-colors shadow-sm" aria-label="Back to Top">
                    <i class="fa-solid fa-arrow-up"></i>
                </button>"""

for filename in os.listdir('.'):
    if filename.endswith('.html') and filename != 'coming-soon.html':
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Fix hover classes that might have been missed
        content = re.sub(r'class="hover:text-white( transition-colors)?"', 'class="hover:text-brandRed dark:hover:text-white transition-colors"', content)
        content = re.sub(r'<a href="#" class="hover:text-brandRed dark:hover:text-white">', '<a href="#" class="hover:text-brandRed dark:hover:text-white transition-colors">', content)
        
        # Add items-center to the flex container for bottom links if needed
        if '<div class="flex gap-6 text-sm text-gray-500">' in content:
            content = content.replace('<div class="flex gap-6 text-sm text-gray-500">', '<div class="flex gap-6 text-sm text-gray-500 items-center">')

        # Add the button if not already there
        if "fa-arrow-up" not in content:
            content = re.sub(
                r'(<a href="#" class="hover:text-brandRed dark:hover:text-white transition-colors">Terms of Service</a>\s*)</div>',
                r'\1' + button_html + '\n            </div>',
                content
            )

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

print("Back to Top button added successfully.")
