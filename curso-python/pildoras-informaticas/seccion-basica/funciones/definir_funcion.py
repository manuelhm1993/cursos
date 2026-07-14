def imprimir_mensaje():
    print("Estamos aprendiendo Python")
    print("Estamos aprendiendo instrucciones básicas")
    print("Poco a poco iremos avanzando")

for i in range(5):
    print(f"Iteración #{i + 1}")
    imprimir_mensaje()
    
    if i == 3:
        print("\nEjecutando código fuera de la función")
    
    print()