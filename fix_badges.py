import glob, re

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We only want to replace the badges that are absolutely positioned over images
    pattern = r'class="absolute top-4 right-4 bg-brandRed/10 text-brandRed '
    replacement = r'class="absolute top-4 right-4 bg-brandRed text-white shadow-md '
    
    if re.search(pattern, content):
        content = re.sub(pattern, replacement, content)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Updated absolute badges in', file)
