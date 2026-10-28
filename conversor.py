# ==========================================
# CONVERSOR DE MONEDAS Y RESUMEN
# Creado por: agustintin1
# ==========================================

# Cotización fija de ejemplo
COTIZACION_DOLAR = 1250.0

historial = []

while True:
    print("\n==============================")
    print("💵 CONVERSOR DE MONEDAS")
    print(f"📌 Cotización del día: $1 USD = ${COTIZACION_DOLAR} ARS")
    print("==============================")
    print("1. Convertir Pesos (ARS) a Dólares (USD)")
    print("2. Convertir Dólares (USD) a Pesos (ARS)")
    print("3. Ver historial de conversiones")
    print("4. Salir")
    
    opcion = input("\nSelecciona una opción (1-4): ")
    
    if opcion == "1":
        monto_pesos = float(input("\nIngresa la cantidad de Pesos (ARS): $"))
        resultado_usd = monto_pesos / COTIZACION_DOLAR
        print(f"👉 ${monto_pesos:,.2f} ARS equivalen a: US${resultado_usd:,.2f}")
        
        historial.append(f"ARS ${monto_pesos:,.2f} ➔ US${resultado_usd:,.2f}")
        input("\nPresiona [Enter] para continuar...")
        
    elif opcion == "2":
        monto_usd = float(input("\nIngresa la cantidad de Dólares (USD): US$"))
        resultado_pesos = monto_usd * COTIZACION_DOLAR
        print(f"👉 US${monto_usd:,.2f} equivalen a: ${resultado_pesos:,.2f} ARS")
        
        historial.append(f"US${monto_usd:,.2f} ➔ ARS ${resultado_pesos:,.2f}")
        input("\nPresiona [Enter] para continuar...")
        
    elif opcion == "3":
        print("\n--- HISTORIAL DE CONVERSIONES ---")
        if len(historial) == 0:
            print("No hiciste conversiones todavía.")
        else:
            for i, reg in enumerate(historial, 1):
                print(f"{i}. {reg}")
        input("\nPresiona [Enter] para continuar...")
        
    elif opcion == "4":
        print("\n¡Gracias por usar el conversor! ¡Nos vemos, crack!")
        break
    else:
        print("❌ Opción inválida.")
        input("\nPresiona [Enter] para continuar...")