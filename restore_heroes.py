import os
import re

files_to_fix = {
    'products.html': '''        </div>
    </header>

    <main class="pt-20">
        <!-- SECTION 1: Shop Hero -->
        <section class="relative py-32 overflow-hidden bg-brandCream dark:bg-[#121212] section-padding border-b border-gray-100 dark:border-gray-800">
            <div class="max-w-7xl mx-auto relative z-10 text-center" data-aos="fade-up">
                <span class="inline-block py-1 px-3 rounded-full bg-brandRed/10 text-brandRed font-semibold text-sm tracking-wider mb-6">SHOP ALL</span>
                <h1 class="text-5xl md:text-7xl font-display font-black mb-6">Find Your <span class="text-brandOrange">Perfect Heat.</span></h1>
                <p class="text-xl text-gray-600 dark:text-gray-400 max-w-3xl mx-auto mb-10 leading-relaxed">
                    From our mild, fruit-forward blends to our extreme reaper mash, every bottle of Fyrza is guaranteed to elevate your next meal. Explore our full collection below and prepare to turn up the flavor.
                </p>
            </div>
        </section>''',
    
    'recipes.html': '''        </div>
    </header>

    <main class="pt-20">
        <!-- SECTION 1: Recipes Hero -->
        <section class="relative py-32 overflow-hidden bg-brandCream dark:bg-[#121212] section-padding border-b border-gray-100 dark:border-gray-800">
            <div class="max-w-7xl mx-auto relative z-10 text-center" data-aos="fade-up">
                <span class="inline-block py-1 px-3 rounded-full bg-brandRed/10 text-brandRed font-semibold text-sm tracking-wider mb-6">RECIPES</span>
                <h1 class="text-5xl md:text-7xl font-display font-black mb-6">Fire In The <span class="text-brandOrange">Kitchen.</span></h1>
                <p class="text-xl text-gray-600 dark:text-gray-400 max-w-3xl mx-auto mb-10 leading-relaxed">
                    Hot sauce isn't just a condiment—it's a core ingredient. Discover how Fyrza can transform your everyday cooking into culinary masterpieces.
                </p>
            </div>
        </section>''',

    'wholesale.html': '''        </div>
    </header>

    <main class="pt-20">
        <!-- SECTION 1: Wholesale Hero -->
        <section class="relative py-32 overflow-hidden bg-brandCream dark:bg-[#121212] section-padding border-b border-gray-100 dark:border-gray-800">
            <div class="max-w-7xl mx-auto relative z-10 text-center" data-aos="fade-up">
                <span class="inline-block py-1 px-3 rounded-full bg-brandRed/10 text-brandRed font-semibold text-sm tracking-wider mb-6">WHOLESALE</span>
                <h1 class="text-5xl md:text-7xl font-display font-black mb-6">Stock The <span class="text-brandOrange">Fire.</span></h1>
                <p class="text-xl text-gray-600 dark:text-gray-400 max-w-3xl mx-auto mb-10 leading-relaxed">
                    Partner with Fyrza and bring premium, artisan heat to your retail shelves or restaurant tables. We offer competitive pricing and unmatched quality.
                </p>
            </div>
        </section>''',

    'contact.html': '''        </div>
    </header>

    <main class="pt-20">
        <!-- SECTION 1: Contact Hero -->
        <section class="relative py-32 overflow-hidden bg-brandCream dark:bg-[#121212] section-padding border-b border-gray-100 dark:border-gray-800">
            <div class="max-w-7xl mx-auto relative z-10 text-center" data-aos="fade-up">
                <span class="inline-block py-1 px-3 rounded-full bg-brandRed/10 text-brandRed font-semibold text-sm tracking-wider mb-6">CONTACT US</span>
                <h1 class="text-5xl md:text-7xl font-display font-black mb-6">Let's <span class="text-brandOrange">Talk Heat.</span></h1>
                <p class="text-xl text-gray-600 dark:text-gray-400 max-w-3xl mx-auto mb-10 leading-relaxed">
                    Have a question about an order? Want to collaborate? Or just want to share your favorite Fyrza recipe? We're all ears.
                </p>
            </div>
        </section>'''
}

for filename, replacement in files_to_fix.items():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Look for the buggy </section> right after the mobile menu
        # The mobile menu ends with:
        #             </div>
        #         </section>
        
        # We will replace `            </div>\n        </section>` with the new replacement string.
        # Let's use regex to find it safely.
        content = re.sub(
            r'            </div>\n        </section>',
            replacement,
            content,
            count=1
        )
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {filename}")
