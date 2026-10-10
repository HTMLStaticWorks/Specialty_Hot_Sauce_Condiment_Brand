import re

def update_file(filename, replacement_code):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the last <section> block before </main>
    # Find all sections first
    sections = list(re.finditer(r'(<!--.*?-->\s*)?<section.*?</section>', content, re.DOTALL))
    if not sections:
        return
    
    last_section = sections[-1]
    
    # We replace only the last section
    new_content = content[:last_section.start()] + replacement_code + content[last_section.end():]
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {filename}")

# --- Products ---
products_cta = """<!-- SECTION 5: Product CTA -->
<section class="relative py-32 overflow-hidden section-padding">
  <div class="absolute inset-0 z-0">
    <img src="https://images.unsplash.com/photo-1598514982205-f36b96d1e8d4?w=1600&q=80" alt="Chili ingredients flatlay" class="w-full h-full object-cover object-center scale-110" data-aos="scale-in" data-aos-duration="2000">
    <div class="absolute inset-0 bg-black/70 backdrop-blur-sm"></div>
  </div>
  <div class="max-w-4xl mx-auto relative z-10 text-center text-white" data-aos="fade-up">
    <i class="fa-solid fa-pepper-hot text-5xl text-brandRed mb-6 block"></i>
    <h2 class="text-5xl md:text-6xl font-display mb-6 text-white">Not Sure Where to Start?</h2>
    <p class="text-xl text-gray-300 mb-10 max-w-2xl mx-auto">Take our interactive flavor quiz to find your perfect heat match in under 60 seconds.</p>
    <button class="btn-primary border-2 border-brandRed hover:bg-transparent hover:text-brandRed text-lg py-4 transition-colors"> Find My Sauce </button>
  </div>
</section>"""
update_file('products.html', products_cta)

# --- About ---
about_cta = """<!-- SECTION 5: CTA -->
<section class="relative py-32 overflow-hidden section-padding">
  <div class="absolute inset-0 z-0">
    <img src="https://images.unsplash.com/photo-1598514982205-f36b96d1e8d4?w=1600&q=80" alt="Chili ingredients flatlay" class="w-full h-full object-cover object-center scale-110" data-aos="scale-in" data-aos-duration="2000">
    <div class="absolute inset-0 bg-black/70 backdrop-blur-sm"></div>
  </div>
  <div class="max-w-4xl mx-auto relative z-10 text-center text-white" data-aos="fade-up">
    <i class="fa-solid fa-quote-left text-4xl text-brandRed/50 mb-8 block"></i>
    <h2 class="text-3xl md:text-5xl font-display leading-tight mb-12 text-white">"We don't make hot sauce for people who want to prove how tough they are. We make hot sauce for people who want their food to taste incredible."</h2>
    <a href="products.html" class="btn-primary border-2 border-brandRed hover:bg-transparent hover:text-brandRed text-lg py-4 transition-colors">Experience the Flavor</a>
  </div>
</section>"""
update_file('about.html', about_cta)

# --- Recipes ---
recipes_cta = """<!-- SECTION 4: Newsletter -->
<section class="relative py-32 overflow-hidden section-padding">
  <div class="absolute inset-0 z-0">
    <img src="https://images.unsplash.com/photo-1598514982205-f36b96d1e8d4?w=1600&q=80" alt="Ingredients background" class="w-full h-full object-cover object-center scale-110" data-aos="scale-in" data-aos-duration="2000">
    <div class="absolute inset-0 bg-black/70 backdrop-blur-sm"></div>
  </div>
  <div class="max-w-4xl mx-auto relative z-10 text-center text-white" data-aos="fade-up">
    <h2 class="text-5xl md:text-6xl font-display mb-6 text-white">Fresh Recipes.<br>Straight to Your Inbox.</h2>
    <p class="text-xl text-gray-300 mb-10 max-w-2xl mx-auto">We drop a new fiery recipe every Friday. Don't miss out.</p>
    <form class="max-w-md mx-auto flex flex-col sm:block relative group gap-3">
      <input type="email" placeholder="Email address" required class="w-full bg-white/10 border border-white/20 rounded-full py-4 sm:pr-36 text-white placeholder-gray-400 focus:outline-none focus:border-brandRed transition-colors backdrop-blur-md">
      <button type="submit" class="w-full sm:w-auto sm:absolute sm:right-2 sm:top-2 sm:bottom-2 py-4 sm:py-0 bg-brandRed hover:bg-brandRedDark text-white font-bold rounded-full transition-colors"> Sign Me Up </button>
    </form>
  </div>
</section>"""
update_file('recipes.html', recipes_cta)

# --- Home-2 ---
home2_cta = """<!-- SECTION 6: Wholesale CTA -->
<section class="relative py-32 overflow-hidden section-padding">
  <div class="absolute inset-0 z-0">
    <img src="https://images.unsplash.com/photo-1598514982205-f36b96d1e8d4?w=1600&q=80" alt="Wholesale boxes" class="w-full h-full object-cover object-center scale-110" data-aos="scale-in" data-aos-duration="2000">
    <div class="absolute inset-0 bg-black/70 backdrop-blur-sm"></div>
  </div>
  <div class="max-w-4xl mx-auto relative z-10 text-center text-white" data-aos="fade-up">
    <span class="text-brandRed font-bold tracking-widest text-sm uppercase mb-4 block">For Retailers & Restaurants</span>
    <h2 class="text-5xl md:text-6xl font-display mb-6 text-white">Bring Fyrza to Your Customers.</h2>
    <p class="text-xl text-gray-300 mb-10 max-w-2xl mx-auto">Stock the shelves of your specialty store, grocery, or restaurant with a hot sauce brand that demands attention.</p>
    <a href="wholesale.html" class="btn-primary border-2 border-brandRed hover:bg-transparent hover:text-brandRed text-lg py-4 transition-colors">Start a Wholesale Order</a>
  </div>
</section>"""
update_file('home-2.html', home2_cta)
