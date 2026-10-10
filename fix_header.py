import glob

def fix_header_breakpoints():
    files = glob.glob('*.html')
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Apply replacements to fix the 1024px nav squish issue (upgrading lg to xl breakpoint)
        content = content.replace('class="flex justify-between items-center h-20"', 'class="flex justify-between items-center h-20 gap-6 xl:gap-8"')
        content = content.replace('class="hidden lg:flex gap-8 items-center"', 'class="hidden xl:flex gap-8 items-center"')
        content = content.replace('class="hidden lg:flex items-center gap-6"', 'class="hidden xl:flex items-center gap-6"')
        content = content.replace('class="lg:hidden flex items-center gap-4"', 'class="xl:hidden flex items-center gap-4"')
        content = content.replace('class="hidden lg:hidden bg-white', 'class="hidden xl:hidden bg-white')

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed header in {file}")

if __name__ == '__main__':
    fix_header_breakpoints()
