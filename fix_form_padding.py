import glob
import re

def fix_newsletter_form():
    for filename in glob.glob("*.html"):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Fix input padding: Add pl-6 to the input class string
        content = content.replace(
            'class="w-full bg-white/10 border border-white/20 rounded-full py-4 sm:pr-36 text-white placeholder-gray-400',
            'class="w-full bg-white/10 border border-white/20 rounded-full py-4 pl-6 sm:pr-36 text-white placeholder-gray-400'
        )

        # Fix button padding: Add px-8 to the button class string
        content = content.replace(
            'class="w-full sm:w-auto sm:absolute sm:right-2 sm:top-2 sm:bottom-2 py-4 sm:py-0 bg-brandRed',
            'class="w-full sm:w-auto sm:absolute sm:right-2 sm:top-2 sm:bottom-2 px-8 py-4 sm:py-0 bg-brandRed'
        )

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed form in {filename}")

if __name__ == "__main__":
    fix_newsletter_form()
