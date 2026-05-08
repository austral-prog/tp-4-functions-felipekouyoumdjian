# ---- Funciones provistas (NO modificar) ----

def apply_discount(price, discount_pct):
    """Dado un precio y un porcentaje de descuento, retorna el precio con el descuento aplicado."""
    return price * (1 - discount_pct / 100)

def apply_tax(price, tax_pct):
    """Dado un precio y un porcentaje de impuesto, retorna el precio con el impuesto aplicado."""
    return price * (1 + tax_pct / 100)

# ---- Funciones a implementar ----

def final_price(price, quantity, discount_pct, tax_pct):
    subtotal = price * quantity
    descuento = apply_discount(subtotal, discount_pct) 
    impuesto = apply_tax(descuento, tax_pct)
    
    return round(impuesto, 2) 

def best_deal(price_a, qty_a, disc_a, price_b, qty_b, disc_b, tax_pct):
    A = final_price(price_a, qty_a, disc_a, tax_pct)
    B = final_price(price_b, qty_b, disc_b, tax_pct)

    if A <= B:
        return "A"
    else: 
        return "B"
    