import re
import sys

file_path = "products.html"

# 9 distinct bottle/sauce images
new_images = [
    "https://images.pexels.com/photos/5950444/pexels-photo-5950444.jpeg",
    "https://images.pexels.com/photos/15750739/pexels-photo-15750739.jpeg",
    "https://images.pexels.com/photos/27116329/pexels-photo-27116329.jpeg",
    "https://images.pexels.com/photos/13696031/pexels-photo-13696031.jpeg",
    "https://images.pexels.com/photos/6605151/pexels-photo-6605151.jpeg",
    "https://images.pexels.com/photos/6157052/pexels-photo-6157052.jpeg",
    "https://images.pexels.com/photos/4197491/pexels-photo-4197491.jpeg",
    "https://images.unsplash.com/photo-1574621100236-d25a6104bc86?w=600&q=80",
    "https://images.unsplash.com/photo-1591871900138-0fcbf0357564?w=600&q=80"
]

search_pattern = r'https://images\.unsplash\.com/photo-1598514982205-f36b96d1e8d4\?w=600&q=80'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace each occurrence sequentially
for img in new_images:
    content = re.sub(search_pattern, img, content, count=1)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated products.html with distinct images")
