// Main JavaScript file for Milk Tea Ordering System

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all components
    initializeOrderForm();
    initializePaymentForm();
    initializeStatusUpdates();
    initializeAnimations();
});

// Order Form Functionality
function initializeOrderForm() {
    const orderForms = document.querySelectorAll('.order-form');
    
    orderForms.forEach(form => {
        const sizeSelect = form.querySelector('select[name="size_id"]');
        const flavorSelect = form.querySelector('select[name="flavor_id"]');
        const toppingsCheckboxes = form.querySelectorAll('input[name="toppings"]');
        const quantityInput = form.querySelector('input[name="quantity"]');
        
        if (sizeSelect || flavorSelect || toppingsCheckboxes.length > 0) {
            // Add price calculation
            addPriceCalculation(form);
        }
    });
}

function addPriceCalculation(form) {
    const drinkCard = form.closest('.drink-card');
    const basePriceElement = drinkCard.querySelector('.price');
    const basePrice = parseFloat(basePriceElement.textContent.replace('$', ''));
    
    // Create price display element
    let totalPriceElement = form.querySelector('.total-price');
    if (!totalPriceElement) {
        totalPriceElement = document.createElement('div');
        totalPriceElement.className = 'total-price';
        totalPriceElement.style.cssText = 'font-weight: bold; color: #27ae60; margin: 1rem 0; font-size: 1.2rem;';
        form.insertBefore(totalPriceElement, form.querySelector('button'));
    }
    
    function calculatePrice() {
        let totalPrice = basePrice;
        
        // Size multiplier
        const sizeSelect = form.querySelector('select[name="size_id"]');
        if (sizeSelect) {
            const selectedSize = sizeSelect.options[sizeSelect.selectedIndex];
            const multiplierMatch = selectedSize.text.match(/×([\d.]+)/);
            if (multiplierMatch) {
                totalPrice *= parseFloat(multiplierMatch[1]);
            }
        }
        
        // Flavor additional price
        const flavorSelect = form.querySelector('select[name="flavor_id"]');
        if (flavorSelect && flavorSelect.value) {
            const selectedFlavor = flavorSelect.options[flavorSelect.selectedIndex];
            const priceMatch = selectedFlavor.text.match(/\+\$([\d.]+)/);
            if (priceMatch) {
                totalPrice += parseFloat(priceMatch[1]);
            }
        }
        
        // Toppings price
        const toppingsCheckboxes = form.querySelectorAll('input[name="toppings"]:checked');
        toppingsCheckboxes.forEach(checkbox => {
            const label = checkbox.closest('label');
            const priceMatch = label.textContent.match(/\+\$([\d.]+)/);
            if (priceMatch) {
                totalPrice += parseFloat(priceMatch[1]);
            }
        });
        
        // Quantity
        const quantityInput = form.querySelector('input[name="quantity"]');
        const quantity = quantityInput ? parseInt(quantityInput.value) || 1 : 1;
        totalPrice *= quantity;
        
        totalPriceElement.textContent = `Total: $${totalPrice.toFixed(2)}`;
    }
    
    // Add event listeners
    form.addEventListener('change', calculatePrice);
    form.addEventListener('input', calculatePrice);
    
    // Initial calculation
    calculatePrice();
}

// Payment Form Functionality
function initializePaymentForm() {
    const paymentForm = document.querySelector('.payment-form');
    if (!paymentForm) return;
    
    const paymentOptions = paymentForm.querySelectorAll('input[name="payment_method"]');
    const creditCardInfo = document.getElementById('credit-card-info');
    
    paymentOptions.forEach(option => {
        option.addEventListener('change', function() {
            if (creditCardInfo) {
                creditCardInfo.style.display = this.value === 'credit_card' ? 'block' : 'none';
            }
        });
    });
}

// Status Updates for Order Tracking
function initializeStatusUpdates() {
    const statusContainer = document.querySelector('.order-status-card');
    if (!statusContainer) return;
    
    // Auto-refresh functionality is handled in the template
    // This function can be extended for additional status features
    
    // Add visual feedback for status changes
    const statusItems = document.querySelectorAll('.status-item');
    statusItems.forEach(item => {
        item.addEventListener('click', function() {
            // Could add manual status update functionality here
            console.log('Status item clicked:', this.dataset.status);
        });
    });
}

// Animation and UI Enhancements
function initializeAnimations() {
    // Smooth scroll for navigation
    const navLinks = document.querySelectorAll('nav a');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            // Add smooth transition effect
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 150);
        });
    });
    
    // Button click animations
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 150);
        });
    });
    
    // Form validation feedback
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    field.style.borderColor = '#e74c3c';
                    isValid = false;
                } else {
                    field.style.borderColor = '#27ae60';
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                showNotification('Please fill in all required fields', 'error');
            }
        });
    });
}

// Utility Functions
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `message ${type}`;
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        z-index: 1000;
        max-width: 300px;
        animation: slideIn 0.3s ease-out;
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease-in';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 3000);
}

// Add CSS animations
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes slideOut {
        from { transform: translateX(0); opacity: 1; }
        to { transform: translateX(100%); opacity: 0; }
    }
`;
document.head.appendChild(style);

// Cart functionality
let cart = JSON.parse(sessionStorage.getItem('milkTeaCart')) || [];

function addToCart(item) {
    cart.push(item);
    sessionStorage.setItem('milkTeaCart', JSON.stringify(cart));
    updateCartDisplay();
    showNotification('Item added to cart!', 'success');
}

function updateCartDisplay() {
    const cartCount = document.querySelector('.cart-count');
    if (cartCount) {
        cartCount.textContent = cart.length;
    }
}

// Order status polling for real-time updates
function startStatusPolling(orderNumber) {
    if (!orderNumber) return;
    
    const pollInterval = setInterval(() => {
        fetch(`/api/order-status/${orderNumber}/`)
            .then(response => response.json())
            .then(data => {
                updateOrderStatusDisplay(data.status);
                
                // Stop polling when order is completed
                if (data.status === 'completed') {
                    clearInterval(pollInterval);
                }
            })
            .catch(error => {
                console.error('Error polling order status:', error);
                clearInterval(pollInterval);
            });
    }, 5000); // Poll every 5 seconds
    
    // Stop polling after 30 minutes
    setTimeout(() => {
        clearInterval(pollInterval);
    }, 30 * 60 * 1000);
}

function updateOrderStatusDisplay(status) {
    const statusText = document.getElementById('status-text');
    const statusItems = document.querySelectorAll('.status-item');
    const receiveBtn = document.getElementById('receive-btn');
    
    if (!statusText) return;
    
    const statusMap = {
        'placed': 'Order Placed',
        'preparing': 'Preparing Your Order',
        'ready': 'Ready for Pickup'
    };
    
    statusText.textContent = statusMap[status] || status;
    
    // Update visual indicators
    statusItems.forEach(item => {
        item.classList.remove('active', 'completed');
        const itemStatus = item.getAttribute('data-status');
        
        if (itemStatus === status) {
            item.classList.add('active');
        } else if (
            (status === 'preparing' && itemStatus === 'placed') ||
            (status === 'ready' && (itemStatus === 'placed' || itemStatus === 'preparing'))
        ) {
            item.classList.add('completed');
        }
    });
    
    // Show receive button when ready
    if (receiveBtn) {
        receiveBtn.style.display = status === 'ready' ? 'inline-block' : 'none';
    }
}

// Export functions for use in templates
window.MilkTeaSystem = {
    addToCart,
    updateCartDisplay,
    startStatusPolling,
    updateOrderStatusDisplay,
    showNotification
};
