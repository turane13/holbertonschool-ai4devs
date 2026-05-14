def add_to_cart(item, cart=[]):
    if item is None:
        return cart
        
    cart.append(item)
    
    total_items = len(cart)
    print("Cart updated")
    
    return cart
