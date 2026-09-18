import os, glob, re

replacements = [
    (r'https://loremflickr\.com/\d+/\d+/bottle,sauce\?[^"\'\s]*', 'https://images.unsplash.com/photo-1598514982205-f36b96d1e8d4?w=600&q=80'),
    (r'https://loremflickr\.com/\d+/\d+/food,spicy\?[^"\'\s]*', 'https://images.unsplash.com/photo-1564834724105-918b73d1b9e0?w=600&q=80'),
    (r'https://loremflickr\.com/\d+/\d+/farming\?[^"\'\s]*', 'https://images.pexels.com/photos/15750739/pexels-photo-15750739.jpeg'),
    (r'https://loremflickr\.com/\d+/\d+/spices\?[^"\'\s]*', 'https://images.unsplash.com/photo-1596040033229-a9821ebd058d?w=600&q=80'),
    (r'https://loremflickr\.com/\d+/\d+/bottling\?[^"\'\s]*', 'https://images.unsplash.com/photo-1622485542475-472091409f6e?w=600&q=80'),
    (r'https://loremflickr\.com/\d+/\d+/dark,bottle\?[^"\'\s]*', 'https://images.unsplash.com/photo-1598515753229-411a7db8b7a0?w=1600&q=80'),
    (r'https://loremflickr\.com/\d+/\d+/fire,abstract\?[^"\'\s]*', 'https://images.unsplash.com/photo-1603504106399-563b7848f21f?w=1600&q=80')
]

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    original_content = content
    for pattern, repl in replacements:
        content = re.sub(pattern, repl, content)
        
    if content != original_content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print('Updated', f)
