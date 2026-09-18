import os, glob

replacements = [
    # Orange
    ('text-brandOrange', 'text-brandRed'),
    ('bg-brandOrange', 'bg-brandRed'),
    ('text-orange-400', 'text-brandRed'),
    ('text-orange-500', 'text-brandRed'),
    ('text-orange-800', 'text-brandRed'),
    ('bg-orange-100', 'bg-brandRed/10'),
    ('bg-orange-500', 'bg-brandRed'),
    ('bg-orange-600', 'bg-brandRed'),
    
    # Yellow
    ('text-yellow-400', 'text-brandRed'),
    ('text-yellow-500', 'text-brandRed'),
    ('text-yellow-600', 'text-brandRed'),
    ('text-yellow-800', 'text-brandRed'),
    ('bg-yellow-100', 'bg-brandRed/10'),
    ('bg-yellow-500', 'bg-brandRed'),
    
    # Green
    ('text-green-500', 'text-brandRed'),
    ('text-green-600', 'text-brandRed'),
    ('text-green-700', 'text-brandRed'),
    ('text-green-800', 'text-brandRed'),
    ('bg-green-100', 'bg-brandRed/10'),
    ('bg-green-500', 'bg-brandRed'),
    
    # Purple
    ('text-purple-500', 'text-brandRed'),
    ('bg-purple-100', 'bg-brandRed/10'),
    
    # Pink
    ('text-pink-500', 'text-brandRed'),
    
    # Amber
    ('text-amber-700', 'text-brandRed'),
    ('dark:text-amber-500', 'dark:text-brandRed'),
    
    # Red (standard red -> brandRed)
    ('bg-red-100', 'bg-brandRed/10'),
    ('text-red-600', 'text-brandRed'),
    ('text-red-800', 'text-brandRed'),
    ('bg-red-900', 'bg-brandRed/30'),
]

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    original_content = content
    for old, new in replacements:
        content = content.replace(old, new)
        
    if content != original_content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print('Updated', f)
