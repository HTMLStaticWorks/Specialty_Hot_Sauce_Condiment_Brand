import re

file_path = "recipes.html"

new_images = [
    "https://images.unsplash.com/photo-1608039755401-74207bf5f628?w=600&q=80", # Wings
    "https://images.unsplash.com/photo-1551504734-5ee1c4a1479b?w=600&q=80", # Tacos
    "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=600&q=80", # Pizza
    "https://images.unsplash.com/photo-1585032226651-759b368d7246?w=600&q=80", # Noodles
    "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=600&q=80", # Burger
    "https://images.unsplash.com/photo-1467003909585-2f8a72700288?w=600&q=80", # Salmon
    "https://images.unsplash.com/photo-1541519227354-08fa5d50c44d?w=600&q=80", # Avocado Toast
    "https://images.unsplash.com/photo-1632777174548-281b95b82cb9?w=600&q=80", # Grilled Corn
    "https://images.unsplash.com/photo-1625944230945-1b7dd12a80f1?w=600&q=80"  # Shrimp
]

search_pattern = r'https://images\.unsplash\.com/photo-1564834724105-918b73d1b9e0\?w=600&q=80'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

for img in new_images:
    content = re.sub(search_pattern, img, content, count=1)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated recipes.html with unique and relevant images")
