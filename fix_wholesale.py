import re

file_path = 'wholesale.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# I will replace the 4 cards entirely with a robust structure
new_cards = """
                    <!-- Wholesale Product 1 -->
                    <div class="bg-white dark:bg-gray-800 rounded-xl overflow-hidden shadow-sm border border-gray-100 dark:border-gray-700 flex flex-col" data-aos="fade-up">
                        <img src="https://images.unsplash.com/photo-1598514982205-f36b96d1e8d4?w=600&q=80" alt="Smoked Ember" class="w-full h-48 object-cover m-0 p-0 block">
                        <div class="p-6 flex flex-col flex-grow">
                            <h3 class="text-xl font-bold mb-1">Smoked Ember</h3>
                            <div class="flex justify-between items-center text-sm text-gray-500 mb-4 pb-4 border-b border-gray-100 dark:border-gray-700">
                                <span>5oz Bottle</span>
                                <span class="font-bold text-brandRed">Medium Heat</span>
                            </div>
                            <ul class="text-sm space-y-2 text-gray-600 dark:text-gray-300">
                                <li class="flex justify-between"><span>Units per case:</span> <strong>12</strong></li>
                                <li class="flex justify-between"><span>Retail MSRP:</span> <strong>$12.99</strong></li>
                            </ul>
                        </div>
                    </div>

                    <!-- Wholesale Product 2 -->
                    <div class="bg-white dark:bg-gray-800 rounded-xl overflow-hidden shadow-sm border border-gray-100 dark:border-gray-700 flex flex-col" data-aos="fade-up" data-aos-delay="100">
                        <img src="https://images.unsplash.com/photo-1598515753229-411a7db8b7a0?w=600&q=80" alt="Mango Blaze" class="w-full h-48 object-cover m-0 p-0 block">
                        <div class="p-6 flex flex-col flex-grow">
                            <h3 class="text-xl font-bold mb-1">Mango Blaze</h3>
                            <div class="flex justify-between items-center text-sm text-gray-500 mb-4 pb-4 border-b border-gray-100 dark:border-gray-700">
                                <span>5oz Bottle</span>
                                <span class="font-bold text-brandRed">Hot Heat</span>
                            </div>
                            <ul class="text-sm space-y-2 text-gray-600 dark:text-gray-300">
                                <li class="flex justify-between"><span>Units per case:</span> <strong>12</strong></li>
                                <li class="flex justify-between"><span>Retail MSRP:</span> <strong>$14.99</strong></li>
                            </ul>
                        </div>
                    </div>

                    <!-- Wholesale Product 3 -->
                    <div class="bg-white dark:bg-gray-800 rounded-xl overflow-hidden shadow-sm border border-gray-100 dark:border-gray-700 flex flex-col" data-aos="fade-up" data-aos-delay="200">
                        <img src="https://images.unsplash.com/photo-1564834724105-918b73d1b9e0?w=600&q=80" alt="Inferno Drop" class="w-full h-48 object-cover m-0 p-0 block">
                        <div class="p-6 flex flex-col flex-grow">
                            <h3 class="text-xl font-bold mb-1">Inferno Drop</h3>
                            <div class="flex justify-between items-center text-sm text-gray-500 mb-4 pb-4 border-b border-gray-100 dark:border-gray-700">
                                <span>5oz Bottle</span>
                                <span class="font-bold text-brandRed">Extreme Heat</span>
                            </div>
                            <ul class="text-sm space-y-2 text-gray-600 dark:text-gray-300">
                                <li class="flex justify-between"><span>Units per case:</span> <strong>12</strong></li>
                                <li class="flex justify-between"><span>Retail MSRP:</span> <strong>$16.99</strong></li>
                            </ul>
                        </div>
                    </div>

                    <!-- Wholesale Product 4 -->
                    <div class="bg-white dark:bg-gray-800 rounded-xl overflow-hidden shadow-sm border border-gray-100 dark:border-gray-700 flex flex-col" data-aos="fade-up" data-aos-delay="300">
                        <img src="https://images.unsplash.com/photo-1622485542475-472091409f6e?w=600&q=80" alt="Food Service Jugs" class="w-full h-48 object-cover m-0 p-0 block">
                        <div class="p-6 flex flex-col flex-grow">
                            <h3 class="text-xl font-bold mb-1">Food Service Jugs</h3>
                            <div class="flex justify-between items-center text-sm text-gray-500 mb-4 pb-4 border-b border-gray-100 dark:border-gray-700">
                                <span>64oz Jug</span>
                                <span class="font-bold text-gray-500">All Flavors</span>
                            </div>
                            <ul class="text-sm space-y-2 text-gray-600 dark:text-gray-300">
                                <li class="flex justify-between"><span>Units per case:</span> <strong>4</strong></li>
                                <li class="flex justify-between"><span>Target:</span> <strong>Restaurants</strong></li>
                            </ul>
                        </div>
                    </div>
"""

# Replace the grid contents
pattern = r'<!-- Wholesale Product 1 -->.*<!-- SECTION 4: How Wholesale Works -->'
content = re.sub(pattern, new_cards + '\n                </div>\n            </div>\n        </section>\n\n        <!-- SECTION 4: How Wholesale Works -->', content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated wholesale.html")
