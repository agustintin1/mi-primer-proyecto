productos = [
    {"nombre": "Zapatillas Urbanas", "precio": 45000},
    {"nombre": "Remera Oversize", "precio": 18000},
    {"nombre": "Buzo Hoodie", "precio": 35000},
    {"nombre": "Pantalón Cargo", "precio": 28000}
]

descuento_porcentaje = 20

print("🔥 ¡LISTA DE OFERTAS DEL DÍA! 🔥\n")

for item in productos:
    precio_original = item["precio"]
    monto_descuento = precio_original * (descuento_porcentaje / 100)
    precio_final = precio_original - monto_descuento
    
    print(f"📌 {item['nombre']}")
    print(f"   Precio Anterior: ${precio_original:,.0f}")
    print(f"   ¡Llevalo HOY ({descuento_porcentaje}% OFF) a solo: ${precio_final:,.0f}!")
    print(f"   (Ahorrás: ${monto_descuento:,.0f})\n")

print("------------------------------------------")
print("Copia este texto y pegalo en tu Canal de WhatsApp o Historias.")