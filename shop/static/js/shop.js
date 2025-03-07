// Cart functionality for AK Mobile Case shop
document.addEventListener('DOMContentLoaded', function() {
    // Cart state
    let cart = [];
    
    // DOM Elements
    const addToCartButtons = document.querySelectorAll('.add-to-cart-btn');
    const cartSidebar = document.querySelector('.cart-sidebar');
    const cartOverlay = document.querySelector('.cart-overlay');
    const closeCartButton = document.querySelector('.close-cart');
    const cartItems = document.querySelector('.cart-items');
    const emptyCartMessage = document.querySelector('.empty-cart-message');
    const subtotalAmount = document.querySelector('.subtotal-amount');
    const totalAmount = document.querySelector('.total-amount');
    const checkoutBtn = document.querySelector('.checkout-btn');
    const continueShoppingBtn = document.querySelector('.continue-shopping');
    const cartIcon = document.querySelector('.fa-shopping-cart').parentElement;
    
    // Event Listeners
    addToCartButtons.forEach(button => {
        button.addEventListener('click', addToCart);
    });
    
    closeCartButton.addEventListener('click', closeCart);
    cartOverlay.addEventListener('click', closeCart);
    continueShoppingBtn.addEventListener('click', closeCart);
    cartIcon.addEventListener('click', openCart);
    
    // Add to cart function
    function addToCart(event) {
        const button = event.target;
        const productId = button.getAttribute('data-product-id');
        const productCard = button.closest('.product-card');
        const productImage = productCard.querySelector('.product-image img').src;
        const productName = productCard.querySelector('.product-category').textContent;
        const productPrice = productCard.querySelector('.current-price').textContent;
        const priceValue = parseInt(productPrice.replace('₹', ''));
        
        // Get selected model (first model as default)
        const modelOptions = productCard.querySelectorAll('.variant-option');
        const model = modelOptions.length > 0 ? modelOptions[0].textContent : 'Default';
        
        // Check if product already in cart
        const existingItem = cart.find(item => item.id === productId && item.model === model);
        
        if (existingItem) {
            existingItem.quantity += 1;
        } else {
            cart.push({
                id: productId,
                name: productName,
                price: priceValue,
                image: productImage,
                model: model,
                quantity: 1
            });
        }
        
        // Show success message
        showNotification(`${productName} (${model}) added to cart!`);
        
        // Update cart
        updateCart();
    }
    
    // Update cart display
    function updateCart() {
        // Clear current cart display
        cartItems.innerHTML = '';
        
        if (cart.length === 0) {
            cartItems.appendChild(emptyCartMessage);
            subtotalAmount.textContent = '₹0.00';
            totalAmount.textContent = '₹0.00';
            return;
        }
        
        // Hide empty cart message
        if (emptyCartMessage.parentNode === cartItems) {
            cartItems.removeChild(emptyCartMessage);
        }
        
        // Calculate total
        let subtotal = 0;
        
        // Add each item to cart
        cart.forEach(item => {
            const cartItemElement = document.createElement('div');
            cartItemElement.classList.add('cart-item');
            
            const itemTotal = item.price * item.quantity;
            subtotal += itemTotal;
            
            cartItemElement.innerHTML = `
                <div class="cart-item-image">
                    <img src="${item.image}" alt="${item.name}">
                </div>
                <div class="cart-item-details">
                    <h4 class="cart-item-name">${item.name}</h4>
                    <p class="cart-item-model">Model: ${item.model}</p>
                    <p class="cart-item-price">₹${item.price}</p>
                    <div class="cart-item-quantity">
                        <button class="quantity-btn minus" data-id="${item.id}" data-model="${item.model}">-</button>
                        <span class="quantity">${item.quantity}</span>
                        <button class="quantity-btn plus" data-id="${item.id}" data-model="${item.model}">+</button>
                    </div>
                </div>
                <button class="remove-item" data-id="${item.id}" data-model="${item.model}">
                    <i class="fas fa-trash"></i>
                </button>
            `;
            
            cartItems.appendChild(cartItemElement);
        });
        
        // Update totals
        subtotalAmount.textContent = `₹${subtotal.toFixed(2)}`;
        totalAmount.textContent = `₹${subtotal.toFixed(2)}`;
        
        // Add event listeners to quantity buttons and remove buttons
        document.querySelectorAll('.quantity-btn.minus').forEach(button => {
            button.addEventListener('click', decreaseQuantity);
        });
        
        document.querySelectorAll('.quantity-btn.plus').forEach(button => {
            button.addEventListener('click', increaseQuantity);
        });
        
        document.querySelectorAll('.remove-item').forEach(button => {
            button.addEventListener('click', removeItem);
        });
    }
    
    // Increase item quantity
    function increaseQuantity(event) {
        const id = event.target.getAttribute('data-id');
        const model = event.target.getAttribute('data-model');
        const item = cart.find(item => item.id === id && item.model === model);
        
        if (item) {
            item.quantity += 1;
            updateCart();
        }
    }
    
    // Decrease item quantity
    function decreaseQuantity(event) {
        const id = event.target.getAttribute('data-id');
        const model = event.target.getAttribute('data-model');
        const item = cart.find(item => item.id === id && item.model === model);
        
        if (item) {
            item.quantity -= 1;
            
            if (item.quantity <= 0) {
                removeItem(event);
                return;
            }
            
            updateCart();
        }
    }
    
    // Remove item from cart
    function removeItem(event) {
        const id = event.target.closest('[data-id]').getAttribute('data-id');
        const model = event.target.closest('[data-model]').getAttribute('data-model');
        
        cart = cart.filter(item => !(item.id === id && item.model === model));
        updateCart();
    }
    
    // Open cart
    function openCart() {
        cartSidebar.classList.add('active');
        cartOverlay.classList.add('active');
        document.body.style.overflow = 'hidden'; // Prevent scrolling when cart is open
    }
    
    // Close cart
    function closeCart() {
        cartSidebar.classList.remove('active');
        cartOverlay.classList.remove('active');
        document.body.style.overflow = ''; // Restore scrolling
    }
    
    // Show notification
    function showNotification(message) {
        const notification = document.createElement('div');
        notification.classList.add('notification');
        notification.textContent = message;
        
        document.body.appendChild(notification);
        
        // Show notification
        setTimeout(() => {
            notification.classList.add('show');
        }, 10);
        
        // Hide and remove notification
        setTimeout(() => {
            notification.classList.remove('show');
            setTimeout(() => {
                document.body.removeChild(notification);
            }, 300);
        }, 3000);
    }
    
    // Checkout button
    checkoutBtn.addEventListener('click', function() {
        if (cart.length === 0) {
            showNotification('Your cart is empty!');
            return;
        }
        
        showNotification('Proceeding to checkout...');
        // Here you would typically redirect to a checkout page
        // window.location.href = '/checkout';
    });
});


// Variant selection functionality
document.addEventListener('DOMContentLoaded', function() {
    // Initialize variant selection
    const variantOptions = document.querySelectorAll('.variant-option');
    
    variantOptions.forEach(option => {
        option.addEventListener('click', function() {
            // Get all options in the same group
            const optionsGroup = this.parentElement.querySelectorAll('.variant-option');
            
            // Remove selected class from all options in group
            optionsGroup.forEach(opt => {
                opt.classList.remove('selected');
            });
            
            // Add selected class to clicked option
            this.classList.add('selected');
        });
    });
    
    // Initialize with first option selected
    const productCards = document.querySelectorAll('.product-card');
    productCards.forEach(card => {
        const firstOption = card.querySelector('.variant-option');
        if (firstOption) {
            firstOption.classList.add('selected');
        }
    });
    
    // Modify add to cart function to get selected variant
    const addToCartButtons = document.querySelectorAll('.add-to-cart-btn');
    addToCartButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            // Prevent default cart adding behavior (it will be handled by the cart.js file)
            // This just adds variant selection functionality
            const productCard = this.closest('.product-card');
            const selectedVariant = productCard.querySelector('.variant-option.selected');
            
            if (selectedVariant) {
                // Store selected variant in a data attribute for the cart.js to use
                this.setAttribute('data-selected-variant', selectedVariant.textContent);
            }
        });
    });
    
    // Filter products based on selections
    const phoneModelSelect = document.getElementById('phone-model');
    const categoriesSelect = document.getElementById('categories');
    const sortBySelect = document.getElementById('sort-by');
    
    function applyFilters() {
        const phoneModel = phoneModelSelect.value;
        const category = categoriesSelect.value;
        const sortBy = sortBySelect.value;
        
        // Logic to filter and sort products based on selections
        // This would typically involve server-side filtering or 
        // client-side manipulation of the product display
        console.log(`Filtering: Phone=${phoneModel}, Category=${category}, Sort=${sortBy}`);
        
        // Just a placeholder for demonstration
        showNotification(`Filters applied: ${phoneModel}/${category}/${sortBy}`);
    }
    
    // Add event listeners to filter controls
    if (phoneModelSelect) phoneModelSelect.addEventListener('change', applyFilters);
    if (categoriesSelect) categoriesSelect.addEventListener('change', applyFilters);
    if (sortBySelect) sortBySelect.addEventListener('change', applyFilters);
    
    // Helper notification function (should be defined in cart.js)
    function showNotification(message) {
        // Check if function exists in the global scope
        if (typeof window.showNotification === 'function') {
            window.showNotification(message);
        } else {
            // Fallback implementation
            console.log('Notification:', message);
            
            const notification = document.createElement('div');
            notification.classList.add('notification');
            notification.textContent = message;
            
            document.body.appendChild(notification);
            
            // Show notification
            setTimeout(() => {
                notification.classList.add('show');
            }, 10);
            
            // Hide and remove notification
            setTimeout(() => {
                notification.classList.remove('show');
                setTimeout(() => {
                    document.body.removeChild(notification);
                }, 300);
            }, 3000);
        }
    }
});