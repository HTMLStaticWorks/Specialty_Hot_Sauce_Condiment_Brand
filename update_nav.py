import os
import re

desktop_nav_template = """                <nav class="hidden lg:flex space-x-8 items-center" aria-label="Main Navigation">
                    <a href="index.html" class="nav-link text-gray-900 dark:text-gray-100 py-2 {home_a}">Home</a>
                    <a href="home-2.html" class="nav-link text-gray-900 dark:text-gray-100 py-2 {home2_a}">Home 2</a>
                    <a href="about.html" class="nav-link text-gray-900 dark:text-gray-100 py-2 {about_a}">About</a>
                    <a href="products.html" class="nav-link text-gray-900 dark:text-gray-100 py-2 {products_a}">Products</a>
                    <a href="recipes.html" class="nav-link text-gray-900 dark:text-gray-100 py-2 {recipes_a}">Recipes</a>
                    <a href="wholesale.html" class="nav-link text-gray-900 dark:text-gray-100 py-2 {wholesale_a}">Wholesale</a>
                    <a href="contact.html" class="nav-link text-gray-900 dark:text-gray-100 py-2 {contact_a}">Contact</a>
                </nav>"""

mobile_nav_template = """            <div class="px-4 pt-2 pb-6 space-y-2">
                <a href="index.html" class="block px-3 py-3 rounded-md text-base {home_m}">Home</a>
                <a href="home-2.html" class="block px-3 py-3 rounded-md text-base {home2_m}">Home 2</a>
                <a href="about.html" class="block px-3 py-3 rounded-md text-base {about_m}">About</a>
                <a href="products.html" class="block px-3 py-3 rounded-md text-base {products_m}">Products</a>
                <a href="recipes.html" class="block px-3 py-3 rounded-md text-base {recipes_m}">Recipes</a>
                <a href="wholesale.html" class="block px-3 py-3 rounded-md text-base {wholesale_m}">Wholesale</a>
                <a href="contact.html" class="block px-3 py-3 rounded-md text-base {contact_m}">Contact</a>
                <div class="mt-4 pt-4 border-t border-gray-200 dark:border-gray-700">
                    <a href="products.html" class="btn-primary w-full text-center">Shop Flavors</a>
                </div>
            </div>"""

for filename in os.listdir('.'):
    if filename.endswith('.html') and filename != 'coming-soon.html':
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Determine active file
        home_a = 'active' if filename == 'index.html' else ''
        home2_a = 'active' if filename == 'home-2.html' else ''
        about_a = 'active' if filename == 'about.html' else ''
        products_a = 'active' if filename == 'products.html' else ''
        recipes_a = 'active' if filename == 'recipes.html' else ''
        wholesale_a = 'active' if filename == 'wholesale.html' else ''
        contact_a = 'active' if filename == 'contact.html' else ''

        m_active = 'font-semibold text-brandRed bg-brandRed/10'
        m_inactive = 'font-medium text-gray-900 dark:text-gray-100 hover:bg-gray-50 dark:hover:bg-gray-800'

        home_m = m_active if filename == 'index.html' else m_inactive
        home2_m = m_active if filename == 'home-2.html' else m_inactive
        about_m = m_active if filename == 'about.html' else m_inactive
        products_m = m_active if filename == 'products.html' else m_inactive
        recipes_m = m_active if filename == 'recipes.html' else m_inactive
        wholesale_m = m_active if filename == 'wholesale.html' else m_inactive
        contact_m = m_active if filename == 'contact.html' else m_inactive

        new_desktop = desktop_nav_template.format(
            home_a=home_a, home2_a=home2_a, about_a=about_a,
            products_a=products_a, recipes_a=recipes_a,
            wholesale_a=wholesale_a, contact_a=contact_a
        ).replace('  ', ' ') # Clean up double spaces if empty
        new_desktop = new_desktop.replace(' py-2 "', ' py-2"')

        new_mobile = mobile_nav_template.format(
            home_m=home_m, home2_m=home2_m, about_m=about_m,
            products_m=products_m, recipes_m=recipes_m,
            wholesale_m=wholesale_m, contact_m=contact_m
        )

        # Regex replace desktop nav
        content = re.sub(
            r'                <nav class="hidden lg:flex space-x-8 items-center" aria-label="Main Navigation">.*?</nav>',
            new_desktop,
            content,
            flags=re.DOTALL
        )

        # Regex replace mobile nav
        content = re.sub(
            r'            <div class="px-4 pt-2 pb-6 space-y-2">.*?</div>\n            </div>',
            new_mobile,
            content,
            flags=re.DOTALL
        )

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

print("Navigation updated successfully.")
