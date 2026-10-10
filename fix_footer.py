import os
import glob

def fix_footer():
    files = glob.glob("*.html")
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()

        # Fix the conflicting background class
        content = content.replace("dark:bg-gray-100 dark:bg-white/10", "dark:bg-white/10")
        
        # In case some files only have dark:bg-gray-100 but meant dark:bg-gray-800
        # Wait, the exact string is "bg-gray-100 dark:bg-gray-100 dark:bg-white/10"
        content = content.replace("bg-gray-100 dark:bg-gray-100 dark:bg-white/10", "bg-gray-100 dark:bg-white/10")

        # Replace twitter icon with x-twitter
        # Specifically inside the aria-label="Twitter" block to be safe, but fa-brands fa-twitter is unique enough.
        content = content.replace('fa-brands fa-twitter', 'fa-brands fa-x-twitter')

        with open(file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Processed {file}")

if __name__ == "__main__":
    fix_footer()
