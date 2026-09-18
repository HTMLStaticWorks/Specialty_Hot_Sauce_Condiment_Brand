document.addEventListener('DOMContentLoaded', () => {
    
    // Function to handle form validation
    const validateForm = (formId) => {
        const form = document.getElementById(formId);
        if(!form) return;

        form.addEventListener('submit', (e) => {
            e.preventDefault();
            let isValid = true;

            const requiredInputs = form.querySelectorAll('[required]');
            
            requiredInputs.forEach(input => {
                const errorSpan = input.nextElementSibling;
                
                if(!input.value.trim()) {
                    isValid = false;
                    input.classList.add('border-red-500');
                    input.classList.remove('border-gray-200', 'dark:border-gray-700');
                    if(errorSpan && errorSpan.classList.contains('error-msg')) {
                        errorSpan.classList.remove('hidden');
                    }
                } else if(input.type === 'email' && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(input.value)) {
                    isValid = false;
                    input.classList.add('border-red-500');
                    input.classList.remove('border-gray-200', 'dark:border-gray-700');
                    if(errorSpan && errorSpan.classList.contains('error-msg')) {
                        errorSpan.textContent = 'Please enter a valid email address';
                        errorSpan.classList.remove('hidden');
                    }
                } else {
                    input.classList.remove('border-red-500');
                    input.classList.add('border-gray-200', 'dark:border-gray-700');
                    if(errorSpan && errorSpan.classList.contains('error-msg')) {
                        errorSpan.classList.add('hidden');
                    }
                }
            });

            if(isValid) {
                // Show success state
                const submitBtn = form.querySelector('button[type="submit"]');
                const originalText = submitBtn.innerHTML;
                
                submitBtn.innerHTML = '<i class="fa-solid fa-check mr-2"></i> Sent Successfully';
                submitBtn.classList.remove('bg-brandRed');
                submitBtn.classList.add('bg-green-600');
                
                // Reset form
                form.reset();
                
                setTimeout(() => {
                    submitBtn.innerHTML = originalText;
                    submitBtn.classList.add('bg-brandRed');
                    submitBtn.classList.remove('bg-green-600');
                }, 4000);
            }
        });

        // Clear error on input
        const allInputs = form.querySelectorAll('input, textarea, select');
        allInputs.forEach(input => {
            input.addEventListener('input', () => {
                input.classList.remove('border-red-500');
                input.classList.add('border-gray-200', 'dark:border-gray-700');
                const errorSpan = input.nextElementSibling;
                if(errorSpan && errorSpan.classList.contains('error-msg')) {
                    errorSpan.classList.add('hidden');
                }
            });
        });
    };

    // Initialize validations
    validateForm('wholesaleForm');
    validateForm('contactForm');
});
