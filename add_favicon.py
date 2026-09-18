import os

favicon_link = '    <link rel="icon" type="image/svg+xml" href="favicon.svg">\n'

for f in os.listdir('.'):
    if f.endswith('.html'):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        if 'favicon.svg' not in content:
            content = content.replace('</head>', f'{favicon_link}</head>')
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f'Added favicon to {f}')
