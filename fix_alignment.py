import re

file_path = 'index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add relative hover:z-50 to the group divs
content = content.replace('class="group flex flex-col items-center text-center cursor-pointer"', 
                          'class="group flex flex-col items-center text-center cursor-pointer relative hover:z-50"')

# Fix the tooltip positioning from absolute mt-32 to absolute top-full mt-2
content = content.replace('absolute mt-32', 'absolute top-full mt-2')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html alignments")
