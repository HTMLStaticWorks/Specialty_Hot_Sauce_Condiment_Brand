document.addEventListener('DOMContentLoaded', () => {
    const filterBtns = document.querySelectorAll('.filter-btn');
    const productCards = document.querySelectorAll('.product-item');

    if(filterBtns.length > 0 && productCards.length > 0) {
        filterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                // Remove active class from all
                filterBtns.forEach(b => {
                    b.classList.remove('bg-brandRed', 'text-white');
                    b.classList.add('bg-white', 'text-gray-700', 'dark:bg-gray-800', 'dark:text-gray-300');
                });

                // Add active class to clicked
                btn.classList.remove('bg-white', 'text-gray-700', 'dark:bg-gray-800', 'dark:text-gray-300');
                btn.classList.add('bg-brandRed', 'text-white');

                const filterValue = btn.getAttribute('data-filter');
                const filterType = btn.getAttribute('data-type'); // 'heat' or 'flavor'

                productCards.forEach(card => {
                    if (filterValue === 'all') {
                        card.style.display = 'block';
                        setTimeout(() => { card.style.opacity = '1'; card.style.transform = 'scale(1)'; }, 50);
                    } else {
                        const cardHeat = card.getAttribute('data-heat');
                        const cardFlavor = card.getAttribute('data-flavor');

                        if ((filterType === 'heat' && cardHeat === filterValue) || 
                            (filterType === 'flavor' && cardFlavor === filterValue)) {
                            card.style.display = 'block';
                            setTimeout(() => { card.style.opacity = '1'; card.style.transform = 'scale(1)'; }, 50);
                        } else {
                            card.style.opacity = '0';
                            card.style.transform = 'scale(0.95)';
                            setTimeout(() => { card.style.display = 'none'; }, 300); // match transition duration
                        }
                    }
                });
            });
        });
    }
});
