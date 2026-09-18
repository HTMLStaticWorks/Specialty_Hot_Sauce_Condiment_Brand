import re

file_path = "products.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# I want to replace `h-[80%] object-contain drop-shadow-xl z-10 transition-transform duration-500 hover:-translate-y-2`
# with `absolute inset-0 w-full h-full object-cover transition-transform duration-500 hover:scale-105`
# But I must be careful about any variations in spacing.
# The easiest way is to use regex.

pattern = r'class="h-\[80%\] object-contain drop-shadow-xl z-10 transition-transform duration-500 hover:-translate-y-2"'
replacement = 'class="absolute inset-0 w-full h-full object-cover z-0 transition-transform duration-500 hover:scale-105"'

content, count = re.subn(pattern, replacement, content)
print(f"Replaced {count} occurrences.")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
