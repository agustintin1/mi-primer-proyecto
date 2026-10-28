# ==========================================
# AGENDA INTELIGENTE Y GENERADOR DE CLAVES
# Creado por: agustintin1
# ==========================================

import random

# Memoria inicial de tareas
tareas = ["Estudiar programación", "Comprar yerba Canarias", "Ir al gimnasio"]

while True:
    print("\n==============================")
    print("📋 MI SUPER AGENDA & HERRAMIENTAS")
    print("==============================")
    print("1. Ver mis tareas pendientes")
    print("2. Agregar una nueva tarea")
    print("3. Generar contraseña segura")
    print("4. Salir")
    
    opcion = input("\nElige una opción (1-4): ")
    
    if opcion == "1":
        print("\n--- TUS TAREAS ACTUALES ---")
        if len(tareas) == 0:
            print("¡No hay tareas pendientes por ahora!")
        else:
            for indice, una_tarea in enumerate(tareas, 1):
                print(f"{indice}. {una_tarea}")
                
    elif opcion == "2":
        nueva = input("Escribe la nueva tarea que quieres agregar: ")
        tareas.append(nueva)
        print(f"✅ ¡Tarea '{nueva}' agregada con éxito!")
        
    elif opcion == "3":
        print("\n--- GENERADOR DE CONTRASEÑAS ---")
        caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%"
        longitud = 8
        # Creamos la contraseña mezclando caracteres al azar
        password_generada = "".join(random.choices(caracteres, k=longitud))
        print(f"🔑 Tu nueva contraseña segura es: {password_generada}")
        
    elif opcion == "4":
        print("\n¡Gracias por usar la agenda! ¡Hasta luego, crack!")
        break
    else:
        print("❌ Opción inválida. Elige un número del 1 al 4.")