import os

filepath = 'wholesale.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Section Background
content = content.replace(
    '<section id="enquiry-form" class="py-24 bg-brandCharcoal text-white section-padding relative overflow-hidden">',
    '<section id="enquiry-form" class="py-24 bg-gray-50 dark:bg-brandCharcoal text-brandCharcoal dark:text-white section-padding relative overflow-hidden">'
)

# 2. Heading
content = content.replace(
    '<h2 class="text-4xl md:text-5xl font-display mb-4">Request Wholesale Pricing</h2>',
    '<h2 class="text-4xl md:text-5xl font-display mb-4 text-brandCharcoal dark:text-white">Request Wholesale Pricing</h2>'
)

# 3. Paragraph
content = content.replace(
    '<p class="text-gray-400">Fill out the details below',
    '<p class="text-gray-600 dark:text-gray-400">Fill out the details below'
)

# 4. Form wrapper
content = content.replace(
    'class="bg-white/5 p-8 md:p-12 rounded-3xl border border-white/10 backdrop-blur-md"',
    'class="bg-white dark:bg-white/5 p-8 md:p-12 rounded-3xl border border-gray-200 dark:border-white/10 shadow-xl dark:shadow-none backdrop-blur-md"'
)

# 5. Inputs and Textarea
content = content.replace(
    'bg-white/10 border border-white/20 rounded-lg py-3 px-4 text-white',
    'bg-gray-50 dark:bg-white/10 border border-gray-200 dark:border-white/20 rounded-lg py-3 px-4 text-brandCharcoal dark:text-white placeholder-gray-400 dark:placeholder-gray-500'
)

# 6. Select
content = content.replace(
    'bg-[#3c3c3c] border border-white/20 rounded-lg py-3 px-4 text-white',
    'bg-gray-50 dark:bg-[#3c3c3c] border border-gray-200 dark:border-white/20 rounded-lg py-3 px-4 text-brandCharcoal dark:text-white'
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Wholesale fixed!")
